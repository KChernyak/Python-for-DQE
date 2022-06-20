import json
import os
import sys
import csv
import pandas as pd
import regex as re
import xml.etree.ElementTree as ElementTree

from previous_modules.file_data import FileData

default_path = 'C:\Git\Python for DQE\M9_XML'
txt_file = 'Content_to_load.txt'
json_file = 'Content_to_load.json'
xml_file = 'Content_to_load.xml'
newsfeed = 'Newsfeed.txt'


# Create CSV statistics class

csv_words = 'word_count.csv'
csv_letters = 'letters_statistic.csv'


class CreateCSV:
    def __init__(self, def_path, news_file):
        self.def_path = def_path
        self.news_file = news_file
        words_dict = self.word_count()
        self.create_words_csv(words_dict)
        letters_list = self.create_letters_list(self.news_file)
        count_of_letters = self.create_letters_count_list(letters_list)
        self.create_stat_csv(count_of_letters)
        print(f'Files {csv_words} and {csv_letters} were created.')

    def word_count(self):
        word_pattern = r"\p{L}+"
        with open(f'{self.def_path}\\{self.news_file}') as text_file:
            words_dict = {}
            words = re.findall(word_pattern, text_file.read().lower())
            for word in words:
                if word not in words_dict.keys():
                    words_dict[word] = 1
                elif word in words_dict.keys():
                    words_dict[word] += 1
        return words_dict

    @staticmethod
    def create_words_csv(words_dict):
        with open(csv_words, 'w', encoding="utf-8", newline='') as csv_words_collection:
            header = ['Word', 'Count of repeating']
            writer = csv.DictWriter(csv_words_collection, fieldnames=header)
            writer.writeheader()
            for key, value in words_dict.items():
                writer.writerow({'Word': key, 'Count of repeating': value})
        sort_csv(csv_words, 'Word')

    @staticmethod
    def create_letters_list(text_file):
        letter_pattern = r"\p{L}"
        letters = list()
        with open(text_file, 'r', encoding="utf-8") as file:
            text = file.read()
            for lt in re.findall(letter_pattern, text):
                letters.append(lt)
        return letters

    @staticmethod
    def create_letters_count_list(letters_list):
        count_of_letters = []
        letters_list_len = len(letters_list)
        for el in letters_list:
            lwr = letters_list.count(el.lower())
            upr = letters_list.count(el.upper())
            prc = round(((lwr + upr) / letters_list_len) * 100, 3)
            count_of_letters.append((el.lower(), lwr + upr, upr, prc))
        count_of_letters = list(dict.fromkeys(count_of_letters))
        return count_of_letters

    @staticmethod
    def create_stat_csv(count_of_letters):
        with open(csv_letters, 'w', encoding="utf-8", newline='') as csv_stat:
            header = ['Letter', 'Count_all', 'Count_uppercase', 'Percentage %']
            writer = csv.DictWriter(csv_stat, fieldnames=header)
            writer.writeheader()
            for ltr, lwr, upr, prc in count_of_letters:
                writer.writerow({'Letter': ltr, 'Count_all': lwr, 'Count_uppercase': upr, 'Percentage %': prc})
        sort_csv(csv_letters, 'Letter')


def sort_csv(csv_name, column_name):
    df = pd.read_csv(csv_name, encoding="utf-8")
    sorted_df = df.sort_values(column_name)
    sorted_df.to_csv(csv_name, index=False)


# File with newsfeed creation from content to load from different file formats


def choose_path():
    path = input('Type path of the file or just hit Enter to choose default path')
    if path == '':
        return default_path
    return path


def json_to_list(path, file):
    with open(f'{path}\\{file}') as file_json:
        json_list = json.load(file_json)
    return json_list


def xml_to_list(path, file):
    file_xml = ElementTree.parse(f'{path}\\{file}')
    root = file_xml.getroot()
    xml_list = list()
    for element in root:
        temp_dict = dict()
        for tag in element:
            temp_dict[tag.tag] = tag.text
        xml_list.append(temp_dict)
    return xml_list


def locate_file(file_path, file_name):
    try:
        with open(f'{file_path}\\{file_name}', "r+", encoding='utf-8') as file:
            return file.read()
    except IOError:
        print(f'File {file_path}\\{file_name} was not found!')
        sys.exit()


def write_to_file(text):
    with open(newsfeed, 'a', encoding="utf-8") as f:
        f.write(text)
    print(text + 'Was added')


def delete_source_file(file):
    os.remove(file)


def main():
    file_path = choose_path()
    user_choice = input("t - for .txt file, j - for .json, x - for .xml. Choose one of the listed options, otherwise "
                        "- exit from the program\n")
    if user_choice == 't':
        file_content = locate_file(file_path, txt_file)
        file_data = FileData(file_content, 't')
        write_to_file(str(file_data))
        delete_source_file(txt_file)
    elif user_choice == 'j':
        file_content = json_to_list(file_path, json_file)
        file_data = FileData(file_content, 'j')
        write_to_file(str(file_data))
        delete_source_file(json_file)
    elif user_choice == 'x':
        file_content = xml_to_list(file_path, xml_file)
        file_data = FileData(file_content, 'x')
        write_to_file(str(file_data))
        delete_source_file(xml_file)
    else:
        print('Exiting the program. Choose from proposed file formats')
        sys.exit()
    CreateCSV(file_path, newsfeed)


main()
