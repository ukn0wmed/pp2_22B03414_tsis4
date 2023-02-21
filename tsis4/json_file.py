import json

# Open the JSON file and load the data
with open("sample-data.json", "r") as f:
    data = json.load(f)

# Define column headers
headers = ["DN", "Description", "Speed", "MTU"]

# Print the column headers
print("{:<50}{:<30}{:<8}{}".format(*headers))
print("-" * 70)

# Loop through the interfaces and print their details
for interface in data["imdata"]:
    dn = interface["l1PhysIf"]["attributes"]["dn"]
    descr = interface["l1PhysIf"]["attributes"].get("descr", "")
    speed = interface["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = interface["l1PhysIf"]["attributes"].get("mtu", "")
    print("{:<50}{:<30}{:<8}{}".format(dn, descr, speed, mtu))
