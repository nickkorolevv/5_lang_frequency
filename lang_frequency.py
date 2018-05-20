import re
import collections
import sys
import os


def load_data(filepath):
    with open(filepath, "r", encoding="windows-1251") as file_handler:
        text = file_handler.read()
        return text


def get_most_frequent_words(text, max_count):
    text_list = re.findall("([a-zA-Zа-яА-ЯёЁ']+)", text.lower())
    word_frequency = collections.Counter(text_list).most_common(max_count)
    return word_frequency


def print_top_word(sentence, words):
    print(sentence)
    for index, (word, count) in enumerate(words, 1):
        print(index, "- {} встречается {} раз(а)".format(word, count))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Файл не выбран, пожалуйста, выберите файл")
    if not(os.path.exists(filepath)):
        exit("Файла нет в директории")
    text = load_data(filepath)
    max_count = 10
    words = get_most_frequent_words(text, max_count)
    print_top_word("Самые популярные слова: ", words)
