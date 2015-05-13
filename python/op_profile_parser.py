__author__ = 'dstuckey'

import csv
import zipfile

import provider

def extract_provider(record):
    thedoc = provider.Provider(
        npi = "",
        first_name = record['Physician_Profile_First_Name'],
        last_name = record['Physician_Profile_Last_Name'],
        middle_initial=record['Physician_Profile_Middle_Name'],
        zip_first_5 = record['Physician_Profile_Zip_Code'][0:5],
        zip_ext = record['Physician_Profile_Zip_Code'][5:9],
        op_profile_id = record['Physician_Profile_ID']
    )
    return thedoc

#openpayments_filename = "/Users/dstuckey/Downloads/12192014_RFRSHDTL/OPPR_SPLMTL_PH_PRFL_12192014.csv"

# with open(openpayments_filename) as opfile:
#     reader = csv.DictReader(opfile)
#     first = reader.next()
#     print(first)
#
#     for key in first.keys():
#         print key, " : ", first[key]

opn_gen_zipfilename = "../../12192014_RFRSHDTL.zip"
profile_filename = "OPPR_SPLMTL_PH_PRFL_12192014.csv"

output_filename = "op_profile_min.csv"

with open(opn_gen_zipfilename) as thezip:
    unzipped = zipfile.ZipFile(thezip)
    # names = unzipped.namelist()
    # for name in names:
    #     print name

    with unzipped.open(profile_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        first = reader.next()
        #print(first)

        # for key in first.keys():
        #    print key, " : ", first[key]

        first_provider = extract_provider(first)
        print first_provider.first_name, " ", first_provider.middle_initial, " ", first_provider.last_name

        # for i in range(0,5,1):
        #     record = reader.next()
        #     this_provider = extract_provider(record)
        #     print this_provider.first_name, " ", this_provider.middle_initial, " ", this_provider.last_name

        # truncate output filename
        # with open(output_filename, 'w') as output_file:
        #     pass

        with open(output_filename, 'w') as output_file:
            csvwriter = csv.writer(output_file)
            csvwriter.writerow(['FirstName','MiddleInitial','LastName','ZipCode5','NPI','OpProfileID'])
            while(True):
                thisrecord = reader.next()
                if (thisrecord == None):
                    break
                cur_provider = extract_provider(thisrecord)
                csvwriter.writerow([cur_provider.first_name, cur_provider.middle_initial, cur_provider.last_name,
                                    cur_provider.zip_first_5, cur_provider.npi, cur_provider.op_profile_id])


