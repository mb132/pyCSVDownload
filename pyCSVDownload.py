import csv,os, time
from urllib import request

filename = "list.csv"
dir_path = os.getcwd()
dlpath = "F:\pyTestDL\RipTest"
debug = True
firstrun = False

# Tonga | Barcode | Packshot | Photo 1 | Photo 2 | Photo 3
#   0   |    1    |    2     |   3     |    4    |    5


# Open file
with open(filename, newline="") as csvfile:

    reader = csv.DictReader(csvfile, delimiter=";")

    piccount = 0 #Number of downloaded Images
    linecount = 1 #Number ob Processed Lines

    if debug:
        print("Opened", filename, "as", reader, end=" ")
        print("Analysing...")

    totallines = len(open(filename).readlines())

    if debug: print("Done!")

    for row in reader:
        os.system("cls")
        if firstrun: print("Processed",linecount,"of",totallines - 1," Lines and downloaded",piccount,"pictures.")
        print("Processing Line:", linecount)

        packshoturl = ""
        picture1 = ""
        picture2 = ""
        picture3 = ""

        tongaID = row["Tonga"]

        if row["Packshot"] != "":
            packshoturl = row['Packshot']
            if debug: print("   Downloading: Packshot |", row['Packshot'])
            fullfilename = os.path.join(dlpath, (tongaID) + "_packshot.jpg")
            request.urlretrieve(row['Packshot'], fullfilename)

            piccount += 1

        if row["Photo 1"] != "":
            picture1 = row['Photo 1']
            if debug: print("   Downloading: Photo 1 |", row['Photo 1'])
            fullfilename = os.path.join(dlpath, (tongaID) + "_1.jpg")
            request.urlretrieve(row['Photo 1'], fullfilename)

            piccount += 1

        if row["Photo 2"] != "":
            picture2 = row['Photo 2']
            if debug: print("   Downloading: Photo 2 |", row['Photo 2'])
            fullfilename = os.path.join(dlpath, (tongaID) + "_2.jpg")
            request.urlretrieve(row['Photo 2'], fullfilename)

            piccount += 1

        if row["Photo 3"] != "":
            picture3 = row['Photo 3']
            if debug: print("   Downloading: Photo 3 |", row['Photo 3'])
            fullfilename = os.path.join(dlpath, (tongaID) + "_3.jpg")
            request.urlretrieve(row['Photo 3'], fullfilename)

            piccount += 1

        print("Done!")
        print()
        firstrun = True
        linecount += 1