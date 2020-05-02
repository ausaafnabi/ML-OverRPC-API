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
def Renderer(filelocation, filename, filetype):
    Renderer.dep = Fetch_dependency(filetype)
    Renderer.file = filelocation + filename

    with open(Renderer.file,'w') as virtualcoder:
        virtualcoder.writelines(Renderer.dep)
    #
    #
# To test the file ..... Uncomment it
# Renderer('Test','.py',"HelloWorld")
