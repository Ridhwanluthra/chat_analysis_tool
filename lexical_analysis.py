from segmentation import segmentation
import xml.etree.ElementTree as etree
from xml.dom import minidom


class lexical_analysis(object):

    def __init__(self):
        # open the sample file for analysis
        self.segment_obj = segmentation()
        tree = etree.parse('dict.xml')
        self.root = tree.getroot()
        self.tag_root = etree.parse('pos_tags.xml').getroot()
        with open('sample.txt', 'r') as f:
            string = f.read()
            self.word_list = self.segment_obj.split_words(string)

    # helps in putting the xml in a human readable form
    def xml_pretify(self, elem):
        rough_string = etree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="    ")

    # ADD THE WORD LIST ARG AND REMOVE FROM INIT
    def create_analysed_xml(self):
        my_dict = etree.Element('my_dict')
        # loop through all the words
        for i in range(len(self.word_list)):
            exists = False
            # loop through all the tags
            for child in self.root:
                for word in child:
                    if word.text == self.word_list[i]:
                        exists = True
                        child_attrib = child.attrib['tags']
            entry = etree.SubElement(my_dict, 'entry')
            token = etree.SubElement(entry, 'token')
            token.text = self.word_list[i]
            if exists:
                entry.set('tags', child_attrib)
        tree = self.xml_pretify(my_dict)
        with open('lexi.xml', 'w') as lexi:
            lexi.truncate()
            lexi.write(tree)
        # tree = etree.ElementTree(self.xml_pretify(my_dict))
        # tree.write('lexi.xml')

    def differentiate_persons(self):
        my_dict = etree.Element('my_dict')
        # loop through all the words
        for i in range(len(self.word_list)):
            exists = False
            # loop through all the tags
            if self.word_list[i] == 'Person1':
                person1 = True
            elif self.word_list[i] == 'Person2':
                person1 = False
            for child in self.root:
                for word in child:
                    if word.text == self.word_list[i]:
                        exists = True
                        child_attrib = child.attrib['tags']
            entry = etree.SubElement(my_dict, 'entry')
            token = etree.SubElement(entry, 'token')
            token.text = self.word_list[i]
            if person1:
                entry.set('person', '1')
            elif not person1:
                entry.set('person', '2')
            if exists:
                entry.set('tags', child_attrib)
        tree = self.xml_pretify(my_dict)
        with open('lexi.xml', 'w') as lexi:
            lexi.truncate()
            lexi.write(tree)
        # tree = etree.ElementTree(self.xml_pretify(my_dict))
        # tree.write('lexi.xml')

    def simplify_pos_tags(self):
        # defining only 5 word classes for now:
        # they are noun, verb, adjective, adverb, others
        pos_tags_list = []
        for child in self.tag_root:
            if child.text[0] == 'N':
    #     <tag discription="Coordinating conjunction ">CC</tag>
    # <tag discription="Cardinal number ">CD</tag>
    # <tag discription="Determiner ">DT</tag>
    # <tag discription="Existential there ">EX</tag>
    # <tag discription="Foreign word ">FW</tag>
    # <tag discription="Preposition or subordinating conjunction ">IN</tag>
    # <tag discription="Adjective ">JJ</tag>
    # <tag discription="Adjective, comparative ">JJR</tag>
    # <tag discription="Adjective, superlative ">JJS</tag>
    # <tag discription="List item marker ">LS</tag>
    # <tag discription="Modal ">MD</tag>
    # <tag discription="Noun, singular or mass ">NN</tag>
    # <tag discription="Noun, plural ">NNS</tag>
    # <tag discription="Proper noun, singular ">NNP</tag>
    # <tag discription="Proper noun, plural ">NNPS</tag>
    # <tag discription="Predeterminer ">PDT</tag>
    # <tag discription="Possessive ending ">POS</tag>
    # <tag discription="Personal pronoun ">PRP</tag>
    # <tag discription="Possessive pronoun ">PRP$</tag>
    # <tag discription="Adverb ">RB</tag>
    # <tag discription="Adverb, comparative ">RBR</tag>
    # <tag discription="Adverb, superlative ">RBS</tag>
    # <tag discription="Particle ">RP</tag>
    # <tag discription="Symbol ">SYM</tag>
    # <tag discription="to ">TO</tag>
    # <tag discription="Interjection ">UH</tag>
    # <tag discription="Verb, base form ">VB</tag>
    # <tag discription="Verb, past tense ">VBD</tag>
    # <tag discription="Verb, gerund or present participle ">VBG</tag>
    # <tag discription="Verb, past participle ">VBN</tag>
    # <tag discription="Verb, non-3rd person singular present ">VBP</tag>
    # <tag discription="Verb, 3rd person singular present ">VBZ</tag>
    # <tag discription="Wh-determiner ">WDT</tag>
    # <tag discription="Wh-pronoun ">WP</tag>
    # <tag discription="Possessive wh-pronoun ">WP$</tag>
    # <tag discription="Wh-adverb &#10;">WRB</tag>

if __name__ == '__main__':
    la = lexical_analysis()
    # la.create_analysed_xml()
    la.simplify_pos_tags()
