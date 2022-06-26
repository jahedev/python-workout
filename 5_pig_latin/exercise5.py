"""
The rules for translating words from English into PigLatin are quite simple:

- If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of theword. So “air” becomes “airway” and “eat” becomes “eatway.”

- If the word begins with any other letter, then we take the first letter, put it onthe  end  of  the  word,  and  then  add  “ay.”  Thus,  “python”  becomes  “ythonpay” and “computer” becomes “omputercay.”

(And yes, I recognize that the rules can be made more sophisticated. Let’s keep it sim-ple for the purposes of this exercise.)  For  this  exercise,  write  a  Python  function  (pig_latin)  that  takes  a  string  as  input,assumed to be an English word. The function should return the translation of this wordinto Pig Latin. You may assume that the word contains no capital letters or punctuation.
"""

def pig_latin(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    words = s.lower().split()
    for i, word in enumerate(words):
        first_letter = word[0]
        if first_letter in vowels:
            words[i] = '{}way'.format(word)
        else:
            words[i] = '{}{}ay'.format(word[1:], first_letter)
    
    return ' '.join(words)

if __name__ == '__main__':
    sentence = 'The quick brown fox jumps over the lazy dog'
    print(f'\n{sentence}\n\nBECOMES\n\n{pig_latin(sentence)}\n')