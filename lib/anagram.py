# your code goesclass Anagram:
    def __init__(self, word):
        self.word_letters = sorted(x for x in word)

    def match(self, my_list):
        new_list = []
        for item in my_list:
            if self.word_letters == sorted([i for i in item]):
                new_list.append(item)
        return new_list here!
