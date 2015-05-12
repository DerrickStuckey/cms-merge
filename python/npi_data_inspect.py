__author__ = 'dstuckey'

import csv
import zipfile

npi_filename = "../../NPPES_Data_Dissemination_April_2015.zip"

with open(npi_filename) as zipped_file:
    thezip = zipfile.ZipFile(zipped_file)
    names = thezip.namelist()
    for name in names:
        print name

    csvfilename = "npidata_20050523-20150412.csv"
    headerfilename = "npidata_20050523-20150412FileHeader.csv"

    with thezip.open(csvfilename) as csvfile:
        reader = csv.DictReader(csvfile)

        first = reader.next()
        print "First Record Fields and Values:"
        for key in first.keys():
            print key, " : ", first[key]

    #
    #     for i in range(0,5,1):
    #         record = reader.next()
    #         print "Provider ID stuff:"
    #         for key in record.keys():
    #             if "PROVIDER" in key:
    #                 print key, " : ", record[key]
