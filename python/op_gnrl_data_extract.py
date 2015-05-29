__author__ = 'dstuckey'

import csv
import zipfile

from collections import defaultdict

import provider

opn_gen_zipfilename = "../../12192014_RFRSHDTL.zip"

# manufacturer_name = 'Pfizer Inc.'
# output_filename = '../data/pfizer_payments.csv'
manufacturer_name = 'Kowa pharmaceutical Co.Ltd'
output_filename = '../data/kowa_payments.csv'

MFR_FIELD_1 = 'Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name'
MFR_FIELD_2 = 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name'

num_payments_dict = defaultdict(lambda:0)
total_values_dict = defaultdict(lambda:0)
first_name_dict = {}
last_name_dict = {}

with open(opn_gen_zipfilename) as thezip:
    unzipped = zipfile.ZipFile(thezip)

    gen_name = "OPPR_RFRSH_DTL_GNRL_12192014.csv"
    with unzipped.open(gen_name) as csvfile:
        reader = csv.DictReader(csvfile)

        #iterate through each record
        while(True):
            try:
                thisrecord = reader.next()
                profile_id = thisrecord['Physician_Profile_ID']
                manufacturer1 = thisrecord[MFR_FIELD_1]
                manufacturer2 = thisrecord[MFR_FIELD_2]
                dollar_value = float(thisrecord['Total_Amount_of_Payment_USDollars'])
                phys_first_name = thisrecord['Physician_First_Name']
                phys_last_name = thisrecord['Physician_Last_Name']

                if (manufacturer1 == manufacturer_name) or (manufacturer2 == manufacturer_name):
                    #dbg
                    print manufacturer_name, " payed ", profile_id

                    num_payments_dict[profile_id] = num_payments_dict[profile_id] + 1
                    total_values_dict[profile_id] = total_values_dict[profile_id] + dollar_value
                    first_name_dict[profile_id] = phys_first_name
                    last_name_dict[profile_id] = phys_last_name

            except StopIteration:
                print "done!"; break

#now write the output
with open(output_filename, 'w') as output_file:
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(['Physician_Profile_ID','Physician_First_Name','Physician_Last_Name',"Manufacturer","Num_Payments","Total_Payment_Value"])

    for profile_id in num_payments_dict.keys():
        num_payments = num_payments_dict[profile_id]
        total_values = total_values_dict[profile_id]
        phys_first_name = first_name_dict[profile_id]
        phys_last_name = last_name_dict[profile_id]
        csvwriter.writerow([profile_id,phys_first_name,phys_last_name,manufacturer_name,num_payments,total_values])