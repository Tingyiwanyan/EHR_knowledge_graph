import os
import json
import numpy as np
import random

class kg_process_data():
    """
    divide into train and test data set
    """
    def __init__(self,kg):
        self.train_percent = 0.9
        self.test_percent = 0.1
        self.kg = kg
        self.train_patient = []
        self.test_patient = []
        self.test_patient = []
        self.train_patient_whole = []
        self.test_patient_whole = []
    """
    Prepare death data, 10 cross validation
    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_mortality)
        #self.train_num = np.int(np.floor(self.data_patient_num*self.train_percent))
        self.test_num = np.int(np.floor(self.data_patient_num*self.test_percent))
        for j in range(10):
            for i in self.kg.total_data_mortality[j*self.test_num:(j+1)*self.train_num]:
                self.test_patient.append(i)
            self.train_patient = [i for i in self.kg.total_data_mortality if i not in self.test_patient]
            self.train_patient_whole.append(self.train_patient)
            self.test_patient_whole.append(self.test_patient)



    """
    Prepare intubation data, 10 cross validation
    """
    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_intubation)
        self.train_num = np.int(np.floor(self.data_patient_num*self.train_percent))
        for i in self.kg.total_data[0:self.train_num]:
            self.train_patient.append(i)
        test_whole = [i for i in self.kg.total_data_mortality if i not in self.train_patient]

        for i in test_whole:
            self.test_patient.append(i)
    """


    """
    prepare icu data, 10 cross validation
    """
    """
    def separate_train_test(self):
        self.data_patient_num = len(self.kg.total_data_icu)
        self.train_num = np.int(np.floor(self.data_patient_num*self.train_percent))
        for i in self.kg.total_data[0:self.train_num]:
            self.train_patient.append(i)
        test_whole = [i for i in self.kg.total_data_mortality if i not in self.train_patient]

        for i in test_whole:
            self.test_patient.append(i)
    """


