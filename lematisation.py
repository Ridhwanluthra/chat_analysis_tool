import re


class porter_stemmer:

    def __init__(self):
        self.re_is_cons = re.compile('[^aeiou]', re.IGNORECASE)
        self.re_contains_vowel = re.compile('.*[aeiou].*', re.IGNORECASE)

#############################################################################
# All the helper function for porter's stemming algorithm
#############################################################################
    def is_cons(self, letter):
        return bool(self.re_is_cons.match(letter))

    def is_consonant(self, word, i):
        letter = word[i]
        if self.is_cons(letter):
            # treating y as vowel if the letter before is vowel
            if letter == 'y' and self.is_cons(word[i - 1]):
                return False
            else:
                return True
        else:
            return False

    def is_vowel(self, word, i):
        return not(self.is_consonant(word, i))

    # *S
    def ends_with(self, stem, letter):
        return stem.endswith(letter)

    # *v*
    def contains_vowel(self, stem):
        return bool(self.re_contains_vowel.match(stem))

    # *d
    def double_cons(self, stem):
        if len(stem) >= 2:
            return bool(self.is_consonant(stem, -1) and
                        self.is_consonant(stem, -2))
        else:
            return False

    # gets the structure of the word in terms of [C][CV]*[V]
    def get_form(self, word):
        form = []
        form_str = ''
        for i in range(len(word)):
            if self.is_consonant(word, i):
                if i != 0:
                    prev = form[-1]
                    if prev != 'C':
                        form.append('C')
                else:
                    form.append('C')
            else:
                if i != 0:
                    prev = form[-1]
                    if prev != 'V':
                        form.append('V')
                else:
                    form.append('V')
        for j in form:
            form_str += j
        return form_str

    def get_m(self, word):
        form = self.get_form(word)
        m = form.count('VC')
        return m

    # *o
    def cvc(self, word):
        if len(word) >= 3:
            # picking the last 3 letters
            f = -3
            s = -2
            t = -1
            third = word[t]
            if self.is_consonant(
                word,
                f) and self.is_vowel(
                word,
                s) and self.is_consonant(
                word,
                    t):
                if third != 'w' and third != 'x' and third != 'y':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def replace(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        replaced = base + rep
        return replaced

    def replace_m0(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.get_m(base) > 0:
            replaced = base + rep
            return replaced
        else:
            return orig

    def replace_m1(self, orig, rem, rep):
        result = orig.rfind(rem)
        base = orig[:result]
        if self.get_m(base) > 1:
            replaced = base + rep
            return replaced
        else:
            return orig

#############################################################################
# MAIN STEPS OF THE PORTER'S STEMMING ALGORITHM BEGINS
#############################################################################

    def step_1a(self, word):
        if word.endswith('sses'):
            word = self.replace(word, 'sses', 'ss')
        elif word.endswith('ies'):
            word = self.replace(word, 'ies', 'i')
        elif word.endswith('ss'):
            word = self.replace(word, 'ss', 'ss')
        elif word.endswith('s'):
            word = self.replace(word, 's', '')
        else:
            pass
        return word

    def step_1b(self, word):
        flag = False
        if word.endswith('eed'):
            result = word.rfind('eed')
            base = word[:result]
            if self.get_m(base) > 0:
                word = base
                word += 'ee'
        elif word.endswith('ed'):
            result = word.rfind('ed')
            base = word[:result]
            if self.contains_vowel(base):
                word = base
                flag = True
        elif word.endswith('ing'):
            result = word.rfind('ing')
            base = word[:result]
            if self.contains_vowel(base):
                word = base
                flag = True
        if flag:
            if word.endswith('at') or word.endswith(
                    'bl') or word.endswith('iz'):
                word += 'e'
            elif self.double_cons(word) and not
            self.ends_with(word, 'l') and not
            self.ends_with(word, 's') and not
            self.ends_with(word, 'z'):
                word = word[:-1]
            elif self.get_m(word) == 1 and self.cvc(word):
                word += 'e'
            else:
                pass
        else:
            pass
        return word

    def step_1c(self, word):
        if word.endswith('y'):
            result = word.rfind('y')
            base = word[:result]
            if self.contains_vowel(base):
                word = base
                word += 'i'
        return word

    def step_2(self, word):
        if word.endswith('ational'):
            word = self.replace_m0(word, 'ational', 'ate')
        elif word.endswith('tional'):
            word = self.replace_m0(word, 'tional', 'tion')
        elif word.endswith('enci'):
            word = self.replace_m0(word, 'enci', 'ence')
        elif word.endswith('anci'):
            word = self.replace_m0(word, 'anci', 'ance')
        elif word.endswith('izer'):
            word = self.replace_m0(word, 'izer', 'ize')
        elif word.endswith('abli'):
            word = self.replace_m0(word, 'abli', 'able')
        elif word.endswith('alli'):
            word = self.replace_m0(word, 'alli', 'al')
        elif word.endswith('entli'):
            word = self.replace_m0(word, 'entli', 'ent')
        elif word.endswith('eli'):
            word = self.replace_m0(word, 'eli', 'e')
        elif word.endswith('ousli'):
            word = self.replace_m0(word, 'ousli', 'ous')
        elif word.endswith('ization'):
            word = self.replace_m0(word, 'ization', 'ize')
        elif word.endswith('ation'):
            word = self.replace_m0(word, 'ation', 'ate')
        elif word.endswith('ator'):
            word = self.replace_m0(word, 'ator', 'ate')
        elif word.endswith('alism'):
            word = self.replace_m0(word, 'alism', 'al')
        elif word.endswith('iveness'):
            word = self.replace_m0(word, 'iveness', 'ive')
        elif word.endswith('fulness'):
            word = self.replace_m0(word, 'fulness', 'ful')
        elif word.endswith('ousness'):
            word = self.replace_m0(word, 'ousness', 'ous')
        elif word.endswith('aliti'):
            word = self.replace_m0(word, 'aliti', 'al')
        elif word.endswith('iviti'):
            word = self.replace_m0(word, 'iviti', 'ive')
        elif word.endswith('biliti'):
            word = self.replace_m0(word, 'biliti', 'ble')
        return word

    def step_3(self, word):
        if word.endswith('icate'):
            word = self.replace_m0(word, 'icate', 'ic')
        elif word.endswith('ative'):
            word = self.replace_m0(word, 'ative', '')
        elif word.endswith('alize'):
            word = self.replace_m0(word, 'alize', 'al')
        elif word.endswith('iciti'):
            word = self.replace_m0(word, 'iciti', 'ic')
        elif word.endswith('ful'):
            word = self.replace_m0(word, 'ful', '')
        elif word.endswith('ness'):
            word = self.replace_m0(word, 'ness', '')
        return word

    def step_4(self, word):
        if word.endswith('al'):
            word = self.replace_m1(word, 'al', '')
        elif word.endswith('ance'):
            word = self.replace_m1(word, 'ance', '')
        elif word.endswith('ence'):
            word = self.replace_m1(word, 'ence', '')
        elif word.endswith('er'):
            word = self.replace_m1(word, 'er', '')
        elif word.endswith('ic'):
            word = self.replace_m1(word, 'ic', '')
        elif word.endswith('able'):
            word = self.replace_m1(word, 'able', '')
        elif word.endswith('ible'):
            word = self.replace_m1(word, 'ible', '')
        elif word.endswith('ant'):
            word = self.replace_m1(word, 'ant', '')
        elif word.endswith('ement'):
            word = self.replace_m1(word, 'ement', '')
        elif word.endswith('ment'):
            word = self.replace_m1(word, 'ment', '')
        elif word.endswith('ent'):
            word = self.replace_m1(word, 'ent', '')
        elif word.endswith('ou'):
            word = self.replace_m1(word, 'ou', '')
        elif word.endswith('ism'):
            word = self.replace_m1(word, 'ism', '')
        elif word.endswith('ate'):
            word = self.replace_m1(word, 'ate', '')
        elif word.endswith('iti'):
            word = self.replace_m1(word, 'iti', '')
        elif word.endswith('ous'):
            word = self.replace_m1(word, 'ous', '')
        elif word.endswith('ive'):
            word = self.replace_m1(word, 'ive', '')
        elif word.endswith('ize'):
            word = self.replace_m1(word, 'ize', '')
        elif word.endswith('ion'):
            result = word.rfind('ion')
            base = word[:result]
            if self.get_m(base) > 1 and (
                self.ends_with(
                    base,
                    's') or self.ends_with(
                    base,
                    't')):
                word = base
            word = self.replace_m1(word, '', '')
        return word

    def step_5a(self, word):
        if word.endswith('e'):
            base = word[:-1]
            if self.get_m(base) > 1:
                word = base
            elif self.get_m(base) == 1 and not self.cvc(base):
                word = base
        return word

    def step_5b(self, word):
        if self.get_m(word) > 1 and self.double_cons(
                word) and self.ends_with(word, 'l'):
            word = word[:-1]
        return word

    def stem(self, word):
        word = self.step_1a(word)
        word = self.step_1b(word)
        word = self.step_1c(word)
        word = self.step_2(word)
        word = self.step_3(word)
        word = self.step_4(word)
        word = self.step_5a(word)
        word = self.step_5b(word)
        return word

if __name__ == '__main__':
    from word_segmentation import word_list
    # word_list = th()
    for i in range(len(word_list)):
        p = porter_stemmer()
        print(word_list[i], ":  ", p.stem(word_list[i]))
