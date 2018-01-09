from urllib import request
import csv
import os
import concurrent.futures.process
import concurrent.futures.thread

# Tonga | Barcode | Packshot | Photo 1 | Photo 2 | Photo 3
#   0   |    1    |    2     |   3     |    4    |    5

debug = False
filename = "list.csv"


def download(url, path, name, type):

    fullfilename = os.path.join(path, name + type)

    #if debug: print("Downloading:", url, "to", fullfilename)

    request.urlretrieve(url, fullfilename)

    if debug: print(fullfilename,"done")

    return True


def analysecontend(file):
    count = 0
    with open(file, newline="") as csvfile:
        tempreader = csv.DictReader(csvfile, delimiter=";")
        for row in tempreader:
            if row["Packshot"] != "":
                count += 1

            if row["Photo 1"] != "":
                count += 1

            if row["Photo 2"] != "":
                count += 1

            if row["Photo 3"] != "":
                count += 1
    return count


RowsToProcess = analysecontend(filename)
ProcessedRows = 0

print("Downloading", RowsToProcess,"Files")

with open(filename, newline="") as csvfile:

    reader = csv.DictReader(csvfile, delimiter=";")

    with concurrent.futures.ThreadPoolExecutor(max_workers=None,) as executor:

        for row in reader:

            if row["Packshot"] != "":
                executor.submit(download, row["Packshot"], "F:\pyTestDL\AsyncRipTest", row["Tonga"] + "_packshot", ".jpg")

            if row["Photo 1"] != "":
                executor.submit(download, row["Photo 1"], "F:\pyTestDL\AsyncRipTest", row["Tonga"] + "_1", ".jpg")

            if row["Photo 2"] != "":
                executor.submit(download, row["Photo 2"], "F:\pyTestDL\AsyncRipTest", row["Tonga"] + "_2", ".jpg")

            if row["Photo 3"] != "":
                executor.submit(download, row["Photo 3"], "F:\pyTestDL\AsyncRipTest", row["Tonga"] + "_3", ".jpg")
            print(ProcessedRows)
print("Done")