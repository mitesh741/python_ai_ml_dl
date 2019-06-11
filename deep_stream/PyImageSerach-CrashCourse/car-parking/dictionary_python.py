import time
import pprint

name_dict = {"col1": 973, "col2": "1452 29th Street",
             "col3": "Here is a value", "col4" : "Here is another value",
             "col5" : "NULL", "col6": "Scottsdale",
             "col7": "N/A", "col8" : "41.5946922",
             "col9": "Building", "col10" : "Commercial"}


for k, v in name_dict.items():
    print("This is the key: '%s' and this is the value '%s'\n" % (k, v) )
    new_key = "Mitesh"
    name_dict[new_key] = name_dict.pop(k)

print(name_dict)
