import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main_function():
    archive_name = os.path.expanduser(os.path.join('.', 'myarchive'))
    root_dir = os.path.expanduser(os.path.join('.', 'directory_tobe_archived'))
    if not os.path.isdir(root_dir):
        print('Not a valid directory for archive')
    make_archive(archive_name, 'zip', root_dir)
    
if __name__=='__main__':
    print(__doc__)    
    main_function()