from segmentation import segmentation
import xml.etree.ElementTree as etree
from xml.dom import minidom


class lexical_analysis(object):

    def __init__(self):
        self.segment_obj = segmentation()
        tree = etree.parse('dict.xml')
        self.root = tree.getroot()
        with open('sample.txt', 'r') as f:
            string = f.read()
            self.word_list = self.segment_obj.split_words(string)

    def xml_pretify(self, elem):
        rough_string = etree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="    ")

    # ADD THE WORD LIST ARG AND REMOVE FROM INIT
    def create_analysed_xml(self):
        my_dict = etree.Element('my_dict')
        for i in range(len(self.word_list)):
            exists = False
            exact_match = False
            for child in self.root:
                for word in child:
                    if word.text == self.word_list[i]:
                        print('exact;', self.word_list[i], ":    ", word.text)
                        exact_match = True
            if not exact_match:
                if word.text in self.word_list[i]:
                    print(self.word_list[i], ":    ", word.text)
        #                 exists = True
        #                 child_attrib = child.attrib['tags']
        #     entry = etree.SubElement(my_dict, 'entry')
        #     token = etree.SubElement(entry, 'token')
        #     token.text = self.word_list[i]
        #     if exists:
        #         entry.set('tags', child_attrib)
        # tree = self.xml_pretify(my_dict)
        # with open('lexi.xml', 'w') as lexi:
        #     lexi.truncate()
        #     lexi.write(tree)
        # tree = etree.ElementTree(self.xml_pretify(my_dict))
        # tree.write('lexi.xml')

if __name__ == '__main__':
    la = lexical_analysis()
    la.create_analysed_xml()
