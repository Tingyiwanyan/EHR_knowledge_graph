import os
import json
import numpy as np
import random

class kg_process_data():
    """
    divide into train and test data set
    """
    def __init__(self,kg):
        self.train_percent = 0.8
        self.test_percent = 0.2
        self.kg = kg
        self.train_patient = []
        self.test_patient = []
        self.test_patient = []
        self.train_patient_whole = []
        self.test_patient_whole = []
        self.train_mortality = []
        self.train_mortality_whole = []
        self.train_validate_mortality_whole = []
        self.test_mortality = []

    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data)
        self.train_num = np.int(np.floor(self.data_patient_num * self.train_percent))
        for i in self.kg.total_data[0:self.train_num]:
            self.train_patient.append(i)
        test_whole = [i for i in self.kg.total_data if i not in self.train_patient]
        for i in test_whole:
            self.test_patient.append(i)
    """
    """
    Prepare death data, 10 cross validation
    """

    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_mortality)
        #self.train_num = np.int(np.floor(self.data_patient_num*self.train_percent))
        self.test_num = np.int(np.floor(self.data_patient_num*self.test_percent))
        for i in self.kg.total_data_mortality[0 * self.test_num:(0 + 1) * self.test_num]:
            self.test_mortality.append(i)
        self.train_mortality = [i for i in self.kg.total_data_mortality if i not in self.test_mortality]

        self.data_patient_num = len(self.train_mortality)
        # self.train_num = np.int(np.floor(self.data_patient_num*self.train_percent))
        self.test_num = np.int(np.floor(self.data_patient_num * 0.2))
        for j in range(5):
            for i in self.train_mortality[j*self.test_num:(j+1)*self.test_num]:
                self.test_patient.append(i)
            self.train_patient = [i for i in self.kg.total_data_mortality if i not in self.test_patient]
            self.train_mortality_whole.append(self.train_patient)
            self.train_validate_mortality_whole.append(self.test_patient)
            self.test_patient = []




    """
    Prepare intubation data, 10 cross validation
    """
    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_intubation)
        self.test_num = np.int(np.floor(self.data_patient_num * self.test_percent))
        for j in range(5):
            for i in self.kg.total_data_intubation[j * self.test_num:(j + 1) * self.test_num]:
                self.test_patient.append(i)
            self.train_patient = [i for i in self.kg.total_data_intubation if i not in self.test_patient]
            self.train_patient_whole.append(self.train_patient)
            self.test_patient_whole.append(self.test_patient)
            self.test_patient = []
    """


    """
    prepare icu data, 10 cross validation
    """
    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_icu)
        self.test_num = np.int(np.floor(self.data_patient_num * self.test_percent))
        self.train_duplicate = []
        for j in range(5):
            for i in self.kg.total_data_mortality[j * self.test_num:(j + 1) * self.test_num]:
                self.test_patient.append(i)
            self.train_patient = [i for i in self.kg.total_data_mortality if i not in self.test_patient]
            for k in self.train_patient:
                if self.kg.dic_patient[k]['death_flag'] == 1:
                    self.train_duplicate.append(k)
            self.train_patient += self.train_duplicate
            random.shuffle(self.train_patient)
            self.train_patient_whole.append(self.train_patient)
            self.test_patient_whole.append(self.test_patient)
            self.test_patient = []
            self.train_duplicate = []
    """



