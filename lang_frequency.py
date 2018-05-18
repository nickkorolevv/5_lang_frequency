import re
import collections
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="windows-1251") as file_handler:
        text = file_handler.read()
        return text


def get_most_frequent_words(text):
    match_obj = re.compile("([a-zA-Zа-яА-ЯёЁ']+)")
    text_data = match_obj.findall(text)
    word_list = []
    for word in text_data:
        word_list.append(word.lower())

    freq_dict = collections.Counter(word_list)
    return freq_dict


def print_top_word(sentence, freq_dict, count):
    print(sentence)
    counter = 1
    for dict_item in freq_dict.most_common(count):
        print(str(counter)+')', i[0], "встречается", i[1], "раз(а)")
        counter += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = format(sys.argv[1])
    else:
        exit("Файл не выбран, пожалуйста, выберите файл")

    text = load_data(filepath)
    freq_dict = get_most_frequent_words(text)
    count = 10
    print_top_word("Самые популярные слова: ", freq_dict, count)
