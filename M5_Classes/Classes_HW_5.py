import re
import sys
from datetime import datetime


class Publication:
    def __init__(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.current_date = datetime.now()

    def write_to_file(self):
        with open('Newsfeed.txt', 'a') as file:
            file.write(self.record + '\n\n')
        print('New record has successfully added to the file')

    def header(self):
        class_name = self.__class__.__name__
        return f"{class_name} {(30 - len(class_name) - 1) * '-'}"

    def footer(self):
        return f"{30 * '-'}"


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city_name = input("Enter the name of the city with which the news is related: ")
        self.publication_date = datetime.now().strftime("%Y-%m-%d %H.%M")
        self.record = self.header() + '\n' + \
                      self.publication_text + '\n' + \
                      self.city_name.title() + ', ' + \
                      self.publication_date + '\n' + \
                      self.footer()


class PrivateAd(Publication):
    def __init__(self):
        super().__init__()
        self.actual_until \
            = input("Please, enter date until which ad will be actual in format yyyy-mm-dd: ")
        self.get_actual_until_date()
        date_diff = self.actual_until - self.current_date
        if date_diff.days < 0:
            print(f"Looks like ad expired. Ad was not added. Try again, pay attention to date format")
            sys.exit()
        self.record = self.header() + '\n' + self.publication_text + '\n' + f'Actual until: ' + str(
            self.actual_until.strftime('%Y-%m-%d')) + ',' + f' {date_diff.days} days left' + '\n' + self.footer()

    def get_actual_until_date(self):
        try:
            self.actual_until = datetime.strptime(self.actual_until, '%Y-%m-%d')
        except ValueError as e:
            self.actual_until = input('Incorrect date format entered. Please, '
                                      'try again and follow date format pattern (yyyy-mm-dd): ')
            if "exit" != self.actual_until:
                self.get_actual_until_date()
            else:
                sys.exit()


class Event(Publication):
    def __init__(self):
        super().__init__()
        self.event_address = input("Enter address where event will be performed: ")
        self.event_datetime = input("Please, enter date and time when event will be performed "
                                    "in format (yyyy-mm-dd hh:mm): ")
        self.get_event_datetime()
        date_diff = self.event_datetime - self.current_date
        if date_diff.days < 0:
            print(f"Looks like Event has already performed. Event was not added. Try again, pay attention to Event date")
            sys.exit()
        self.record = self.header() + '\n' + \
                      self.publication_text + '\n' + \
                      f'Where: {self.event_address}' + '\n' + \
                      f'When: {self.event_datetime}' + '\n' + \
                      self.footer()

    def get_event_datetime(self):
        try:
            self.event_datetime = datetime.strptime(self.event_datetime, "%Y-%m-%d %H:%M")
        except ValueError as e:
            self.event_datetime = input('Incorrect date format entered. Please, '
                                        'try again and follow date format pattern (yyyy-mm-dd hh:mm): ')
            if "exit" != self.event_datetime:
                self.get_event_datetime()
            else:
                sys.exit()


def main():
    while True:
        try:
            user_input = int(input("Enter number from 1 to 3 to define type of publication which you want to add.\n"
                                   "1 for News, 2 for Private Advertisement, 3 for Event announcement: "))
            if user_input == 1:
                News().write_to_file()
            elif user_input == 2:
                PrivateAd().write_to_file()
            elif user_input == 3:
                Event().write_to_file()
            elif user_input < 1 or user_input > 3:
                raise ValueError
        except ValueError:
            print(f'Incorrect input! Please enter number from 1 to 3 for desired publication type:\n'
                  f'1 if you want to add News\n'
                  f'2 if you want to add Privat Advertisement\n'
                  f'3 if you want to add Event')
        else:
            break


main()
