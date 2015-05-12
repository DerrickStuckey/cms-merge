__author__ = 'dstuckey'

import re

# class Provider:
#     def __init__(self, npi, first_name, middle_initial, last_name, zip_first_5, zip_ext, last_org_name, city, state, country):
#         self.npi = npi
#         self.first_name = first_name
#         self.middle_initial = middle_initial
#         self.last_name = last_name
#         self.zip_first_5 = zip_first_5
#         self.zip_ext = zip_ext
#         self.last_org_name = last_org_name
#         self.city = city
#         self.state = state
#         self.country = country

#minimal identifying information (hopefully)
class Provider:
    def __init__(self, npi, first_name, middle_initial, last_name, zip_first_5, zip_ext, op_profile_id):
        self.npi = npi
        self.first_name = standardize_name(first_name)
        self.middle_initial = standardize_name(middle_initial)
        self.last_name = standardize_name(last_name)
        self.zip_first_5 = zip_first_5
        self.zip_ext = zip_ext
        self.op_profile_id = op_profile_id

def standardize_name(thestring):
    nospecials = re.sub("[^a-zA-Z]", "", thestring)
    return nospecials.lower()