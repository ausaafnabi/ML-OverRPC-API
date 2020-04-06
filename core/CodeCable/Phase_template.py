import sys
sys.path.append('../../')
from core.CodeCable.Code import *

Initializer = {
    "Usage" : "To initialize the data",
     "code" : "#A comment of Approval",
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
  },
  "HelloWorld" : {
      "Function" : HelloFunction,
      "Function Call": HelloCall, 
  }
} 

