import tensorflow as tf
import numpy as np
import random
import math
import copy
from itertools import groupby


class pretrain_dhgm():
    """
    Create dynamic HGM model
    """

    def __init__(self, kg, data_process):
        print("Im here in death")
        # tf.compat.v1.disable_v2_behavior()
        # tf.compat.v1.disable_eager_execution()
        self.kg = kg
        self.data_process = data_process
        # self.hetro_model = hetro_model
        self.train_data = self.data_process.train_patient
        self.test_data = self.data_process.test_patient
        self.length_train = len(self.train_data)
        self.length_test = len(self.test_data)
        self.batch_size = 16
        self.time_sequence = 4
        self.time_step_length = 6
        self.predict_window_prior = self.time_sequence * self.time_step_length
        self.latent_dim_cell_state = 100
        self.latent_dim_att = 100
        self.latent_dim_demo = 50
        self.epoch = 2
        self.item_size = len(list(kg.dic_vital.keys()))
        self.demo_size = len(list(kg.dic_race.keys()))
        self.lab_size = len(list(kg.dic_lab.keys()))
        self.latent_dim = self.item_size + self.lab_size
        self.com_size = 12
        self.input_seq = []
        self.threshold = 0.5
        self.positive_lab_size = 5
        self.negative_lab_size = 10
        self.positive_sample_size = self.positive_lab_size + 1
        # self.positive_sample_size = 2
        self.negative_sample_size = self.negative_lab_size + 1
        # self.negative_sample_size = 2
        self.neighbor_pick_skip = 5
        self.neighbor_pick_neg = 10
        self.neighbor_death = len(kg.dic_death[1])
        self.neighbor_discharge = len(kg.dic_death[0])
        """
        define LSTM variables
        """
        self.init_hiddenstate = tf.keras.backend.placeholder(
            [None, 1 + self.positive_lab_size + self.negative_lab_size, self.latent_dim])
        self.input_y_logit = tf.keras.backend.placeholder([None, 2])
        self.input_y_logit_intubate = tf.keras.backend.placeholder([None, 1])
        self.input_x_vital = tf.keras.backend.placeholder(
            [None, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.item_size])
        self.input_x_lab = tf.keras.backend.placeholder(
            [None, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.lab_size])
        self.input_icu_intubation = tf.keras.backend.placeholder([None,self.time_sequence,1+self.positive_lab_size+self.negative_lab_size,2])
        self.input_x = tf.concat([self.input_x_vital, self.input_x_lab], 3)
        #self.input_x = tf.concat([self.input_x,self.input_icu_intubation],3)
        self.input_x_demo = tf.keras.backend.placeholder(
            [None, 1 + self.positive_lab_size + self.negative_lab_size, self.demo_size])
        self.input_x_com = tf.keras.backend.placeholder(
            [None, 1 + self.positive_lab_size + self.negative_lab_size, self.com_size])
        # self.input_x_demo = tf.concat([self.input_x_demo_,self.input_x_com],2)
        self.init_forget_gate = tf.keras.initializers.he_normal(seed=None)
        self.init_info_gate = tf.keras.initializers.he_normal(seed=None)
        self.init_cell_state = tf.keras.initializers.he_normal(seed=None)
        self.init_output_gate = tf.keras.initializers.he_normal(seed=None)
        self.init_forget_gate_weight = tf.keras.initializers.he_normal(seed=None)
        self.init_info_gate_weight = tf.keras.initializers.he_normal(seed=None)
        self.init_cell_state_weight = tf.keras.initializers.he_normal(seed=None)
        self.weight_forget_gate = \
            tf.Variable(
                self.init_forget_gate(shape=(self.item_size + self.lab_size + self.latent_dim, self.latent_dim)))
        self.weight_info_gate = \
            tf.Variable(self.init_info_gate(shape=(self.item_size + self.lab_size + self.latent_dim, self.latent_dim)))
        self.weight_cell_state = \
            tf.Variable(self.init_cell_state(shape=(self.item_size + self.lab_size + self.latent_dim, self.latent_dim)))
        self.weight_output_gate = \
            tf.Variable(
                self.init_output_gate(shape=(self.item_size + self.lab_size + self.latent_dim, self.latent_dim)))
        self.bias_forget_gate = tf.Variable(self.init_forget_gate_weight(shape=(self.latent_dim,)))
        self.bias_info_gate = tf.Variable(self.init_info_gate_weight(shape=(self.latent_dim,)))
        self.bias_cell_state = tf.Variable(self.init_cell_state_weight(shape=(self.latent_dim,)))
        self.bias_output_gate = tf.Variable(self.init_output_gate(shape=(self.latent_dim,)))


        """
        Define LSTM variables plus attention
        """
        self.init_hiddenstate_att = tf.keras.backend.placeholder([None,
                                                                  1 + self.positive_lab_size + self.negative_lab_size + self.neighbor_pick_skip + self.neighbor_pick_neg,
                                                                  self.latent_dim])
        self.input_x_vital_att = tf.keras.backend.placeholder([None, self.time_sequence,
                                                               1 + self.positive_lab_size + self.negative_lab_size + self.neighbor_pick_skip + self.neighbor_pick_neg,
                                                               self.item_size])
        self.input_x_lab_att = tf.keras.backend.placeholder([None, self.time_sequence,
                                                             1 + self.positive_lab_size + self.negative_lab_size + self.neighbor_pick_skip + self.neighbor_pick_neg,
                                                             self.lab_size])
        self.input_x_att = tf.concat([self.input_x_vital_att, self.input_x_lab_att], 3)
        self.input_x_demo_att = tf.keras.backend.placeholder([None,
                                                              1 + self.positive_lab_size + self.negative_lab_size + self.neighbor_pick_skip + self.neighbor_pick_neg,
                                                              self.demo_size])

        """
        Define relation model
        """
        self.shape_relation = (self.latent_dim + self.latent_dim_demo,)
        self.init_mortality = tf.keras.initializers.he_normal(seed=None)
        self.init_lab = tf.keras.initializers.he_normal(seed=None)
        """
        Define parameters
        """
        self.mortality = tf.keras.backend.placeholder([None, 2, 2])
        self.Death_input = tf.keras.backend.placeholder([1, 2])
        self.init_weight_mortality = tf.keras.initializers.he_normal(seed=None)
        self.weight_mortality = \
            tf.Variable(self.init_weight_mortality(shape=(2, self.latent_dim + self.latent_dim_demo)))
        self.bias_mortality = tf.Variable(self.init_weight_mortality(shape=(self.item_size+self.lab_size + self.latent_dim_demo,)))

        self.lab_test = \
            tf.keras.backend.placeholder([None, self.positive_lab_size + self.negative_lab_size, self.item_size])
        self.weight_lab = \
            tf.Variable(self.init_weight_mortality(shape=(self.item_size, self.latent_dim)))
        self.bias_lab = tf.Variable(self.init_weight_mortality(shape=(self.latent_dim,)))
        """
        relation type 
        """
        self.relation_mortality = tf.Variable(self.init_mortality(shape=self.shape_relation))
        self.relation_lab = tf.Variable(self.init_lab(shape=self.shape_relation))

        """
        Define attention mechanism
        """
        self.init_weight_att_W = tf.keras.initializers.he_normal(seed=None)
        self.init_weight_vec_a = tf.keras.initializers.he_normal(seed=None)
        self.weight_att_W = tf.Variable(self.init_weight_att_W(
            shape=(self.latent_dim + self.latent_dim_demo, self.latent_dim_att + self.latent_dim_demo)))
        self.weight_vec_a = tf.Variable(
            self.init_weight_vec_a(shape=(2 * (self.latent_dim_att + self.latent_dim_demo), 1)))

        """
        Define attention on sample neighbors
        """
        self.init_weight_vec_a_neighbor = tf.keras.initializers.he_normal(seed=None)
        self.weight_vec_a_neighbor = tf.Variable(
            self.init_weight_vec_a_neighbor(shape=(self.latent_dim + self.latent_dim_demo, 1)))

        """
        Define attention on Retain model for time
        """
        self.init_retain_b = tf.keras.initializers.he_normal(seed=None)
        self.init_retain_weight = tf.keras.initializers.he_normal(seed=None)
        self.weight_retain_w = tf.Variable(self.init_retain_weight(shape=(self.latent_dim, 1)))

        """
        Define attention on Retain model for feature variable
        """
        self.init_retain_variable_b = tf.keras.initializers.he_normal(seed=None)
        self.bias_retain_variable_b = tf.Variable(self.init_retain_variable_b(shape=(self.latent_dim,)))
        self.init_retain_variable_w = tf.keras.initializers.he_normal(seed=None)
        self.weight_retain_variable_w = tf.Variable(
            self.init_retain_variable_w(shape=(self.latent_dim, self.latent_dim)))

        """
        Define classification matrix for lstm
        """
        self.init_bias_classification_b = tf.keras.initializers.he_normal(seed=None)
        self.init_weight_classification_w = tf.keras.initializers.he_normal(seed=None)
        self.bias_classification_b = tf.Variable(self.init_bias_classification_b(shape=(1,)))
        self.weight_classification_w = tf.Variable(
            self.init_weight_classification_w(shape=(self.latent_dim + self.latent_dim_demo, 1)))

        """
        Define input projection
        """
        self.init_projection_b = tf.keras.initializers.he_normal(seed=None)
        self.bias_projection_b = tf.Variable(self.init_projection_b(shape=(self.latent_dim,)))
        self.init_projection_w = tf.keras.initializers.he_normal(seed=None)
        self.weight_projection_w = tf.Variable(
            self.init_projection_w(shape=(self.lab_size+self.item_size, self.latent_dim)))

    def lstm_cell(self):
        cell_state = []
        hidden_rep = []
        self.project_input = tf.math.add(tf.matmul(self.input_x, self.weight_projection_w), self.bias_projection_b)
        #self.project_input = tf.matmul(self.input_x, self.weight_projection_w)
        for i in range(self.time_sequence):
            x_input_cur = tf.gather(self.project_input, i, axis=1)
            if i == 0:
                concat_cur = tf.concat([self.init_hiddenstate, x_input_cur], 2)
            else:
                concat_cur = tf.concat([hidden_rep[i - 1], x_input_cur], 2)
            forget_cur = \
                tf.math.sigmoid(tf.math.add(tf.matmul(concat_cur, self.weight_forget_gate), self.bias_forget_gate))
            info_cur = \
                tf.math.sigmoid(tf.math.add(tf.matmul(concat_cur, self.weight_info_gate), self.bias_info_gate))
            cellstate_cur = \
                tf.math.tanh(tf.math.add(tf.matmul(concat_cur, self.weight_cell_state), self.bias_cell_state))
            info_cell_state = tf.multiply(info_cur, cellstate_cur)
            if not i == 0:
                forget_cell_state = tf.multiply(forget_cur, cell_state[i - 1])
                cellstate_cur = tf.math.add(forget_cell_state, info_cell_state)
            output_gate = \
                tf.nn.relu(tf.math.add(tf.matmul(concat_cur, self.weight_output_gate), self.bias_output_gate))
            hidden_current = tf.multiply(output_gate, cellstate_cur)
            cell_state.append(cellstate_cur)
            hidden_rep.append(hidden_current)

        self.hidden_last = hidden_rep[self.time_sequence - 1]
        for i in range(self.time_sequence):
            hidden_rep[i] = tf.expand_dims(hidden_rep[i], 1)
        self.hidden_rep = tf.concat(hidden_rep, 1)
        self.check = concat_cur


    def demo_layer(self):
        self.Dense_demo = tf.compat.v1.layers.dense(inputs=self.input_x_demo,
                                                    units=self.latent_dim_demo,
                                                    kernel_initializer=tf.keras.initializers.he_normal(seed=None),
                                                    activation=tf.nn.relu)


    def build_dhgm_model(self):
        """
        Build dynamic HGM model
        """
        #self.Dense_patient = tf.expand_dims(self.hidden_last,1)
        #self.Dense_patient = tf.concat([self.hidden_last,self.Dense_demo],2)


        self.hidden_att_e = tf.matmul(self.hidden_rep,self.weight_retain_w)
        self.hidden_att_e_softmax = tf.nn.softmax(self.hidden_att_e,1)
        self.hidden_att_e_broad = tf.broadcast_to(self.hidden_att_e_softmax,[tf.shape(self.input_x_vital)[0],
                                                                             self.time_sequence,1+self.positive_lab_size+self.negative_lab_size,self.latent_dim])


        self.hidden_att_e_variable = tf.math.sigmoid(
            tf.math.add(tf.matmul(self.hidden_rep, self.weight_retain_variable_w), self.bias_retain_variable_b))
        # self.hidden_att_e_softmax = tf.nn.softmax(self.hidden_att_e, -1)
        self.parameter_mul = tf.multiply(self.hidden_att_e_broad,self.hidden_att_e_variable)
        self.hidden_mul_variable = tf.multiply(self.parameter_mul, self.project_input)
        # self.hidden_final = tf.reduce_sum(self.hidden_mul, 1)
        self.hidden_final = tf.reduce_sum(self.hidden_mul_variable, 1)
        self.Dense_patient = tf.concat([self.hidden_final, self.Dense_demo], 2)
        #self.Dense_patient = tf.concat([self.hidden_mul_variable, self.Dense_demo], 2)


        #self.Dense_patient = self.hidden_last_comb
        # self.Dense_patient = tf.expand_dims(self.hidden_rep,2)


        self.Dense_mortality_ = \
            tf.nn.relu(tf.math.add(tf.matmul(self.mortality, self.weight_mortality), self.bias_mortality))

        self.Dense_mortality = tf.math.subtract(self.Dense_mortality_, self.relation_mortality)

        self.Dense_death_rep_ = \
            tf.nn.relu(tf.math.add(tf.matmul(self.Death_input, self.weight_mortality), self.bias_mortality))

        self.Dense_death_rep = tf.math.subtract(self.Dense_death_rep_, self.relation_mortality)

        idx_origin = tf.constant([0])
        self.x_origin_entropy = tf.squeeze(tf.gather(self.Dense_patient, idx_origin, axis=1),axis=1)

        self.output_layer = tf.math.sigmoid(
            tf.math.add(tf.matmul(self.x_origin_entropy, self.weight_classification_w), self.bias_classification_b))

        self.bce = tf.keras.losses.BinaryCrossentropy()
        self.cross_entropy = self.bce(self.input_y_logit_intubate, self.output_layer)

        """
        Get interpretation matrix
        """
        """
        self.braod_weight_variable = tf.broadcast_to(self.weight_projection_w,[tf.shape(self.input_x_vital)[0],
                                                                               self.time_sequence,
                                                                               1+self.positive_lab_size+self.negative_lab_size,
                                                                               self.latent_dim,self.latent_dim])

        self.exp_hidden_att_e_variable = tf.expand_dims(self.hidden_att_e_variable,axis=3)
        self.broad_hidden_att_e_variable = tf.broadcast_to(self.exp_hidden_att_e_variable,[tf.shape(self.input_x_vital)[0],
                                                                               self.time_sequence,
                                                                               1+self.positive_lab_size+self.negative_lab_size,
                                                                               self.latent_dim,self.latent_dim])

        self.exp_hidden_att_e_broad = tf.expand_dims(self.hidden_att_e_broad,axis=3)
        self.broad_hidden_att_e = tf.broadcast_to(self.exp_hidden_att_e_broad,[tf.shape(self.input_x_vital)[0],
                                                                               self.time_sequence,
                                                                               1+self.positive_lab_size+self.negative_lab_size,
                                                                               self.latent_dim,self.latent_dim])
        self.project_weight_variable = tf.multiply(self.broad_hidden_att_e_variable, self.braod_weight_variable)
        self.project_weight_variable_final = tf.multiply(self.broad_hidden_att_e,self.project_weight_variable)
        """
        """
        Get score important
        """
        """
        self.time_feature_index = tf.constant([i for i in range(self.lab_size+self.item_size)])
        self.mortality_hidden_rep = tf.gather(self.Dense_death_rep, self.time_feature_index, axis=1)
        self.score_attention_ = tf.matmul(self.project_weight_variable_final,tf.expand_dims(tf.squeeze(self.mortality_hidden_rep),1))
        self.score_attention = tf.squeeze(self.score_attention_,[4])
        self.input_importance = tf.multiply(self.score_attention,self.input_x)
        """


        """
        self.Dense_lab_ = \
            tf.nn.relu(tf.math.add(tf.matmul(self.lab_test,self.weight_lab),self.bias_lab))
        self.Dense_lab = tf.math.add(self.Dense_lab_,self.relation_lab)
        """

    def build_att_mortality(self):
        """
        build attention model for mortality node
        """
        self.att_skip_latent = tf.matmul(self.x_att_skip, self.weight_att_W)
        self.x_skip_center_brod = tf.broadcast_to(self.x_skip_mor, [self.batch_size, self.neighbor_pick_skip,
                                                                    self.latent_dim_att + self.latent_dim_demo])
        self.att_skip_center = tf.matmul(self.x_skip_center_brod, self.weight_att_W)
        self.concat_att_skip = tf.concat([self.att_skip_center, self.att_skip_latent], axis=2)

        self.att_neg_latent = tf.matmul(self.x_att_neg, self.weight_att_W)
        self.x_neg_center_brod = tf.broadcast_to(self.x_negative_mor, [self.batch_size, self.neighbor_pick_neg,
                                                                       self.latent_dim_att + self.latent_dim_demo])
        self.att_neg_center = tf.matmul(self.x_neg_center_brod, self.weight_att_W)
        self.concat_att_neg = tf.concat([self.att_neg_center, self.att_neg_latent], axis=2)

        """
        times the weight vector a
        """
        self.weight_att_skip_a = tf.matmul(self.concat_att_skip, self.weight_vec_a)
        self.weight_att_neg_a = tf.matmul(self.concat_att_neg, self.weight_vec_a)

        self.soft_max_att_skip = tf.broadcast_to(tf.nn.softmax(self.weight_att_skip_a, axis=1),
                                                 [self.batch_size, self.neighbor_pick_skip,
                                                  self.latent_dim_att + self.latent_dim_demo])
        self.soft_max_att_neg = tf.broadcast_to(tf.nn.softmax(self.weight_att_neg_a, axis=1),
                                                [self.batch_size, self.neighbor_pick_neg,
                                                 self.latent_dim_att + self.latent_dim_demo])

        self.att_rep_skip_mor = tf.multiply(self.soft_max_att_skip, self.att_skip_latent)
        self.att_rep_neg_mor = tf.multiply(self.soft_max_att_neg, self.att_neg_latent)

        self.att_rep_skip_mor_sum = tf.reduce_sum(self.att_rep_skip_mor, 1)
        self.att_rep_neg_mor_sum = tf.reduce_sum(self.att_rep_neg_mor, 1)

        self.att_rep_skip_mor_final = tf.nn.relu(self.att_rep_skip_mor_sum)
        self.att_rep_neg_mor_final = tf.nn.relu(self.att_rep_neg_mor_sum)

    def get_latent_rep_hetero(self):
        """
        Prepare data for SGNS loss function
        """
        idx_origin = tf.constant([0])
        self.x_origin = tf.gather(self.Dense_patient, idx_origin, axis=1)
        # self.x_origin = self.hidden_last

        idx_skip_mortality = tf.constant([0])
        self.x_skip_mor = tf.gather(self.Dense_mortality, idx_skip_mortality, axis=1)
        idx_neg_mortality = tf.constant([1])
        self.x_negative_mor = tf.gather(self.Dense_mortality, idx_neg_mortality, axis=1)

        """
        item_idx_skip = tf.constant([i+1 for i in range(self.positive_lab_size)])
        self.x_skip_item = tf.gather(self.Dense_lab,item_idx_skip,axis=1)
        item_idx_negative = tf.constant([i+self.positive_lab_size+1 for i in range(self.negative_lab_size)])
        self.x_negative_item = tf.gather(self.Dense_lab,item_idx_negative,axis=1)
        self.x_skip = tf.concat([self.x_skip,self.x_skip_item],axis=1)
        self.x_negative = tf.concat([self.x_negative,self.x_negative_item],axis=1)
        """
        patient_idx_skip = tf.constant([i + 1 for i in range(self.positive_lab_size)])
        self.x_skip_patient = tf.gather(self.Dense_patient, patient_idx_skip, axis=1)
        patient_idx_negative = tf.constant([i + self.positive_lab_size + 1 for i in range(self.negative_lab_size)])
        self.x_negative_patient = tf.gather(self.Dense_patient, patient_idx_negative, axis=1)

        # self.process_patient_att()

        self.x_skip = tf.concat([self.x_skip_mor, self.x_skip_patient], axis=1)
        self.x_negative = tf.concat([self.x_negative_mor, self.x_negative_patient], axis=1)


    def get_positive_patient(self, center_node_index):
        self.patient_pos_sample_vital = np.zeros((self.time_sequence, self.positive_lab_size + 1, self.item_size))
        self.patient_pos_sample_lab = np.zeros((self.time_sequence, self.positive_lab_size + 1, self.lab_size))
        self.patient_pos_sample_icu_intubation_label = np.zeros((self.time_sequence, self.positive_lab_size+1, 2))
        self.patient_pos_sample_demo = np.zeros((self.positive_lab_size + 1, self.demo_size))
        self.patient_pos_sample_com = np.zeros((self.positive_lab_size + 1, self.com_size))
        if self.kg.dic_patient[center_node_index]['death_flag'] == 0:
            flag = 0
            neighbor_patient = self.kg.dic_death[0]
        else:
            flag = 1
            neighbor_patient = self.kg.dic_death[1]
        time_seq = self.kg.dic_patient[center_node_index]['prior_time_vital'].keys()
        time_seq_int = [np.int(k) for k in time_seq]
        time_seq_int.sort()
        # time_index = 0
        # for j in self.time_seq_int:
        for j in range(self.time_sequence):
            # if time_index == self.time_sequence:
            #    break
            if flag == 0:
                pick_death_hour = self.kg.mean_death_time + np.int(np.floor(np.random.normal(0, 20, 1)))
                start_time = pick_death_hour - self.predict_window_prior + float(j) * self.time_step_length
                end_time = start_time + self.time_step_length
            else:
                start_time = self.kg.dic_patient[center_node_index]['death_hour'] - self.predict_window_prior + float(
                    j) * self.time_step_length
                end_time = start_time + self.time_step_length
            one_data_vital = self.assign_value_patient(center_node_index, start_time, end_time)
            one_data_lab = self.assign_value_lab(center_node_index, start_time, end_time)
            one_data_icu_label = self.assign_value_icu_intubation(center_node_index, start_time, end_time)
            # one_data_demo = self.assign_value_demo(center_node_index)
            self.patient_pos_sample_vital[j, 0, :] = one_data_vital
            self.patient_pos_sample_lab[j, 0, :] = one_data_lab
            self.patient_pos_sample_icu_intubation_label[j,0,:] = one_data_icu_label
            # time_index += 1
        one_data_demo = self.assign_value_demo(center_node_index)
        # one_data_com = self.assign_value_com(center_node_index)
        self.patient_pos_sample_demo[0, :] = one_data_demo
        # self.patient_pos_sample_com[0,:] = one_data_com
        for i in range(self.positive_lab_size):
            index_neighbor = np.int(np.floor(np.random.uniform(0, len(neighbor_patient), 1)))
            patient_id = neighbor_patient[index_neighbor]
            time_seq = self.kg.dic_patient[patient_id]['prior_time_vital'].keys()
            time_seq_int = [np.int(k) for k in time_seq]
            time_seq_int.sort()
            one_data_demo = self.assign_value_demo(patient_id)
            # one_data_com = self.assign_value_com(patient_id)
            self.patient_pos_sample_demo[i + 1, :] = one_data_demo
            # self.patient_pos_sample_com[i+1,:] = one_data_com
            # time_index = 0
            # for j in time_seq_int:
            for j in range(self.time_sequence):
                # if time_index == self.time_sequence:
                #   break
                # self.time_index = np.int(j)
                # start_time = float(j)*self.time_step_length
                # end_time = start_time + self.time_step_length
                if flag == 0:
                    pick_death_hour = self.kg.mean_death_time + np.int(np.floor(np.random.normal(0, 20, 1)))
                    start_time = pick_death_hour - self.predict_window_prior + float(j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                else:
                    start_time = self.kg.dic_patient[patient_id]['death_hour'] - self.predict_window_prior + float(
                        j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                one_data_vital = self.assign_value_patient(patient_id, start_time, end_time)
                one_data_lab = self.assign_value_lab(patient_id, start_time, end_time)
                one_data_icu_label = self.assign_value_icu_intubation(patient_id, start_time, end_time)
                self.patient_pos_sample_vital[j, i + 1, :] = one_data_vital
                self.patient_pos_sample_lab[j, i + 1, :] = one_data_lab
                self.patient_pos_sample_icu_intubation_label[j,i+1,:] = one_data_icu_label
                # time_index += 1

    def get_negative_patient(self, center_node_index):
        self.patient_neg_sample_vital = np.zeros((self.time_sequence, self.negative_lab_size, self.item_size))
        self.patient_neg_sample_lab = np.zeros((self.time_sequence, self.negative_lab_size, self.lab_size))
        self.patient_neg_sample_icu_intubation_label = np.zeros((self.time_sequence,self.negative_lab_size,2))
        self.patient_neg_sample_demo = np.zeros((self.negative_lab_size, self.demo_size))
        self.patient_neg_sample_com = np.zeros((self.negative_lab_size, self.com_size))
        if self.kg.dic_patient[center_node_index]['death_flag'] == 0:
            neighbor_patient = self.kg.dic_death[1]
            flag = 1
        else:
            neighbor_patient = self.kg.dic_death[0]
            flag = 0
        for i in range(self.negative_lab_size):
            index_neighbor = np.int(np.floor(np.random.uniform(0, len(neighbor_patient), 1)))
            patient_id = neighbor_patient[index_neighbor]
            time_seq = self.kg.dic_patient[patient_id]['prior_time_vital'].keys()
            time_seq_int = [np.int(k) for k in time_seq]
            time_seq_int.sort()
            time_index = 0
            one_data_demo = self.assign_value_demo(patient_id)
            # one_data_com = self.assign_value_com(patient_id)
            self.patient_neg_sample_demo[i, :] = one_data_demo
            # self.patient_neg_sample_com[i,:] = one_data_com
            # for j in time_seq_int:
            for j in range(self.time_sequence):
                # if time_index == self.time_sequence:
                #   break
                # self.time_index = np.int(j)
                # start_time = float(j)*self.time_step_length
                # end_time = start_time + self.time_step_length
                if flag == 0:
                    pick_death_hour = self.kg.mean_death_time + np.int(np.floor(np.random.normal(0, 20, 1)))
                    start_time = pick_death_hour - self.predict_window_prior + float(j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                else:
                    start_time = self.kg.dic_patient[patient_id]['death_hour'] - self.predict_window_prior + float(
                        j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                one_data_vital = self.assign_value_patient(patient_id, start_time, end_time)
                one_data_lab = self.assign_value_lab(patient_id, start_time, end_time)
                one_data_icu_label = self.assign_value_icu_intubation(patient_id,start_time,end_time)
                self.patient_neg_sample_vital[j, i, :] = one_data_vital
                self.patient_neg_sample_lab[j, i, :] = one_data_lab
                self.patient_neg_sample_icu_intubation_label[j,i,:] = one_data_icu_label
                # time_index += 1

    """
    def get_negative_sample_rep(self):
        self.item_neg_sample = np.zeros((self.negative_lab_size,self.item_size))
        index = 0
        for i in self.neg_nodes_item:
            one_sample_neg_item = self.assign_value_item(i)
            self.item_neg_sample[index,:] = one_sample_neg_item
            index += 1
    """

    def SGNN_loss(self):
        """
        implement sgnn loss
        """
        negative_training_norm = tf.math.l2_normalize(self.x_negative, axis=2)

        skip_training = tf.broadcast_to(self.x_origin,
                                        [self.batch_size, self.negative_sample_size,
                                         self.latent_dim + self.latent_dim_demo])

        skip_training_norm = tf.math.l2_normalize(skip_training, axis=2)

        dot_prod = tf.multiply(skip_training_norm, negative_training_norm)

        dot_prod_sum = tf.reduce_sum(dot_prod, 2)

        sum_log_dot_prod = tf.math.log(tf.math.sigmoid(tf.math.negative(tf.reduce_mean(dot_prod_sum, 1))))

        positive_training = tf.broadcast_to(self.x_origin, [self.batch_size, self.positive_sample_size,
                                                            self.latent_dim + self.latent_dim_demo])

        positive_skip_norm = tf.math.l2_normalize(self.x_skip, axis=2)

        positive_training_norm = tf.math.l2_normalize(positive_training, axis=2)

        dot_prod_positive = tf.multiply(positive_skip_norm, positive_training_norm)

        dot_prod_sum_positive = tf.reduce_sum(dot_prod_positive, 2)

        sum_log_dot_prod_positive = tf.math.log(tf.math.sigmoid(tf.reduce_mean(dot_prod_sum_positive, 1)))

        self.negative_sum = tf.math.negative(
            tf.reduce_sum(tf.math.add(sum_log_dot_prod, sum_log_dot_prod_positive)))

    def config_model(self):
        self.lstm_cell()
        self.demo_layer()
        # self.softmax_loss()
        self.build_dhgm_model()
        self.get_latent_rep_hetero()
        self.SGNN_loss()
        #self.softmax_loss()
        self.train_step_cross_entropy = tf.train.AdamOptimizer(1e-3).minimize(self.cross_entropy)
        self.train_step_neg = tf.compat.v1.train.AdamOptimizer(1e-3).minimize(self.negative_sum)
        # self.train_step_cross_entropy = tf.train.AdamOptimizer(1e-3).minimize(self.cross_entropy)
        self.sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()
        tf.local_variables_initializer().run()


    def assign_value_patient(self, patientid, start_time, end_time):
        self.one_sample = np.zeros(self.item_size)
        self.freq_sample = np.zeros(self.item_size)
        self.times = []
        for i in self.kg.dic_patient[patientid]['prior_time_vital'].keys():
            if (np.int(i) > start_time or np.int(i) == start_time) and np.int(i) < end_time:
                self.times.append(i)
        for j in self.times:
            for i in self.kg.dic_patient[patientid]['prior_time_vital'][str(j)].keys():
                mean = np.float(self.kg.dic_vital[i]['mean_value'])
                std = np.float(self.kg.dic_vital[i]['std'])
                ave_value = np.mean(
                    [np.float(k) for k in self.kg.dic_patient[patientid]['prior_time_vital'][str(j)][i]])
                index = self.kg.dic_vital[i]['index']
                if std == 0:
                    self.one_sample[index] += 0
                    self.freq_sample[index] += 1
                else:
                    self.one_sample[index] = (np.float(ave_value) - mean) / std
                    self.freq_sample[index] += 1

        out_sample = self.one_sample / self.freq_sample
        for i in range(self.item_size):
            if math.isnan(out_sample[i]):
                out_sample[i] = 0

        return out_sample

    def assign_value_icu_intubation(self,patientid,start_time,end_time):
        one_sample_icu_intubation = np.zeros(2)
        if self.kg.dic_patient[patientid]['icu_label'] == 1:
            icu_hour = self.kg.dic_patient[patientid]['in_icu_hour']
            if icu_hour > start_time:
                one_sample_icu_intubation[0] = 1

        if self.kg.dic_patient[patientid]['intubation_label'] == 1:
            intubation_hour = self.kg.dic_patient[patientid]['intubation_hour']
            if intubation_hour > start_time and intubation_hour < end_time:
                one_sample_icu_intubation[1] = 1
            if intubation_hour < start_time:
                if self.kg.dic_patient[patientid]['extubation_label'] == 1:
                    extubation_hour = self.kg.dic_patient[patientid]['extubation_hour']
                    if extubation_hour > start_time:
                        one_sample_icu_intubation[1] = 1
                if self.kg.dic_patient[patientid]['extubation_label'] == 0:
                    one_sample_icu_intubation[1] = 1

        return one_sample_icu_intubation



    def assign_value_lab(self, patientid, start_time, end_time):
        self.one_sample_lab = np.zeros(self.lab_size)
        self.freq_sample_lab = np.zeros(self.lab_size)
        self.times_lab = []
        for i in self.kg.dic_patient[patientid]['prior_time_lab'].keys():
            if (np.int(i) > start_time or np.int(i) == start_time) and np.int(i) < end_time:
                self.times_lab.append(i)
        for j in self.times_lab:
            for i in self.kg.dic_patient[patientid]['prior_time_lab'][str(j)].keys():
                if i[-1] == 'A':
                    continue
                if i == "EOSINO":
                    continue
                if i == "EOSINO_PERC":
                    continue
                if i == "BASOPHIL":
                    continue
                if i == "BASOPHIL_PERC":
                    continue
                mean = np.float(self.kg.dic_lab[i]['mean_value'])
                std = np.float(self.kg.dic_lab[i]['std'])
                ave_value = np.mean([np.float(k) for k in self.kg.dic_patient[patientid]['prior_time_lab'][str(j)][i]])
                index = self.kg.dic_lab[i]['index']
                if std == 0:
                    self.one_sample_lab[index] += 0
                    self.freq_sample_lab[index] += 1
                else:
                    self.one_sample_lab[index] += (np.float(ave_value) - mean) / std
                    self.freq_sample_lab[index] += 1

        out_sample_lab = self.one_sample_lab / self.freq_sample_lab
        for i in range(self.lab_size):
            if math.isnan(out_sample_lab[i]):
                out_sample_lab[i] = 0

        return out_sample_lab

    def assign_value_demo(self, patientid):
        one_sample = np.zeros(self.demo_size)
        for i in self.kg.dic_demographic[patientid]['race']:
            if i == 'race':
                race = self.kg.dic_demographic[patientid]['race']
                index = self.kg.dic_race[race]['index']
                one_sample[index] = 1
            elif i == 'Age':
                age = self.kg.dic_demographic[patientid]['Age']
                index = self.kg.dic_race['Age']['index']
                if age == 0:
                    one_sample[index] = age
                else:
                    one_sample[index] = (np.float(age) - self.kg.age_mean) / self.kg.age_std
            elif i == 'gender':
                gender = self.kg.dic_demographic[patientid]['gender']
                index = self.kg.dic_race[gender]['index']
                one_sample[index] = 1

        return one_sample

    def assign_value_com(self, patientid):
        one_sample = np.zeros(self.com_size)
        self.com_index = np.where(self.kg.com_mapping_ar[:, 0] == patientid)[0][0]
        deidentify_index = self.kg.com_mapping_ar[self.com_index][1]
        self.map_index = np.where(deidentify_index == self.kg.com_ar[:, 1])[0][0]
        one_sample[:] = [np.int(i) for i in self.kg.com_ar[self.map_index, 4:]]

        return one_sample

    def get_batch_train(self, data_length, start_index, data):
        """
        get training batch data
        """
        train_one_batch_vital = np.zeros(
            (data_length, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.item_size))
        train_one_batch_lab = np.zeros(
            (data_length, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.lab_size))
        train_one_batch_icu_intubation = np.zeros((data_length,self.time_sequence,1+self.positive_lab_size+self.negative_lab_size,2))
        train_one_batch_demo = np.zeros(
            (data_length, 1 + self.positive_lab_size + self.negative_lab_size, self.demo_size))
        train_one_batch_com = np.zeros(
            (data_length, 1 + self.positive_lab_size + self.negative_lab_size, self.com_size))
        # train_one_batch_item = np.zeros((data_length,self.positive_lab_size+self.negative_lab_size,self.item_size))
        train_one_batch_mortality = np.zeros((data_length, 2, 2))
        one_batch_logit = np.zeros((data_length, 2))
        self.real_logit = np.zeros(data_length)
        # self.item_neg_sample = np.zeros((self.negative_lab_size, self.item_size))
        # self.item_pos_sample = np.zeros((self.positive_lab_size, self.item_size))
        index_batch = 0
        index_increase = 0
        # while index_batch < data_length:
        for i in range(data_length):
            self.check_patient = i
            self.patient_id = data[start_index + i]
            # if self.kg.dic_patient[self.patient_id]['item_id'].keys() == {}:
            #   index_increase += 1
            #  continue
            # index_batch += 1
            self.time_seq = self.kg.dic_patient[self.patient_id]['prior_time_vital'].keys()
            self.time_seq_int = [np.int(k) for k in self.time_seq]
            self.time_seq_int.sort()
            time_index = 0
            flag = self.kg.dic_patient[self.patient_id]['death_flag']
            """
            if flag == 0:
                one_batch_logit[i,0,0] = 1
                one_batch_logit[i,1,1] = 1
            else:
                one_batch_logit[i,0,1] = 1
                one_batch_logit[i,1,0] = 1
                self.real_logit[i] = 1
            """
            if flag == 0:
                train_one_batch_mortality[i, 0, :] = [1, 0]
                train_one_batch_mortality[i, 1, :] = [0, 1]
                one_batch_logit[i, 0] = 1
            else:
                train_one_batch_mortality[i, 0, :] = [0, 1]
                train_one_batch_mortality[i, 1, :] = [1, 0]
                one_batch_logit[i, 1] = 1

            self.get_positive_patient(self.patient_id)
            self.get_negative_patient(self.patient_id)
            train_one_data_vital = np.concatenate((self.patient_pos_sample_vital, self.patient_neg_sample_vital),
                                                  axis=1)
            train_one_data_lab = np.concatenate((self.patient_pos_sample_lab, self.patient_neg_sample_lab), axis=1)
            train_one_data_demo = np.concatenate((self.patient_pos_sample_demo, self.patient_neg_sample_demo), axis=0)
            train_one_data_com = np.concatenate((self.patient_pos_sample_com, self.patient_neg_sample_com), axis=0)
            train_one_data_icu_intubation = np.concatenate((self.patient_pos_sample_icu_intubation_label,self.patient_neg_sample_icu_intubation_label),axis=1)
            train_one_batch_vital[i, :, :, :] = train_one_data_vital
            train_one_batch_lab[i, :, :, :] = train_one_data_lab
            train_one_batch_demo[i, :, :] = train_one_data_demo
            train_one_batch_com[i, :, :] = train_one_data_com
            train_one_batch_icu_intubation[i,:,:,:] = train_one_data_icu_intubation

        return train_one_batch_vital, train_one_batch_lab, train_one_batch_demo, one_batch_logit, train_one_batch_mortality, train_one_batch_com,train_one_batch_icu_intubation

    def get_batch_train_intubate(self, data_length, start_index, data):
        """
        get period train data
        """
        one_batch_logit = np.zeros((data_length, 1))
        train_one_batch_vital = np.zeros(
            (data_length, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.item_size))
        train_one_batch_lab = np.zeros(
            (data_length, self.time_sequence, 1 + self.positive_lab_size + self.negative_lab_size, self.lab_size))
        train_one_batch_demo = np.zeros(
            (data_length, 1 + self.positive_lab_size + self.negative_lab_size, self.demo_size))
        train_one_batch_com = np.zeros(
            (data_length, 1 + self.positive_lab_size + self.negative_lab_size, self.com_size))
        for i in range(data_length):
            self.patient_id = data[start_index + i]
            flag = self.kg.dic_patient[self.patient_id]['intubation_label']
            for j in range(self.time_sequence):
                # start_time = float(j)*self.time_step_length
                # end_time = start_time + self.time_step_length
                if flag == 0:
                    #start_time = self.kg.dic_patient[self.patient_id][
                    #                 'discharge_hour'] - self.predict_window_prior + float(j) * self.time_step_length
                    pick_intubate_hour = self.kg.mean_intubate_time + np.int(np.floor(np.random.normal(0, 20, 1)))
                    start_time = pick_intubate_hour - self.predict_window_prior + float(j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                    self.check_start_time = start_time
                else:
                    start_time = self.kg.dic_patient[self.patient_id]['intubation_hour'] - self.predict_window_prior + float(
                        j) * self.time_step_length
                    end_time = start_time + self.time_step_length
                    self.check_start_time = start_time

                self.one_data_vital = self.assign_value_patient(self.patient_id, start_time, end_time)
                self.one_data_lab = self.assign_value_lab(self.patient_id, start_time, end_time)
                train_one_batch_vital[i, j,0, :] = self.one_data_vital
                train_one_batch_lab[i, j,0, :] = self.one_data_lab
            # flag = self.kg.dic_patient[self.patient_id]['death_flag']
            if flag == 1:
                one_batch_logit[i, 0] = 1
            """
            else:
                #death_time_length = self.kg.dic_patient[self.patient_id]['death_hour']-self.train_time_window
                #if death_time_length < self.death_predict_window:
                one_batch_logit[i,1] = 1
            """
            # else:
            # one_batch_logit[i,0] = 1
            self.one_data_demo = self.assign_value_demo(self.patient_id)
            # self.one_data_com = self.assign_value_com(self.patient_id)
            train_one_batch_demo[i,0, :] = self.one_data_demo
            # train_one_batch_com[i,:] = self.one_data_com

        return train_one_batch_vital, train_one_batch_lab, one_batch_logit, train_one_batch_demo, train_one_batch_com

    def train(self):
        """
        train the system
        """
        init_hidden_state = np.zeros(
            (self.batch_size, 1 + self.positive_lab_size + self.negative_lab_size, self.latent_dim))
        iteration = np.int(np.floor(np.float(self.length_train) / self.batch_size))

        for j in range(self.epoch):
            print('epoch')
            print(j)
            for i in range(iteration):
                self.train_one_batch_vital, self.train_one_batch_lab, self.train_one_batch_demo, self.one_batch_logit, self.one_batch_mortality, self.one_batch_com,self.one_batch_icu_intubation = self.get_batch_train(
                    self.batch_size, i * self.batch_size, self.train_data)

                self.err_ = self.sess.run([self.negative_sum, self.train_step_neg],
                                          feed_dict={self.input_x_vital: self.train_one_batch_vital,
                                                     self.input_x_lab: self.train_one_batch_lab,
                                                     self.input_x_demo: self.train_one_batch_demo,
                                                     # self.input_x_com: self.one_batch_com,
                                                     # self.lab_test: self.one_batch_item,
                                                     self.mortality: self.one_batch_mortality,
                                                     self.init_hiddenstate: init_hidden_state,
                                                     self.input_icu_intubation:self.one_batch_icu_intubation})
                print(self.err_[0])

                """
                self.err_lstm = self.sess.run([self.cross_entropy, self.train_step_cross_entropy,self.init_hiddenstate,self.output_layer,self.logit_sig],
                                     feed_dict={self.input_x: self.train_one_batch,
                                                self.input_y_logit: self.one_batch_logit,
                                                self.init_hiddenstate:init_hidden_state})
                print(self.err_lstm[0])
                """

    def train_intubate(self):
        """
        train the system
        """
        init_hidden_state = np.zeros(
            (self.batch_size, 1 + self.positive_lab_size + self.negative_lab_size, self.latent_dim))
        iteration = np.int(np.floor(np.float(self.length_train) / self.batch_size))
        for j in range(self.epoch):
            print('epoch')
            print(j)
            for i in range(iteration):
                self.train_one_batch, self.train_one_batch_lab, self.logit_one_batch, self.train_one_batch_demo, self.train_one_batch_com = self.get_batch_train_intubate(
                    self.batch_size, i * self.batch_size, self.train_data)
                self.err_ = self.sess.run(
                    [self.cross_entropy, self.train_step_cross_entropy, self.init_hiddenstate, self.output_layer],
                    feed_dict={self.input_x_vital: self.train_one_batch,
                               self.input_x_lab: self.train_one_batch_lab,
                               self.input_y_logit_intubate: self.logit_one_batch,
                               self.init_hiddenstate: init_hidden_state,
                               self.input_x_demo: self.train_one_batch_demo})
                print(self.err_[0])


    def test(self, data):
        """
        test the system, return the accuracy of the model
        """
        test_length = len(data)
        init_hidden_state = np.zeros(
            (test_length, 1 + self.positive_lab_size + self.negative_lab_size, self.latent_dim))
        test_data, self.test_data_lab, self.test_logit, self.test_demo, self.test_com = self.get_batch_train_intubate(
            test_length, 0, data)
        self.logit_out = self.sess.run(self.output_layer, feed_dict={self.input_x_vital: test_data,
                                                                     self.input_x_demo: self.test_demo,
                                                                     self.input_x_lab: self.test_data_lab,
                                                                     self.input_x_com: self.test_com,
                                                                     self.init_hiddenstate: init_hidden_state})
        """
        self.test_att_score = self.sess.run([self.score_attention, self.input_importance],
                                            feed_dict={self.input_x_vital: test_data,
                                            self.input_demo_:self.test_demo,
                                            self.input_x_lab:self.test_data_lab,
                                            self.input_x_com:self.test_com,
                                            self.init_hiddenstate:init_hidden_state})
        """
        self.correct = 0
        self.tp_test = 0
        self.fp_test = 0
        self.fn_test = 0
        self.tp_correct = 0
        self.tp_neg = 0
        """
        for i in range(test_length):
            if self.test_logit[i,1] == 1:
                self.tp_correct += 1
            if self.test_logit[i,1] == 1 and self.logit_out[i,1] > self.threshold:
                print("im here")
                self.correct += 1
                self.tp_test += 1
                print(self.tp_test)
            if self.test_logit[i,1] == 0:
                self.tp_neg += 1
            if self.test_logit[i,1] == 1 and self.logit_out[i,1] < self.threshold:
                self.fn_test += 1
            if self.test_logit[i,1] == 0 and self.logit_out[i,1] > self.threshold:
                self.fp_test += 1
            if self.test_logit[i,1] == 0 and self.logit_out[i,1] < self.threshold:
                self.correct += 1
        """
        for i in range(test_length):
            if self.test_logit[i, 0] == 1:
                self.tp_correct += 1
            if self.test_logit[i, 0] == 1 and self.logit_out[i, 0] > self.threshold:
                self.correct += 1
                self.tp_test += 1
            if self.test_logit[i, 0] == 0:
                self.tp_neg += 1
            if self.test_logit[i, 0] == 1 and self.logit_out[i, 0] < self.threshold:
                self.fn_test += 1
            if self.test_logit[i, 0] == 0 and self.logit_out[i, 0] > self.threshold:
                self.fp_test += 1
            if self.test_logit[i, 0] == 0 and self.logit_out[i, 0] < self.threshold:
                self.correct += 1

        """
        self.tp_test = 0
        self.fp_test = 0
        self.fn_test = 0
        for i in range(test_length):
            if self.test_logit[i,1] == 1 and self.logit_out[i,1] > self.threshold:
                self.tp_test += 1
            if self.test_logit[i,1] == 1 and self.logit_out[i,1] < self.threshold:
                self.fn_test += 1
            if self.test_logit[i,1] == 0 and self.logit_out[i,1] > self.threshold:
                self.fp_test += 1
        """
        self.precision_test = np.float(self.tp_test) / (self.tp_test + self.fp_test)
        self.recall_test = np.float(self.tp_test) / (self.tp_test + self.fn_test)

        self.f1_test = 2 * (self.precision_test * self.recall_test) / (self.precision_test + self.recall_test)

        self.acc = np.float(self.correct) / test_length

        threshold = 0.0
        self.resolution = 0.01
        tp_test = 0
        fp_test = 0
        self.tp_total = []
        self.fp_total = []
        self.precision_total = []
        self.recall_total = []
        while (threshold < 1.01):
            tp_test = 0
            fp_test = 0
            fn_test = 0
            precision_test = 0
            for i in range(test_length):
                if self.test_logit[i, 0] == 1 and self.logit_out[i, 0] > threshold:
                    tp_test += 1
                if self.test_logit[i, 0] == 0 and self.logit_out[i, 0] > threshold:
                    fp_test += 1
                if self.test_logit[i, 0] == 1 and self.logit_out[i, 0] < threshold:
                    fn_test += 1
            self.check_fp_test = fp_test
            print(self.check_fp_test)
            self.check_tp_test = tp_test
            print(self.check_tp_test)
            if (tp_test + fp_test) == 0:
                precision_test = 1
            else:
                precision_test = np.float(tp_test) / (tp_test + fp_test)
            recall_test = np.float(tp_test) / (tp_test + fn_test)
            tp_rate = tp_test / self.tp_correct
            fp_rate = fp_test / self.tp_neg
            self.tp_total.append(tp_rate)
            self.fp_total.append(fp_rate)
            self.precision_total.append(precision_test)
            self.recall_total.append(recall_test)
            threshold += self.resolution

    def cal_auc(self):
        self.area = 0
        self.tp_total.sort()
        self.fp_total.sort()
        for i in range(len(self.tp_total) - 1):
            x = self.fp_total[i + 1] - self.fp_total[i]
            y = (self.tp_total[i + 1] + self.tp_total[i]) / 2
            self.area += x * y
