import sys
sys.path.append('../../')
from core.CodeCable.Code import *

Initializer = {
    "Usage" : "To initialize the data",
     "code" : "#A comment of Approval",
     "discription" : "some discription"
}
Imports = {
    "Usage" : "Required Imports",
     "code" : MLPre+MLKeras,
     "discription" : "some discription"
}
Plumber = {
    "Usage" : "Required Imports",
     "code" : Pipeline,
     "discription" : "some discription"
}
Sequential = {
    "Usage" : "Basic keras model ",
     "code" : Sequential,
     "discription" : "some discription"
}
HelloFunction = {
    "Usage" : "To test the code",
     "code" : HelloWorld,
     "discription" : "some discription"
}
HelloCall = {
    "Usage" : "To initialize the data",
     "code" : "HelloWorld()",
     "discription" : "some discription"
}
CODEBASE = {
  "Pipelines" : {
    "Initializer" : Initializer,
    "Imports" : Imports,
    "Plumber" : Plumber,
  },
  "KerasModels" : {
    "Initializer" : Initializer,
    "Imports" : Imports,
    "Sequential" : Sequential,
  },
  "HelloWorld" : {
      "Function" : HelloFunction,
      "Function Call": HelloCall,
  }
}
