from variables import (doc_types, img_types, software_types)
import os
import shutil

def doc():
    for i in os.listdir():
        if i.endswith(doc_types):
            print (i)
            shutil.move(i, r"C:\Users\sarar\Desktop\trt\Documentos\doc")

def img():
    for i in os.listdir():
        if i.endswith(img_types):
            print(i)
            shutil.move(i, r"C:\Users\sarar\Desktop\trt\Documentos\Img")

def soft():
    for i in os.listdir():
        if i.endswith(software_types):
            print(i)
            shutil.move(i, r"C:\Users\sarar\Desktop\trt\Documentos\Software")

