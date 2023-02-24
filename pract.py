import json
import pyperclip
with open("data.json", "r") as data_file:
    readf= json.load(data_file)
    print(readf["json"]['password'])
