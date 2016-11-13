import xml.etree.ElementTree as etree

tree = etree.parse('feed.xml')
root = tree.getroot()
print(root)