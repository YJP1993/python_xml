import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()


print root[0][1].text

print "Hello!"