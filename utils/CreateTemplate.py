import os
from utils.Template_directory import *
from utils.utilities import *
import sys
sys.path.append('../')
from core.Renderer.FileRenderer import Renderer
layer1 = [Experiment,Production]
layer1_names = ['Experiment','Production']
Files = File

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
            filePath = dirName + '/'
            FilesGenerator(filePath,str(layer1[i][j]),str(layer1_names[i]))
            print("Directory ",dirName," Created")
    
def FilesGenerator(file_location,foldername,layer_name,dict=Files):

    for i in dict[layer_name][foldername]:
        filename = dict[layer_name][foldername][i]['filename']
        # print(layer_name + foldername + i)
        dependency = dict[layer_name][foldername][i]['dependency']
        print("CREATING: " + filename + "in" + file_location )
        Renderer(file_location,filename,dependency)
        
    