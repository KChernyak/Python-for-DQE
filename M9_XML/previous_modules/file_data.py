import sys
import sys
from datetime import datetime

from previous_modules.task3_refactored import normalize_string_case
sys.path.append('/')


# Publications related part (creation rows News, PrivateAd, Event)


class Record:

    def header(self):
        class_name = self.__class__.__name__
        return f"{class_name} {(30 - len(class_name) - 1) * '-'}"

    def footer(self):
        return f"{30 * '-'}"


class News(Record):

    def __str__(self):
        return self.record

    def __init__(self, news_text, city):
        super().__init__()
        self.news_text = news_text
        self.city_name = city
        self.publish_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.record = self.header() + '\n' + \
                      self.news_text + '\n' + \
                      self.city_name + ', ' + self.publish_date + '\n' + \
                      self.footer()


class PrivateAd(Record):
    def __str__(self):
        return self.record

    def __init__(self, ad_text, ad_actual_until):
        self.ad_text = ad_text
        self.ad_actual_until = ad_actual_until
        self.get_actual_until_date()
        self.current_date = datetime.now()
        date_diff = self.ad_actual_until - self.current_date
        if date_diff.days < 0:
            print(f"Looks like ad expired. Ad was not added")
            sys.exit()
        self.record = self.header() + '\n' \
                      + self.ad_text + '\n' \
                      + f'Actual until: ' + str(self.ad_actual_until.strftime('%Y-%m-%d')) \
                      + f', {date_diff.days} days left' + '\n' \
                      + self.footer()

    def get_actual_until_date(self):
        try:
            self.ad_actual_until = datetime.strptime(self.ad_actual_until, '%Y-%m-%d')
        except ValueError as e:
            print(f'Incorrect date format {self.ad_actual_until} entered. Exiting')
            sys.exit()


class Event(Record):
    def __str__(self):
        return self.record

    def __init__(self, event_text, event_address, event_datetime):
        self.event_text = event_text
        self.event_address = event_address
        self.event_datetime = event_datetime
        self.current_date = datetime.now()
        self.check_event_datetime()
        date_diff = self.event_datetime - self.current_date
        if date_diff.days < 0:
            print(f"Looks like Event has already performed. Exiting")
            sys.exit()
        self.record = self.header() + '\n' + \
                      self.event_text + '\n' + \
                      f'Where: {self.event_address}' + '\n' + \
                      f'When: {self.event_datetime}' + '\n' + \
                      self.footer()

    def check_event_datetime(self):
        try:
            self.event_datetime = datetime.strptime(self.event_datetime, "%Y-%m-%d %H:%M")
        except ValueError as e:
            print(f'Incorrect date format {self.event_datetime} entered. Exiting')
            sys.exit()


# Reading data from the file part


class FileData:
    def __str__(self):
        return self.text_to_append

    def __init__(self, data, file_type):
        self.file_content = data
        self.text_to_append = ''
        if file_type == 't':
            self.parce_txt_file()
        elif file_type in ('j', 'x'):
            self.parce_list()

    @staticmethod
    def validate_record_type(record_type):
        if record_type not in ('News', 'Privatead', 'PrivateAd', 'Event'):
            print(f'Unsupported self type {record_type} in the file, exiting the program')
            sys.exit()

    @staticmethod
    def normalize_list(record_elements):
        for i in range(len(record_elements)):
            record_elements[i] = normalize_string_case(record_elements[i])
        return record_elements

    @staticmethod
    def add_empty_rows_below(text):
        return text + '\n' + '\n'

    def parce_txt_file(self):
        for row in self.file_content.split('\n'):
            record_elements = self.normalize_list(row.split('; '))
            self.validate_record_type(record_elements[0])
            if record_elements[0] == 'News':
                obj = News(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Privatead':
                obj = PrivateAd(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Event':
                obj = Event(record_elements[1], record_elements[2], record_elements[3])
                self.text_to_append += self.add_empty_rows_below(str(obj))

    def parce_list(self):
        for element in self.file_content:
            try:
                if element['type'] == 'News':
                    obj = News(element['text'], element['city'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
                elif element['type'] == 'Privatead':
                    obj = PrivateAd(element['text'], element['valid_until'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
                elif element['type'] == 'Event':
                    obj = Event(element['text'], element['location'], element['event_date'])
                    self.text_to_append += self.add_empty_rows_below(str(obj))
            except KeyError:
                print("Please, check JSON structure and column names in the source file")
                sys.exit()