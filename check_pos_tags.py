import xml.etree.ElementTree as etree


class check_pos_tags(object):

    def __init__(self):
        self.dict_root = etree.parse('dict.xml').getroot()
        self.pos_root = etree.parse('pos_tags.xml').getroot()

    def pos_tags_not_in_dict(self):
        for pos_child in self.pos_root:
            found_flag = False
            for dict_child in self.dict_root:
                n_list = dict_child.attrib['tags'].split(' ')
                # print(n_list)
                if pos_child.text in n_list:
                    found_flag = True
            if not found_flag:
                print(pos_child.text)

    def dict_tags_not_in_pos(self):
        for dict_child in self.dict_root:
            found_flag = False
            n_list = dict_child.attrib['tags'].split(' ')
            for pos_child in self.pos_root:
                for tag in n_list:
                    if tag == pos_child.text:
                        found_flag = True
            if not found_flag:
                print(n_list)

if __name__ == '__main__':
    check = check_pos_tags()
    check.dict_tags_not_in_pos()
