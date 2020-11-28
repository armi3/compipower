from json2html import *
from yattag import Doc
import json
import webbrowser


def make_table(dictionary):
    table_in_html = json2html.convert(json=dictionary)

    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('body'):
            doc.asis(table_in_html)

    #print(doc.getvalue())

    f = open("outputs/table.html", "w")
    f.write(doc.getvalue())
    f.close()

