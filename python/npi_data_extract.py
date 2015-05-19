__author__ = 'dstuckey'

import csv
import zipfile
import provider

npi_filename = "../../NPPES_Data_Dissemination_April_2015.zip"

def extract_provider(record):
    thedoc = provider.Provider(
        npi = record['NPI'],
        first_name = record['Provider First Name'],
        last_name = record['Provider Last Name (Legal Name)'],
        middle_initial=record['Provider Middle Name'],
        zip_first_5 = record['Provider Business Practice Location Address Postal Code'][0:5], #one other option for zip
        zip_ext = record['Provider Business Practice Location Address Postal Code'][5:9],
        op_profile_id = ""
    )
    return thedoc

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
        # print "First Record Fields and Values:"
        # for key in first.keys():
        #     print key, " : ", first[key]

        first_provider = extract_provider(first)
        print first_provider.first_name, " ", first_provider.middle_initial, " ", first_provider.last_name
        print first_provider.npi

        for i in range(0,5,1):
            record = reader.next()
            print "Provider zip codes:"
            # print record['Provider Business Practice Location Address Postal Code']
            # print record['Provider Business Mailing Address Postal Code']
            last_name = record['Provider Last Name (Legal Name)']
            #print "Last Name: ", record['Provider Last Name (Legal Name)']
            # print "Other Last Name: ", record['Provider Other Last Name']
            if last_name == "":
                print "Record missing last name:"
                for key in record.keys():
                    print key, " : ", record[key]
                break

        output_filename = "npi_data_min.csv"

        with open(output_filename, 'w') as output_file:
            csvwriter = csv.writer(output_file)
            csvwriter.writerow(['FirstName','MiddleInitial','LastName','ZipCode5','NPI','OpProfileID'])
            while(True):
                try:
                    thisrecord = reader.next()
                except StopIteration:
                    print "done"; break
                cur_provider = extract_provider(thisrecord)
                csvwriter.writerow([cur_provider.first_name, cur_provider.middle_initial, cur_provider.last_name,
                                    cur_provider.zip_first_5, cur_provider.npi, cur_provider.op_profile_id])
