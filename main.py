from greets import greeting
from translate import Translator

translator=Translator(to_lang='lv')
for g in greeting:
    print(translator.translate(g).title())