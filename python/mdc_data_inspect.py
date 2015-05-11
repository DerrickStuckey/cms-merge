__author__ = 'dstuckey'

import csv
import zipfile

#partd_filename = "/Users/dstuckey/Downloads/PartD_Prescriber_PUF_NPI_13.zip"
partd_filename = "../../PartD_Prescriber_PUF_NPI_13.zip"

with open(partd_filename) as partdfile:
    thezip = zipfile.ZipFile(partdfile)
    # names = thezip.namelist()
    # for name in names:
    #     print name
    tabtxtfilename = "PartD_Prescriber_PUF_NPI_13/PartD_Prescriber_PUF_NPI_13.txt"
    # tabtxtfile = thezip.op

    with thezip.open(tabtxtfilename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        first = reader.next()
        #print(first)

        for key in first.keys():
            print key, " : ", first[key]