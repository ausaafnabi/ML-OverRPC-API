from os import scandir

def Fetch_directories(directory_location):
    # List all subdirectories using scandir()
    DirectoryList = []
    basepath = directory_location
    with scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                DirectoryList.append(entry.name)
    return DirectoryList

###################################################
###             Adding File Attributes          ###
###################################################
from datetime import datetime
import glob
from string import Template

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_latest_modified(directory_location):
    dir_entries = scandir(directory_location)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(str(entry.name)+"Last Modified: "+str(convert_date(info.st_mtime)))

# PATTERN MATCHING :
#Can use the glob pattern to find file in the pattern
# eg : '*[0-9]*.py', '*.py' etc
import glob

def Pattern_Match(pattern):
    for name in glob.glob(pattern):
        print(name)
