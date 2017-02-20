
import exifread
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def processFolder(directoryInput,directoryOutput,fileName,directoryInput2= "none"):
    # count the pictures per hour
    clearCounts()
    file_object = open("%s/%s.txt" % (directoryOutput, fileName), 'w')
    for filename in os.listdir(directoryInput):
        if filename.endswith('.JPG'):
            with open("%s/%s" % (directoryInput, filename), 'rb') as image:  # file path and name
                exif = exifread.process_file(image)
                # print(exif)
                dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                # rename files to a specific format
                # print(dt)
                # segment string dt into date and time
                day, dtime = dt.split(" ", 1)
                # print(dtime)
                # segment time into hour, minute, second
                hour, minute, second = dtime.split(":", 2)
                # print(hour)
                options[hour]()
                file_object.write('%s\t' % dt)

            continue
        else:
            continue
    file_object.close()
    hourarray1,sum1 = countImages()

    if directoryInput2 !=  "none":
        clearCounts()
        file_object = open("%s/%s.txt" % (directoryOutput, fileName+str(2)), 'w')
        for filename in os.listdir(directoryInput2):
            if filename.endswith('.JPG'):
                with open("%s/%s" % (directoryInput2, filename), 'rb') as image:  # file path and name
                    exif = exifread.process_file(image)
                    # print(exif)
                    dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                    # rename files to a specific format
                    # print(dt)
                    # segment string dt into date and time
                    day, dtime = dt.split(" ", 1)
                    # print(dtime)
                    # segment time into hour, minute, second
                    hour, minute, second = dtime.split(":", 2)
                    # print(hour)
                    options[hour]()
                    file_object.write('%s\t' % dt)

                continue
            else:
                continue
        file_object.close()
        hourarray2, sum2 = countImages()
        doubleHistogram(hourarray1, sum1, hourarray2, sum2)

    if desiredChart == "0":
        histogram(hourarray1,sum1)
    elif desiredChart == "2":
        barchart(hourarray1, sum1)

    clearCounts()
    file_object = open("%s/%s.txt" % (directoryOutput, fileName), 'w')
    for filename in os.listdir(directoryInput):
        if filename.endswith('.JPG'):
            with open("%s/%s" % (directoryInput, filename), 'rb') as image:  # file path and name
                exif = exifread.process_file(image)
                # print(exif)
                dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                # rename files to a specific format
                # print(dt)
                # segment string dt into date and time
                day, dtime = dt.split(" ", 1)
                # print(dtime)
                # segment time into hour, minute, second
                hour, minute, second = dtime.split(":", 2)
                # print(hour)
                options[hour]()
                file_object.write('%s\t' % dt)

            continue
        else:
            continue
    file_object.close()

def processDirectory(directoryInput,directoryOutput,fileName,directoryInput2= "none"):
    # count the pictures per hour
    clearCounts()
    file_object = open("%s/%s.txt" % (directoryOutput, fileName), 'w')
    for folder in os.listdir(directoryInput):
        #find way to enter check if folder then enter
        ndirect = directoryInput+"/"+folder
        if os.path.isdir(ndirect):
            print(ndirect)
            for filename in os.listdir(ndirect):
                if filename.endswith('.JPG'):
                    with open("%s/%s" % (ndirect, filename), 'rb') as image:  # file path and name
                        exif = exifread.process_file(image)
                        """if ndirect == "/Users/awhite/Desktop/Baited/PM_7":
                            print(exif)
                            print(filename)"""
                        dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                        # rename files to a specific format
                        # print(dt)
                        # segment string dt into date and time
                        day, dtime = dt.split(" ", 1)
                        # print(dtime)
                        # segment time into hour, minute, second
                        hour, minute, second = dtime.split(":", 2)
                        # print(hour)
                        options[hour]()
                        file_object.write('%s\t' % dt)

                    continue
                else:
                    continue
    file_object.close()
    hourarray1,sum1 = countImages()

    if directoryInput2 !=  "none":
        clearCounts()
        file_object = open("%s/%s.txt" % (directoryOutput, fileName+str(2)), 'w')
        for folder in os.listdir(directoryInput):
            # find way to enter check if folder then enter
            ndirect = directoryInput + "/" + folder
            if os.path.isdir(ndirect):
                for filename in os.listdir(ndirect):
                    if filename.endswith('.JPG'):
                        with open("%s/%s" % (ndirect, filename), 'rb') as image:  # file path and name
                            exif = exifread.process_file(image)
                            # print(exif)
                            dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                            # rename files to a specific format
                            # print(dt)
                            # segment string dt into date and time
                            day, dtime = dt.split(" ", 1)
                            # print(dtime)
                            # segment time into hour, minute, second
                            hour, minute, second = dtime.split(":", 2)
                            # print(hour)
                            options[hour]()
                            file_object.write('%s\t' % dt)

                        continue
                    else:
                        continue
        file_object.close()
        hourarray2, sum2 = countImages()
        doubleHistogram(hourarray1, sum1, hourarray2, sum2)

    if desiredChart == "0":
        histogram(hourarray1,sum1)
    elif desiredChart == "2":
        barchart(hourarray1, sum1)

    clearCounts()
    file_object = open("%s/%s.txt" % (directoryOutput, fileName), 'w')
    for filename in os.listdir(directoryInput):
        if filename.endswith('.JPG'):
            with open("%s/%s" % (directoryInput, filename), 'rb') as image:  # file path and name
                exif = exifread.process_file(image)
                # print(exif)
                dt = str(exif['EXIF DateTimeOriginal'])  # might be different
                # rename files to a specific format
                # print(dt)
                # segment string dt into date and time
                day, dtime = dt.split(" ", 1)
                # print(dtime)
                # segment time into hour, minute, second
                hour, minute, second = dtime.split(":", 2)
                # print(hour)
                options[hour]()
                file_object.write('%s\t' % dt)

            continue
        else:
            continue
    file_object.close()

