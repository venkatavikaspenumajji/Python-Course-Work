import json 

with open("data.json","r")as file:
    data=json.load(file)

data["username"] = "bharat"
data["skills"].append("flask")

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)