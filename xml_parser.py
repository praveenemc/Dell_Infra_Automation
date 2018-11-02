#!/usr/bin/python
import xml.etree.ElementTree as ET
from prettytable import PrettyTable

tbl_output = PrettyTable()
tbl_output.field_names = ["Server Attribute", "Value"]


tree = ET.parse('pe_sample_output.xml')
root = tree.getroot()
for elem in root:
    for subelem in elem:
        #print subelem.attrib['Name'], subelem.text
        tbl_output.add_row([subelem.attrib['Name'], subelem.text])

print tbl_output
