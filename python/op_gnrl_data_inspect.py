__author__ = 'dstuckey'

import csv
import zipfile

import provider

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


def extract_provider(record):
    #zip code (first 5) needs to come from "Physician Profile" record
    thedoc = provider.Provider(
        first_name = record['Physician_First_Name'],
        last_name = record['Physician_Last_Name'],
        middle_initial=record['Physician_Middle_Name'],
        zip_first_5 = record['Recipient_Zip_Code'][0:5],
        zip_ext = record['Recipient_Zip_Code'][5:9], #probably blank
        op_profile_id = record['Physician_Profile_ID']
    )
