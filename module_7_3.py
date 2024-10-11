import io
from pprint import pprint

class WordsFinder:
    file_names = []

    def __init__(self, *file_names):
        for i in file_names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:

                ls_ = []
                for line in file:
                    s = line.lower()
                    ns = ""
                    for char in s:

                        if char not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            ns += char
                        else:
                            continue

                    ls_ += ns.split()

            all_words[i] = ls_
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        res_ = {}
        for i in all_words.keys():
            count_ = 1
            for j in all_words[i]:

                if word.lower() != j:
                    count_ += 1
                else:
                    res_[i] = count_
                    break
        return res_

    def count(self, word):
        all_words = self.get_all_words()
        res_ = {}
        for i in all_words.keys():
            count_ = 0
            for j in all_words[i]:
                if word.lower() == j:
                    count_ +=1
            res_[i] = count_
        return res_



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего