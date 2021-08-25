#script will OCR all PDF files in current working directory.
#Requires ImageMagick and Tesseract to be installed in local machine and added to the path
#List of processed files will appear in log.txt. Any files that do not process correctly will be listed in error.txt.

import os

shutdown = input('Do you want to shutdown when OCR is complete? [Y/N]')
if shutdown == 'Y' or shutdown == 'y':
    print('System will shutdown when OCR is complete')

totalpdfs = 0
worked = 0


files = os.listdir() #get list of files from current directory
for pdffile in files:
    if pdffile.endswith('.pdf'): #if file is a PDF
        totalpdfs = totalpdfs + 1

print(totalpdfs, 'PDFs detected in directory')

for pdffile in files:

    try: 
        if pdffile.endswith('.pdf'): #if file is a PDF
            targetfile=pdffile+'.tiff'
            os.system('Magick -density 300 ' +(pdffile) +' -depth 8 -strip -background white -alpha off ' +(targetfile))#pre-process PDF into TIFF with ImageMagick
            os.system('tesseract ' +(targetfile) +' ' +(targetfile))#OCR tiff with Tesseract
            os.remove(targetfile)#delete the tiff as we have completed OCR and no longer need it (and tiffs are huge!)
            with open('log.txt', 'a') as f:
                print(pdffile, file=f)#add file name of process PDF to log file
            worked = worked + 1
            print ('Processed', worked, 'of', totalpdfs)
        
    except:
        with open ('error.txt', 'a') as f:
            print(pdffile, 'was not successfully processed', file=f)#if there is an error in the above steps, add name of affected file to error file


if shutdown == 'Y' or shutdown == 'y':
    os.system('shutdown /s') #when all files are OCR'd shutdown system
