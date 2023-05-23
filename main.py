from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil
import os

mypath = str(Path(__file__).absolute())
mypath = mypath[:-7]

dokumen = mypath + "Dokumen"
video = mypath + "Video"
audio = mypath + "Audio"
image = mypath + "Image"
other = mypath + "Other"
archive = mypath + "Archive"
app = mypath + "App"

isExist = os.path.exists(app)
if not isExist:
    os.makedirs(app)

isExist = os.path.exists(dokumen)
if not isExist:
    os.makedirs(dokumen)

isExist = os.path.exists(video)
if not isExist:
    os.makedirs(video)

isExist = os.path.exists(image)
if not isExist:
    os.makedirs(image)

isExist = os.path.exists(other)
if not isExist:
    os.makedirs(other)

isExist = os.path.exists(audio)
if not isExist:
    os.makedirs(audio)

isExist = os.path.exists(archive)
if not isExist:
    os.makedirs(archive)


onlyfiles = [f for f in listdir(mypath) if isfile(
    join(mypath, f))]

dok4 = ['docx', 'vsdx', 'html', 'xlsx', 'pptx', 'DOCX']
dok3 = ['pdf', 'xls', 'txt', 'odt', 'doc',
        'xml', 'csv', 'DOC', 'PDF', 'ppt', 'PPT']
vid4 = ['mpeg', 'aiff']
vid3 = ['mp4', '3gp', 'mkv', 'avi', 'mov', 'wmv', 'dat']
ima4 = ['jpeg', 'webp', 'jfif', 'tiff']
ima3 = ['gif', 'jpg', 'jpe', 'bmp', 'dip', 'png', 'ico', 'tif', 'wmf', 'fig']
aud4 = ['flac']
aud3 = ['mp3', 'ogg', 'wav', 'wma', 'm4a', 'amr', 'mp2']
arc3 = ['zip', 'rar', 'iso']
app3 = ['exe']

for filename in onlyfiles:
    if ((filename[-4:] in dok4) or (filename[-3:] in dok3)):
        print(filename)
        shutil.move(mypath+filename, dokumen)
    elif ((filename[-4:] in vid4) or (filename[-3:] in vid3)):
        print(filename)
        shutil.move(mypath+filename, video)
    elif ((filename[-4:] in aud4) or (filename[-3:] in aud3)):
        print(filename)
        shutil.move(mypath+filename, audio)
    elif ((filename[-4:] in ima4) or (filename[-3:] in ima3)):
        print(filename)
        shutil.move(mypath+filename, image)
    elif ((filename[-3:] in arc3)):
        print(filename)
        shutil.move(mypath+filename, archive)
    elif ((filename[-3:] in app3)):
        print(filename)
        shutil.move(mypath+filename, app)
    elif ((filename[-7:] == ('main.py'))):
        print(filename)
    else:
        print(filename)
        shutil.move(mypath+filename, other)
