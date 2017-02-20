#import exifread
import os

# Open image file for reading (binary mode)
path_name = '/Users/awhite/Desktop/Baited'
f = open(path_name, 'rb')
desiredTag = 'EXIF DateTimeOriginal'
# Return Exif tags
#tags = exifread.process_file(f)
rootdir = '/Users/awhite/Desktop/Baited'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
            print(file)
            #f=open(file,'r')
            #lines=f.readlines()
            #f.close()
            #f=open(file,'w')
            #for line in lines:
                #newline = "No you are not"
                #f.write(newline)
            #f.close()