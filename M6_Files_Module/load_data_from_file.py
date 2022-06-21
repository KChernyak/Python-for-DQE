import os
import sys
from previous_modules.file_data import FileData

default_path = 'C:\Git\Personal_Git\Python for DQE\M6_Files_Module\content_to_load'
input_file_name = 'Content_to_load.txt'


def choose_path():
    path = input('Enter path of the file or pres Enter to choose default path.')
    if path == '':
        return default_path
    return path


def locate_file(file_path, file_name):
    try:
        with open(f'{file_path}\\{file_name}', encoding='utf-8', mode='r+') as f:
            return f.read()
    except IOError:
        print(f'File {file_path}\\{file_name} was not found!')
        sys.exit()


def write_to_file(text):
    with open('Newsfeed.txt', 'a', encoding="utf-8") as file:
        file.write(text)
    print('New record has successfully added to the file')


def delete_source_file():
    os.remove(f'{default_path}\\{input_file_name}')


def main():
    file_path = choose_path()
    print(file_path)
    file_content = locate_file(file_path, input_file_name)
    file_data = FileData(file_content)
    write_to_file(str(file_data))
    delete_source_file()


main()