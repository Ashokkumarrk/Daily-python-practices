import csv
import json
with open("C:/Users/ashok/Downloads/doctors (1).csv","r") as f:
    reader=csv.DictReader(f)
    payload=list(reader)
with open("output.json","w") as f:
    json.dump(payload,f,indent=4)
print("conversion success")