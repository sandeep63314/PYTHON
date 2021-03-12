from translate import Translator

_f = open('germanText.txt')
_text = _f.read()

translator = Translator(from_lang = 'de', to_lang = 'en')

trnslt = translator.translate(_text)

with open('englishText.txt' , mode = 'w') as _myfile:
    _myfile.write(trnslt)