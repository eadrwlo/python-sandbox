import re
import sys

file = open(sys.argv[1], 'r+', encoding='UTF-8')

new_txt_file = open('new_subtitles.txt', 'w', encoding='UTF-8')

input_str = file.read()

patter = '[ćśżźłóńąŚĆŹŻŁÓŃĄ]'

input_str = [x for x in input_str]

dict_pol = {
    'ś': 's',
    'ć': 'c',
    'ż': 'z',
    'ź': 'z',
    'ą': 'a',
    'ł': 'l',
    'ó': 'o',
    'ń': 'n',
    'ę': 'e',
    'Ś': 'S',
    'Ć': 'C',
    'Ź': 'Z',
    'Ż': 'Z',
    'Ą': 'A',
    'Ł': 'L',
    'Ó': 'O',
    'Ń': 'N'

}


def char_sek(input_str_):
    for i, x in enumerate(input_str_):
        obj = re.match(patter, x)

        if obj:
            input_str_[i] = dict_pol[x]


char_sek(input_str)

new_txt_file.write(''.join(input_str))
new_txt_file.close()
file.close()
