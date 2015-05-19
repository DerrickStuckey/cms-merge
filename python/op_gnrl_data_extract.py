__author__ = 'dstuckey'

import csv
import zipfile

import provider

opn_gen_zipfilename = "../../12192014_RFRSHDTL.zip"

company_name = 'Pfizer Inc.'
output_filename = '../data/pfizer_payments.csv'

MFR_FIELD_1 = 'Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name'
MFR_FIELD_2 = 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name'

with open(opn_gen_zipfilename) as thezip:
    unzipped = zipfile.ZipFile(thezip)

    gen_name = "OPPR_RFRSH_DTL_GNRL_12192014.csv"
    with unzipped.open(gen_name) as csvfile:
        reader = csv.DictReader(csvfile)

        #write as we go
        with open(output_filename, 'w') as output_file:
            csvwriter = csv.writer(output_file)
            csvwriter.writerow(['Physician_Profile_ID',"Manufacturer","Num_Payments","Total_Payment_Value"])

            current_profile_id = "" #first NPI in file
            num_payments = 0
            total_value = 0

            #iterate through each record
            while(True):
                try:
                    thisrecord = reader.next()
                    profile_id = thisrecord['Physician_Profile_ID']
                    manufacturer1 = thisrecord[MFR_FIELD_1]
                    manufacturer2 = thisrecord[MFR_FIELD_2]
                    dollar_value = thisrecord['Total_Amount_of_Payment_USDollars']

                    if (manufacturer1 == company_name) or (manufacturer2 == company_name):
                        #dbg
                        print company_name, " payed ", profile_id

                        if (profile_id == current_profile_id):
                            #increment the count for this provider
                            total_value += dollar_value
                            num_payments += 1
                        else:
                            #write the count for the current provider, and start a new count
                            csvwriter.writerow([profile_id,company_name,num_payments,total_value])
                            current_profile_id = profile_id
                            total_value = dollar_value
                            num_payments = 1
                except StopIteration:
                    print "done!"; break
