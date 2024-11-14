extensions = {
    "jpeg":"Images",
    "jpg":"Images",
    "png":"Images",
    "gif":"Images",
    "webp":"Images",
    "svg":"Images",

    "mp4":"Vidoes",
    "avi":"Vidoes",
    "webm":"Vidoes",

    "mp3":"Music",
    "aac":"Music",
    "wav":"Music",
    "ogg":"Music",

    "pdf":"Pdf",

    "zip":"Compressed",
    "rar":"Compressed",

    "xls":"Excel",
    "xlsx":"Excel",
}

import os
import shutil

try:
    path = input("Enter path : ")
    files = os.listdir(path)

    print(files)

    for file in files:
        filename,extension=os.path.splitext(file)
        extension = extension[1:]

        folder = extensions[extension]
        
        print(folder)

        if os.path.exists(path+"/"+folder):
            shutil.move(path+"/"+file,path+"/"+folder+"/"+file)
        else:
            os.makedirs(path+"/"+folder)
            shutil.move(path+"/"+file,path+"/"+folder+"/"+file)

    print("Your files are organizied !")

except Exception as e:
    print(e)