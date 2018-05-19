import re
import collections
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="windows-1251") as file_handler:
        text = file_handler.read()
        return text


def get_most_frequent_words(text, COUNT):
    text_list = re.findall("([a-zA-Zа-яА-ЯёЁ']+)", text.lower())
    word_frequency = collections.Counter(text_list).most_common(COUNT)
    return word_frequency


def print_top_word(sentence, word_frequency, COUNT):
    print(sentence)
    for count, word in enumerate(word_frequency):
        print((count+1), "- {} встречается {} раз(а)".format(word[0], word[1]))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Файл не выбран, пожалуйста, выберите файл")
    text = load_data(filepath)
    COUNT = 10
    word_frequency = get_most_frequent_words(text, COUNT)
    print_top_word("Самые популярные слова: ", word_frequency, COUNT)
