__author__ = 'dstuckey'

import csv
import zipfile

#partd_filename = "/Users/dstuckey/Downloads/PartD_Prescriber_PUF_NPI_13.zip"

test_filename = "/Users/dstuckey/Downloads/Dir1.zip"

with open(test_filename) as testfile:
    thezip = zipfile.ZipFile(testfile)
    names = thezip.namelist()
    testfile = thezip.open(names[len(names)-1])
    print testfile.read()