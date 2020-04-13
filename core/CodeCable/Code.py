from string import Template

HelloWorld = """#importing Hello World
def HelloWorld():
    print('Hello')
"""
#----------------------------------------------------------------------------------------------------------------
#================================          Experimentation Codebase         =====================================
#----------------------------------------------------------------------------------------------------------------

###########################################
###             Imports                 ###
###########################################
MLPre = """#Added Pre-requisite imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# add more imports here if you need.

"""
MLKeras = """#Adding Keras Deep learning modules. 
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam 
#Add more here :
"""
MLTensorflow = """#Adding tensorflow imports
import tensorflow as tf
"""
MLSklearn = """
import sklearn
import sklearn.preprocessing
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
###########################################
###           Visualizing               ###
###########################################

###########################################
###   Preprocessing/Feature-Extraction  ###
###########################################
#Have to rebuild the pipeline to build the keras models as well....Also have to implement the Hyperparameter using the grid search
Pipeline = """
#import model to build a pipeline for it...
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# A sample Pipeline prepared for you. Modify it according to your needs
model_pipeline = Pipeline(steps=[
  ("features", FeatureUnion([
    (
      "numerical_features",
      ColumnTransformer([
        (
          "numerical",
          Pipeline(steps=[(
            "impute_stage",
            SimpleImputer(missing_values=np.nan, strategy="median",)
          )]),
          ["feature_1"]
        )
      ])
    ), (
      "categorical_features",
      ColumnTransformer([
        (
          "country_encoding",
          Pipeline(steps=[
            ("ohe", OneHotEncoder(handle_unknown="ignore")),
            ("reduction", NMF(n_components=8)),
          ]),
          ["country"],
        ),
      ])
    ), (
      "text_features",
      ColumnTransformer([
        (
          "title_vec",
          Pipeline(steps=[
            ("tfidf", TfidfVectorizer()),
            ("reduction", NMF(n_components=50)),
          ]),
          "title"
        )
      ])
    )
  ])),
  ("classifiers", RandomForestClassifier())
])
#define train_data and train_labels
model_pipeline.fit(train_data, train_labels.values)
predictions = model_pipeline.predict(predict_data)
"""
###########################################
###             Tensorflow              ###
###########################################

#----------------------------------------------------------------------------------------------------------------
#================================            Production Codebase            =====================================
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#================================            ML-Over-API Codebase           =====================================
#----------------------------------------------------------------------------------------------------------------