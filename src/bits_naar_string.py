from hamming_code import *


ascii_naar_woord = {
    '10000001':'start',
    '00000010':'check_vraag',
    '00000011':'check_klopt',
    '00000100':'bericht',
    '00000101':'check_klopt_niet',
    '11111111':'eind',
    
    '00100000': ' ',
    '00100001': '!',
    '00100010': '"',
    '00100011': '#',
    '00100100': '$',
    '00100101': '%',
    '00100110': '&',
    '00100111': "'",
    '00101000': '(',
    '00101001': ')',
    '00101010': '*',
    '00101011': '+',
    '00101100': ',',
    '00101101': '-',
    '00101110': '.',
    '00101111': '/',
    '00110000': '0',
    '00110001': '1',
    '00110010': '2',
    '00110011': '3',
    '00110100': '4',
    '00110101': '5',
    '00110110': '6',
    '00110111': '7',
    '00111000': '8',
    '00111001': '9',
    '00111010': ':',
    '00111011': ';',
    '00111100': '<',
    '00111101': '=',
    '00111110': '>',
    '00111111': '?',
    '01000000': '@',
    '01000001': 'A',
    '01000010': 'B',
    '01000011': 'C',
    '01000100': 'D',
    '01000101': 'E',
    '01000110': 'F',
    '01000111': 'G',
    '01001000': 'H',
    '01001001': 'I',
    '01001010': 'J',
    '01001011': 'K',
    '01001100': 'L',
    '01001101': 'M',
    '01001110': 'N',
    '01001111': 'O',
    '01010000': 'P',
    '01010001': 'Q',
    '01010010': 'R',
    '01010011': 'S',
    '01010100': 'T',
    '01010101': 'U',
    '01010110': 'V',
    '01010111': 'W',
    '01011000': 'X',
    '01011001': 'Y',
    '01011010': 'Z',
    '01011011': '[',
    '01011100': '\\',
    '01011101': ']',
    '01011110': '^',
    '01011111': '_',
    '01100000': '`',
    '01100001': 'a',
    '01100010': 'b',
    '01100011': 'c',
    '01100100': 'd',
    '01100101': 'e',
    '01100110': 'f',
    '01100111': 'g',
    '01101000': 'h',
    '01101001': 'i',
    '01101010': 'j',
    '01101011': 'k',
    '01101100': 'l',
    '01101101': 'm',
    '01101110': 'n',
    '01101111': 'o',
    '01110000': 'p',
    '01110001': 'q',
    '01110010': 'r',
    '01110011': 's',
    '01110100': 't',
    '01110101': 'u',
    '01110110': 'v',
    '01110111': 'w',
    '01111000': 'x',
    '01111001': 'y',
    '01111010': 'z',
    '01111011': '{',
    '01111100': '|',
    '01111101': '}',
    '01111110': '~'
}

woord_naar_ascii = {
    'start': '10000001',
    'check_vraag.': '00000010',
    'check_klopt.': '00000011',
    'bericht.': '00000100',
    'check_klopt_niet.': '00000101',
    'eind': '11111111',

    ' ': '00100000',
    '!': '00100001',
    '"': '00100010',
    '#': '00100011',
    '$': '00100100',
    '%': '00100101',
    '&': '00100110',
    "'": '00100111',
    '(': '00101000',
    ')': '00101001',
    '*': '00101010',
    '+': '00101011',
    ',': '00101100',
    '-': '00101101',
    '.': '00101110',
    '/': '00101111',
    '0': '00110000',
    '1': '00110001',
    '2': '00110010',
    '3': '00110011',
    '4': '00110100',
    '5': '00110101',
    '6': '00110110',
    '7': '00110111',
    '8': '00111000',
    '9': '00111001',
    ':': '00111010',
    ';': '00111011',
    '<': '00111100',
    '=': '00111101',
    '>': '00111110',
    '?': '00111111',
    '@': '01000000',
    'A': '01000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'O': '01001111',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',
    '[': '01011011',
    '\\': '01011100',
    ']': '01011101',
    '^': '01011110',
    '_': '01011111',
    '`': '01100000',
    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',
    '{': '01111011',
    '|': '01111100',
    '}': '01111101',
    '~': '01111110'
}

#opbouw van een byte: plek 1: start. plek 2: type bericht ('bericht, check_vraag, check_klopt, check_klopt). plek 3 als het een bericht is: inhoud bericht. plek 4: stop  

#functie returned de type bericht, naam en eventuele tekst. als er geen tekst is (want bijvoorbeeld een gebruiker_online bericht) dan wordt er 0 gereturned 
def bits_naar_string(bits,ascii_dict):
    bits = bits[:-8]
    for i in range(8):
        bits = bits[:0] + bits[1:]
    bits = ham_naar_string(bits)
    byte=''
    type_bericht = '' 
    
    tekst=False
    tekst_woord=''
    for bit in bits:
        byte = byte + bit 
        if len(byte) == 8: 
            
            if byte in ascii_dict:
                byte_vertaald = ascii_dict[byte]
            
            if tekst == True:
                if byte_vertaald == 'eind':
                    return type_bericht, tekst_woord
                tekst_woord = tekst_woord + byte_vertaald

            if byte_vertaald=='bericht':
                type_bericht = byte_vertaald
                tekst = True
            elif byte_vertaald == 'check_vraag' or byte_vertaald == 'check_klopt' or byte_vertaald == 'check_klopt_niet':
                type_bericht = byte_vertaald
                return type_bericht, tekst_woord
            byte=''
    return type_bericht, tekst_woord

#deze gaat iets anders. in de functie worden alleen de naam en de tekst van bericht omgezet. de rest wordt buiten de functie eraan geplakt(maar die code bestaat nog niet)
def string_naar_bits(string, woord_naar_ascii):

    type_bericht = ''
    woord=''
    stop = False
    for letter in string: 
        if stop == True:
            
            letter = woord_naar_ascii[letter]
            
            woord = woord + letter
        if stop == False:
            
            type_bericht= type_bericht + letter
            if letter == '.':
                stop = True 
                woord = woord + woord_naar_ascii[type_bericht]
            
            
        
        
    return '10000001' + str(string_naar_ham(woord))+'11111111' 


        
type_bericht, tekst  = bits_naar_string('1000000111010001010001011010001101000010101001011010100111001111111111',ascii_naar_woord)
print(type_bericht)
print(tekst)


print(string_naar_bits('check_klopt_niet.', woord_naar_ascii))