#sums the total images and counts the images per hour and puts that into an array
def countImages():
    hourarray = []
    for i in range(24):
        if (i >= 10):
            hourcount = 'hour' + str(i) + 'count'
        else:
            hourcount = 'hour' + str(0) + str(i) + 'count'
        value = eval(hourcount) #casts hourcount the variable which has the actual no. of images taken
        hourarray.append(value)
    sum = 0
    for j in range(24):
        print("hour:", j, " count: ", hourarray[j])
        sum += hourarray[j]
    print("Total sightings:", sum)
    return hourarray,sum

def histogram(hourarray,sum):
    #pseudo histogram of the sightings
    normhourarray = []
    if sum != 0:
        for k in range(24):
            normhourarray.append(hourarray[k]/sum)
    else:
        return

    N = 24
    ind = np.arange(N)  # the x locations for the groups
    width = 1       # the width of the bars

    f=plt.figure(1)
    plt.bar(ind, normhourarray, width, color='r')
    plt.xlabel('Hour')
    plt.ylabel('Percentage of Sightings')
    plt.title('Percentage of Deer Sightings per Hour at Unbaited Sites:')
    plt.axis([0, 24, 0, .2])
    plt.xticks(np.arange(0, 24, 1.0))
    plt.grid(True)
    f.show()
    showfigure()

def doubleHistogram(hourarray1,sum1,hourarray2,sum2):
    #pseudo histogram of the sightings
    normhourarray1 = []
    normhourarray2 = []
    if sum1 != 0:
        if sum2 != 0:
            for k in range(24):
                normhourarray1.append(hourarray1[k]/sum1)
                normhourarray2.append(hourarray2[k]/sum2)
        else:
            return
    else:
        return

    N = 24
    ind = np.arange(N)  # the x locations for the groups
    width = 1       # the width of the bars

    f=plt.figure(1)
    plt.bar(ind, normhourarray1, width, color='r')
    plt.bar(ind, normhourarray2, width, color='b')
    plt.xlabel('Hour')
    plt.ylabel('Percentage of Sightings')
    plt.title('Percentage of Deer Sightings per Hour:')
    plt.axis([0, 24, 0, .2])
    plt.xticks(np.arange(0, 24, 1.0))
    plt.grid(True)
    f.show()
    showfigure()

def barchart():
    # barchart of sightings
    N = 24
    ind = np.arange(N)  # the x locations for the groups
    width = 1  # the width of the bars

    g = plt.figure(2)
    plt.bar(ind, hourarray, width, color='r')
    plt.xlabel('Hour')
    plt.ylabel('Sightings')
    plt.title('Barchart of Deer Sightings:')
    plt.axis([0, 24, 0, 60])
    plt.xticks(np.arange(0, 24, 1.0))
    plt.grid(True)
    g.show()
    showfigure()

def showfigure():
    input()

#case counting function definitions
def hour00():
    global hour00count
    hour00count+=1

def hour01():
    global hour01count
    hour01count+=1

def hour02():
    global hour02count
    hour02count+=1

def hour03():
    global hour03count
    hour03count+=1

def hour04():
    global hour04count
    hour04count+=1

def hour05():
    global hour05count
    hour05count+=1

def hour06():
    global hour06count
    hour06count+=1

def hour07():
    global hour07count
    hour07count+=1

def hour08():
    global hour08count
    hour08count+=1

def hour09():
    global hour09count
    hour09count+=1

def hour10():
    global hour10count
    hour10count+=1

def hour11():
    global hour11count
    hour11count+=1

def hour12():
    global hour12count
    hour12count+=1

def hour13():
    global hour13count
    hour13count+=1

def hour14():
    global hour14count
    hour14count+=1

def hour15():
    global hour15count
    hour15count+=1

def hour16():
    global hour16count
    hour16count+=1

def hour17():
    global hour17count
    hour17count+=1

def hour18():
    global hour18count
    hour18count+=1

def hour19():
    global hour19count
    hour19count+=1

def hour20():
    global hour20count
    hour20count+=1

