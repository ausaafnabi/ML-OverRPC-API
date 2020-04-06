import os
from utils.Template_directory import *

layer1 = [Experiment,Production]
layer1_names = ['Experiment','Production']

def GetCurrentDirectory():
    currentDirectory = os.getcwd()
    return currentDirectory

def CreateDirectory(directory):
    try:
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def Generator(root_dir):
    for i in range(0,len(layer1)):
        layerName = str(root_dir)+'/'+str(layer1_names[i])
        CreateDirectory(layerName)
        for j in range(0,len(layer1[i])):
            dirName = layerName +'/'+str(layer1[i][j])

            CreateDirectory(dirName)
            print("Directory ",dirName," Created")
