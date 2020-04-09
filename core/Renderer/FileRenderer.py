import sys
sys.path.append('../../')
from string import Template
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
strfile=[]
def Renderer(filename,extention, filetype):
   # global strfile
    dep = Fetch_dependency(filetype)
    file = filename + extention
    with open(file,'w') as virtualcoder:
    #    for i in range(0,len(dep),2):
            strfile.append(dep[0].substitute())
            """dep[0]instead of dep[i]
            because inside list there would be only 2 elements template location and template name"""
            virtualcoder.writelines(dep[0].substitute())
    #
# To test the file ..... Uncomment it
Renderer('Test','.py',"HelloWorld")
