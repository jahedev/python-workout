"""
Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated let- ters. In other words
  * For each word, find the letter that appears the most times.
  * Find the word whose most-repeated letter appears more than any other.
That is, if words is set to
words = ['this', 'is', 'an', 'elementary', 'test', 'example']
then your function should return elementary. That’s because
  * this has no repeating letters.
  * is has no repeating letters.
  * an has no repeating letters.
  * elementary has one repeating letter, e, which appears three times.  
  * test has one repeating letter, t, which appears twice.
  * example has one repeating letter, e, which appears twice.
"""

# take a list of words, or a sentence of type str

from collections import Counter


# -----------------------------------------------
#  |                 3 Solutions                |
# -----------------------------------------------
# 1) Using Counter()
# 2) Using dictionary comprehensions and max
# 3) Using only dictionaries and loops

def most_repeating_word(words):
    if type(words) == str:
        words = words.split(' ')

    ######### Using Counter ###################
    # return max(words, key=lambda word: Counter(word).most_common()[0][1])
    ############################################
    #
    #
    ######## Without Counter ###################
    # def get_freq(word):
    #     return {chr: word.count(chr) for chr in word}

    # def get_max_value(_dict):
    #     return max(_dict.values())
    # return max(words, key=lambda word: get_max_value(get_freq(word)))
    #############################################
    #
    #
    ####### Without comprehensions or max #######
    def get_freq(word):
        freq = {}
        for chr in word:
            freq[chr] = freq.get(chr, 0) + 1
        return freq

    def max_freq_value(freq):
        curr_max = 0
        for _, v in freq.items():
            if v > curr_max:
                curr_max = v
        return curr_max

    def _most_repeating_word(words):
        curr_best_word = ''
        curr_max_occurences = 0

        for word in words:
            letter_frequency = get_freq(word)
            occurences = max_freq_value(letter_frequency)
            if occurences > curr_max_occurences:
                curr_best_word = word
                curr_max_occurences = occurences

        return curr_best_word

    return _most_repeating_word(words)
    #############################################


if __name__ == '__main__':
    sentence = 'this is an elementary test example'
    print(most_repeating_word(sentence))
