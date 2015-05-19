__author__ = 'dstuckey'

import csv
import zipfile

#partd_filename = "/Users/dstuckey/Downloads/PartD_Prescriber_PUF_NPI_13.zip"
partd_filename = "../../PartD_Prescriber_PUF_NPI_DRUG_13.zip"

with open(partd_filename) as partdfile:
    thezip = zipfile.ZipFile(partdfile)
    names = thezip.namelist()
    for name in names:
        print name
    tabtxtfilename = "PartD_Prescriber_PUF_NPI_DRUG_13.txt"
    # tabtxtfile = thezip.op

    with thezip.open(tabtxtfilename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        first = reader.next()
        #print(first)

        # for key in first.keys():
        #     print key, " : ", first[key]

        for i in range(0,10,1):
            record = reader.next()
            print "\n\nRecord ", str(i)
            # print "Provider ID stuff:"
            for key in record.keys():
                # if ("PROVIDER" in key) or ("NPI" in key):
                #     print key, " : ", record[key]
                print key, " : ", record[key]