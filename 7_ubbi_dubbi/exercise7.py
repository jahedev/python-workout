"""
In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). In theory, you only put an ub before every vowel sound, rather than before each vowel. Given that this is a book about Python and not linguistics, I hope that you’ll forgive this slight dif- ference in definition.
"""

import io

def ubbi_dubbi(sentence: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    output = io.StringIO()
    
    for chr in sentence.lower().capitalize():
        if chr in vowels:
            output.write('ub' + chr)
        else:
            output.write(chr)
    
    return output.getvalue()

if __name__ == '__main__':
    sentence = 'I love to drink milk.'
    print(f'\n{ubbi_dubbi(sentence)}\n')