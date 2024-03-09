#JSON - JavaScript Object Notation
import json

with open('data.json', 'r', encoding='utf8') as f:
    my_json = json.load(f)
    

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for txt in my_json["imdata"]:
    if len(txt["l1PhysIf"]["attributes"]["dn"]) == 42:
        print(txt["l1PhysIf"]["attributes"]["dn"], '                            ', txt["l1PhysIf"]["attributes"]["speed"], ' ', txt["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(txt["l1PhysIf"]["attributes"]["dn"], '                             ', txt["l1PhysIf"]["attributes"]["speed"], ' ', txt["l1PhysIf"]["attributes"]["mtu"])
