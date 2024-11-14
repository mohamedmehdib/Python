import os
import shutil
import datetime

source_dir = "C:/Users/medme/Pictures/aaaa"
destination_dir = "C:/Users/medme/Desktop/9raya"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f'Folder copied to: {dest}')
    except:
        print(f'Folder already exists in: {dest}')

copy_folder_to_directory(source_dir, destination_dir)