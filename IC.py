#coding:utf-8
import os
import os.path
import Image
import platform

strPlatform = platform.platform()
if "Windows" in strPlatform:
    command = 'pngquant.exe'
elif "Darwin" in strPlatform:
    command = './pngquant'
else:
    print "System not supported"
    exit()
outputFormat = '.png'
commandParam = '**.png --ext .png --force --quality 65 --speed 1'

currentPath = os.getcwd()
fileList = os.listdir(currentPath)
for file in fileList:
    if(os.path.isdir(file)):
        targetFiles = os.listdir(file)
        outputDir = file + '/output/'
        if not os.path.isdir(outputDir):
            os.makedirs(outputDir)
        for targetFile in targetFiles:
            try:
                img = Image.open(file + '/' + targetFile)
                w, h = img.size
                out = img.resize((w//2, h//2), Image.ANTIALIAS)
                out.save(outputDir + targetFile[0:targetFile.rfind('.')] + outputFormat)
            except IOError:
                print targetFile + ' is not a image file'
            except  Exception as e:
                print e
        os.system(command + ' ' + outputDir + commandParam)
print 'Done'