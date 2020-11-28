from json2html import *
from yattag import Doc
import json
import webbrowser

print("======================================================================")

f = open('output.json',)
# returns JSON object as a dictionary
data = json.load(f)
f.close()

estesifunciona = [{
        "Number": "1",
        "Scope": "Generic Man",
        "Line": "['brown hair', '5.10, 'accountant']",
        "ID": "Generic Man",
        "Type": "Generic Man"
}, {
        "Number": "2",
        "Scope": "Generic Man",
        "Line": "['brown hair', '5.10, 'accountant']",
        "ID": "Generic Man",
        "Type": "Generic Man"
}, {
        "Number": "3",
        "Scope": "Generic Man",
        "Line": "['brown hair', '5.10, 'accountant']",
        "ID": "Generic Man",
        "Type": "Generic Man"
}, {
        "Number": "4",
        "Scope": "Generic Man",
        "Line": "['brown hair', '5.10, 'accountant']",
        "ID": "Generic Man",
        "Type": "Generic Man"
}, {
        "Number": "5",
        "Scope": "Generic Man",
        "Line": "['brown hair', '5.10, 'accountant']",
        "ID": "Generic Man",
        "Type": "Generic Man"
}]


test = json2html.convert(json = data)
print(test)
print("======================================================================")

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        doc.asis(test)

print(doc.getvalue())
print("======================================================================")

f = open("table.html", "w")
f.write(doc.getvalue())
f.close()

#open and read the file after the appending:
f = open("table.html", "r")
print(f.read())

new = 2
url = "table.html"
webbrowser.open(url,new=new)