"""
Now that you’ve successfully written a translator for a single English word, let’s makethings more difficult: translate a series of English words into Pig Latin. Write a func-tion  called pl_sentence  that  takes  a  string  containing  several  words,  separated  byspaces. (To make things easier, we won’t actually ask for a real sentence. More specifi-cally, there will be no capital letters or punctuation.)
"""

import io

def pig_latin(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    output = io.StringIO()
    
    words = s.lower().split()
    for i, word in enumerate(words):
        first_letter = word[0]
        if first_letter in vowels:
            output.write('{}way '.format(word))
        else:
            output.write('{}{}ay '.format(word[1:], first_letter))
    
    return output.getvalue()

if __name__ == '__main__':
    sentence = 'this is a test translation'
    print(f'\n{sentence}\n\nBECOMES\n\n{pig_latin(sentence)}\n')