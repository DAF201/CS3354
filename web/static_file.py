from glob import glob
from os.path import basename
from os import name as os_name

if os_name == 'nt':
    STATIC_FILES_PATH = r'.\\static_files\\'
else:
    STATIC_FILES_PATH = r'./static_files/'
    
STATIC_FILES = {}

# load all to memeory to speed up
for file_name in glob(STATIC_FILES_PATH+'/*.*'):
    try:
        with open(file_name, 'r')as file:
            STATIC_FILES[basename(file_name)] = file.read()
    except:
        with open(file_name, 'rb')as file:
            STATIC_FILES[basename(file_name)] = file.read()
