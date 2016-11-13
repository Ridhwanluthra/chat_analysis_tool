import xml.etree.ElementTree as etree

tree = etree.parse('dict.xml')
root = tree.getroot()
for child in root:
	for n in child:
		print(type(n.text))