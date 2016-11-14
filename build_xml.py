from get_pos_tags import tags, discription
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.ElementTree as etree
from xml.dom import minidom

def pretify(elem):
	rough_string = tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="    ")

root = Element('pos_tags')

for i in range(1,len(tags)):
	child = SubElement(root, 'tag')
	child.set('discription', discription[i])
	child.text = tags[i]
#print(pretify(root))
tree = etree.ElementTree(root)
tree.write('test_pos_tags.xml')