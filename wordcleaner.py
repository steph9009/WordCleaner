import sys
import re
sys.stdin.reconfigure(encoding='ansi')

def wordcheck(word, debug, regular_words, debug_5char, debug_composte, debug_solonum, debug_consonanti, debug_vocali, debug_5cifre, debug_symbol):
    #cerco parole più corte di 5 caratteri
    if re.search(r"\b.{1,4}\s\d+\s\d+\b", word):
        debug_5char.write(word + '\n')
        return
    #cerco parole composte solo da numeri
    if re.search(r"\b\d+\s\d+\s\d+\b", word):
        debug_solonum.write(word + '\n')
        return  
    #cerco parole composte solo da numeri ed un solo simbolo qualsiasi
    if re.search(r"\b(\d+.\d+|\d+.|.\d+)\s\d+\s\d+\b", word):
        debug_solonum.write(word + '\n')
        return
    #cerco parole composte solo da numeri e due simboli qualsiasi
    if re.search(r"\b(\d+.{2}\d+|\d+.{2}|.{2}\d+)\s\d+\s\d+\b", word):
        debug.write(word + '\n')
        return
    #cerco parole composte solo da lettere ed un solo numero
    if re.search(r"\b(\w+\d|\d\w+|\w+\d\w+)\s\d+\s\d+\b", word):
        debug.write(word + '\n')
        return
    #cerco parole tipo abc123abc123 123abc123abc ecc. (perché presumibilmente non naturali)
    if re.search(r"\b.*([0-9]+[a-z]+|[a-z]+[0-9]+){2,}.*\s\d+\s\d+\b", word):
        debug_composte.write(word + '\n')
        return
    #cerco parole con 5+ "non vocali" (es. solo consonanti) consecutive (perché difficilmente naturali)
    if re.search(r".*[^aeiou\d\W]{5,}.*", word):
        debug_consonanti.write(word + '\n')
        return
    #cerco parole con 4+ vocali consecutive (perché difficilmente naturali)
    if re.search(r".*[aeiou]{4,}.*", word):
        debug_vocali.write(word + '\n')
        return
    #cerco parole con 5+ cifre numeriche consecutive perché troppo rumorose
    if re.search(r".*[\d]{5,}.*\s\d+\s\d+\b", word):
        debug_5cifre.write(word + '\n')
        return
    #cerco parole contenenti simboli non alfanumerici né spazi né "-_"
    for char in word:
        if not char.isdigit() and not char.isspace() and char not in ['à', 'è', 'é', 'ì', 'ò', 'ù', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_']:
            debug_symbol.write(word + '\n')
            return
    regular_words.write(word + '\n')
    return

filein = open('..\words+wordCounts+docCounts_V1.txt', encoding='ansi', mode='r')

wordlist = filein.read().splitlines()

regular_words = open('ElencoParolePulite.txt', encoding='ansi', mode='w')
debug = open('debug.txt', encoding='ansi', mode='w')

debug_5char = open('debug_5char.txt', encoding='ansi', mode='w')
debug_composte = open('debug_composte.txt', encoding='ansi', mode='w')
debug_solonum = open('debug_solonum.txt', encoding='ansi', mode='w')
debug_consonanti = open('debug_consonanti.txt', encoding='ansi', mode='w')
debug_vocali = open('debug_vocali.txt', encoding='ansi', mode='w')
debug_5cifre = open('debug_5cifre.txt', encoding='ansi', mode='w')
debug_symbol = open('debug_symbol.txt', encoding='ansi', mode='w')

for word in wordlist:
    wordcheck(word, debug, regular_words, debug_5char, debug_composte, debug_solonum, debug_consonanti, debug_vocali, debug_5cifre, debug_symbol)   
