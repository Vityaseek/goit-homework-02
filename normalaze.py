from pathlib import Path


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЄІЇҐ"



TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g","A", "B", "V", "G", "D", "E", "E", "J", "Z", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
               "F", "H", "TS", "CH", "SH", "SCH", "", "Y", "", "E", "YU", "YA", "JE", "I", "JI", "G" '1', '2', '3',
               '4', '5', '6', '7', '8', '9','0', 'W', 'w', 'Q', 'q', 'C', 'c', 'X', 'x')

list2 = ['(', ')', '*', '+', ',', '-', '.', '/',
         '\\', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', "'", ' ']
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

def normalazie(path):
    for_name = path.translate(TRANS)
    print(type(for_name))
    for_name = Path(for_name)
    string = ''
    for i in for_name.stem:
        if i in TRANSLATION:
            string += i
        else:
            if i == i.upper() and i not in list2:
                string += i
            else:
                i = str(i).replace(i, '_')
                string += i
    return string