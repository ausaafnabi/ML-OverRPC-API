#!/usr/bin/env python3
import os
import re
import click
from PyInquirer import (Token,ValidationError,Validator,print_json,prompt,style_from_dict)
import six
from pyfiglet import figlet_format
from utils.CreateTemplate import *
from core.Renderer.FileRenderer import *

try:
     import colorama
     colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',
    Token.Seperator: '#cc5454',
    Token.Selected: '#0abf5b',
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})

def log(string,color,font="slant",figlet=False):
    if colored:
        if figlet:
            six.print_(colored(figlet_format(string,font=font),color))
        else:
            six.print_(colored(string,color))
    else:
        six.print_(string)

class EmptyValidator(Validator):
    def validate(self,value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position = len(value.text))

def getContentType(answer, conttype):
    return answer.get("content_type").lower() == conttype.lower()

def askProjectInfo():
    questions = [
        {
            'type' : 'input',
            'name' : 'ProjectName',
            'message' : 'PROJECTNAME',
            'validate' : EmptyValidator
        },
    ]
    answers = prompt(questions,style=style)
    return answers

def askMLModelInformation():
    questions = [
        {
            'type' : 'input',
            'name' : 'Dataset',
            'message' : 'DATASET',
            'validate' : EmptyValidator
        },
        {
            'type' : 'input',
            'name' : 'Epoches',
            'message' : 'EPOCHES',
            'validate' : EmptyValidator
        },
        {
            'type' : 'list',
            'name' : 'Classifier',
            'message' : 'CLASSIFIER',
            'choices' : ['Text_Recognizer','Speech_Recognizer','Image_Recognizer'],
            'filter' : lambda val :val.lower()
            #'validate' : EmptyValidator
        },
        {
            'type' : 'confirm',
            'name' : 'confirm_content',
            'message' : 'Do You Want to Send the Request to Train this model (Y/n): ',
            'validate' : EmptyValidator
        },
    ]
    answers = prompt(questions,style=style)
    return answers

@click.command()
def main():
    log("Over-RPC",color="red",figlet=True)
    log("Set-Up The Chain Call Procedure for ML models","green")
    ProjInfo = askProjectInfo()
    #MLInfo = askMLModelInformation()
    # To test the file Created from root uncomment it
    #Renderer('Hello','.py','HelloWorld')
   # CreateDirectory(ProjInfo.get('ProjectName'))
    dirmsg = 'Creating ' + ProjInfo.get('ProjectName') + '  Directory in ' + GetCurrentDirectory()
    log(dirmsg ,color="green")

    Generator(ProjInfo.get('ProjectName'))
if __name__ == '__main__':
    main()
