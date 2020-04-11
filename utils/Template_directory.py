#from TemplatingTools import *

Experiment=[
    'Datasets',
    'Model'
]
Production=[
    'templates',
    'model',
    'util',
    'tests',
    'db'
]

File = {
    "Experiment" : {
        "Datasets" : {
            "file" :{ "filename" : '#',
            "dependency" : "Pipelines" },  
         },
        "Model" : {
            "File1" :{ 
                "filename" : "datapipeline.py",
                "dependency" : "Pipelines"
            },
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },
        },
    },
    
    "Production" :{
        "templates" :{
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },
        },
        "model" : {
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },
        },
        "util" : {    
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },
        },
        "tests" : {
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },        
        },
        "db" : {
            "File2" : { 
                "filename" : "Model.py",
                "dependency" : "HelloWorld",  
            },    
        },
    },
}