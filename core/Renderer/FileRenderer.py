import sys
sys.path.append('../../')
from core.CodeCable.Phase_template import *


def Fetch_dependency(dep , dict = CODEBASE):
    dependency = []
    for i in dict[dep]:
            dependency.append(dict[dep][i]['code'])
    return dependency

###################################################
# This is Temporary fix of the solution
# In the future there will be need of re-visit this module
# MODIFICATIONS NEEDED :
# - Parameters
# - Search Schema
# - file handling
# ################################################ 

def Renderer(filename,extention, filetype):
    dep = Fetch_dependency(filetype)
    file = filename + extention
    with open(file,'w') as virtualcoder:
        #for i in dep:
        virtualcoder.writelines(dep)
    #
# To test the file ..... Uncomment it
# Renderer('Test','.py','HelloWorld')        


