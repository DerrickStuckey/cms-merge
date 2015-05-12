__author__ = 'dstuckey'

import csv
import zipfile

#openpayments_filename = "/Users/dstuckey/Downloads/12192014_RFRSHDTL/OPPR_RFRSH_DTL_GNRL_12192014.csv"
#openpayments_filename = "/Users/dstuckey/Downloads/12192014_RFRSHDTL/OPPR_RFRSH_DTL_OWNRSHP_12192014.csv"
#openpayments_filename = "/Users/dstuckey/Downloads/12192014_RFRSHDTL/OPPR_RFRSH_DTL_RSRCH_12192014.csv"
#openpayments_filename = "/Users/dstuckey/Downloads/12192014_RFRSHDTL/OPPR_SPLMTL_PH_PRFL_12192014.csv"

# with open(openpayments_filename) as opfile:
#     reader = csv.DictReader(opfile)
#     first = reader.next()
#     print(first)
#
#     for key in first.keys():
#         print key, " : ", first[key]

opn_gen_zipfilename = "../../12192014_RFRSHDTL.zip"

with open(opn_gen_zipfilename) as thezip:
    unzipped = zipfile.ZipFile(thezip)
    # names = unzipped.namelist()
    # for name in names:
    #     print name

    gen_name = "OPPR_RFRSH_DTL_GNRL_12192014.csv"
    with unzipped.open(gen_name) as csvfile:
        reader = csv.DictReader(csvfile)
        first = reader.next()
        #print(first)

        for key in first.keys():
            print key, " : ", first[key]