def hour21():
    global hour21count
    hour21count+=1

def hour22():
    global hour22count
    hour22count+=1

def hour23():
    global hour23count
    hour23count+=1

#clean variables
def clearCountsArray():
    global hour00count
    global hour01count
    global hour02count
    global hour03count
    global hour04count
    global hour05count
    global hour06count
    global hour07count
    global hour08count
    global hour09count
    global hour10count
    global hour11count
    global hour12count
    global hour13count
    global hour14count
    global hour15count
    global hour16count
    global hour17count
    global hour18count
    global hour19count
    global hour20count
    global hour21count
    global hour22count
    global hour23count

    hour00count = 0
    hour01count = 0
    hour02count = 0
    hour03count = 0
    hour04count = 0
    hour05count = 0
    hour06count = 0
    hour07count = 0
    hour08count = 0
    hour09count = 0
    hour10count = 0
    hour11count = 0
    hour12count = 0
    hour13count = 0
    hour14count = 0
    hour15count = 0
    hour16count = 0
    hour17count = 0
    hour18count = 0
    hour19count = 0
    hour20count = 0
    hour21count = 0
    hour22count = 0
    hour23count = 0

#initialize counts
hour00count = 0
hour01count = 0
hour02count = 0
hour03count = 0
hour04count = 0
hour05count = 0
hour06count = 0
hour07count = 0
hour08count = 0
hour09count = 0
hour10count = 0
hour11count = 0
hour12count = 0
hour13count = 0
hour14count = 0
hour15count = 0
hour16count = 0
hour17count = 0
hour18count = 0
hour19count = 0
hour20count = 0
hour21count = 0
hour22count = 0
hour23count = 0

#dictionary of functions, which acts as a case switch
options = { '00' : hour00,
            '01' : hour01,
            '02' : hour02,
            '03' : hour03,
            '04' : hour04,
            '05' : hour05,
            '06' : hour06,
            '07' : hour07,
            '08' : hour08,
            '09' : hour09,
            '10' : hour10,
            '11' : hour11,
            '12' : hour12,
            '13' : hour13,
            '14' : hour14,
            '15' : hour15,
            '16' : hour16,
            '17' : hour17,
            '18' : hour18,
            '19' : hour19,
            '20' : hour20,
            '21' : hour21,
            '22' : hour22,
            '23' : hour23,
}

#interface
directOrFile =input("Enter '0' if you want to process a folder with images or '1' if you want to process a folder of folders containing images: ")
directoryInput = input("Example filepath '/Users/awhite/Desktop/Research/Silman_Lab_Fall_16/PM_12'\nEnter the file path of the folder of images you want to process: ")
directoryOutput = input("Enter the destination file path of the output file: ")
fileName = input("Enter the desired name for the output file: ")
desiredChart =input("Type a '0' for a histogram of the data, '1' for a comparative histogram or a '2' for a barchart:")



#do you want raw output?

#fix these if statements for correct directory
if directoryInput == "default":
    directoryInput = "/Users/awhite/Desktop/Research/Silman_Lab_Fall_16/PM_12"
    default1= "/Users/awhite/Desktop/Baited"

if directoryOutput == "default":
    directoryOutput = "/Users/awhite/Desktop"

if fileName == "default":
    fileName = "output"

#processes folder
if directOrFile == "0":
    if desiredChart == "1":
        directoryInput2 = input(
            "Example filepath '/Users/awhite/Desktop/Research/Silman_Lab_Fall_16/PM_12'\nEnter the file path of the second folder of images you want to process: ")
        if directoryInput2 == "default":
            directoryInput2 = "/Users/awhite/Desktop/Unbaited/PM_11"
        processFolder(directoryInput, directoryOutput, fileName, directoryInput2)
    elif desiredChart == "0":
        processFolder(directoryInput, directoryOutput, fileName)  # add how you want to process file
    elif desiredChart == "2":
        processFolder(directoryInput, directoryOutput, fileName)  # add how you want to process file
    elif desiredChart == "3":
        processFolder2("/Users/awhite/Desktop/Baited", directoryOutput, fileName)

#process folder of folders
elif directOrFile == "1":
    if directoryInput == "/Users/awhite/Desktop/Research/Silman_Lab_Fall_16/PM_12":
        directoryInput = "/Users/awhite/Desktop/Unbaited"
    if desiredChart == "1":
        directoryInput2 = input(
            "Example filepath '/Users/awhite/Desktop/Research/Silman_Lab_Fall_16/PM_12'\nEnter the file path of the second folder of images you want to process: ")
        if directoryInput2 == "default":
            directoryInput2 = "/Users/awhite/Desktop/Baited"
        processDirectory(directoryInput, directoryOutput, fileName, directoryInput2)
    elif desiredChart == "0":
        processDirectory(directoryInput, directoryOutput, fileName)  # add how you want to process file
    elif desiredChart == "2":
        processDirectory(directoryInput, directoryOutput, fileName)  # add how you want to process file


