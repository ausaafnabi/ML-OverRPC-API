from string import Template

HelloWorld = """#importing Hello World
def HelloWorld():
    print('Hello')
"""
###########################################
###             Imports                 ###
###########################################
MLPre = """#Added Pre-requisite imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# add more imports here if you need for preprocessing

"""
MLKeras = """#Adding Keras Deep learning modules
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
"""
MLTensorflow = """#Adding tensorflow imports
import tensorflow as tf
"""

####################################################
####          keras sequential models            ###
####################################################
Sequential = """
def MLPModel(xtrain , ytrain , hiddenlayer = 60,
             activation1='relu' , activation2 = 'softmax' , inp_dim =20,
             lossmethod = 'categorical_crossentropy'):
    
    model = Sequential()
    # Dense(hiddenlayer) is a fully-connected layer with "hiddenlayer" hidden units.
    # in the first layer, you must specify the expected input data shape:
    # here, inp_dim = dimensional vectors.
    model.add(Dense(64, activation=activation1, input_dim=inp_dim))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation=activation1))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation=activation2))
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss=lossmethod,
                  optimizer=sgd,
                  metrics=['accuracy'])
    model.fit(xtrain, ytrain,
              epochs=20,
              batch_size=128)
"""
