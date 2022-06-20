import pyodbc

config_path = 'C:\Git\Python for DQE\M10_Database_API\config.ini'


class DB:
    def __init__(self, row, news_type):
        self.row = row
        self.news_type = news_type
        self.connection = pyodbc.connect(config_path)
        self.tables_metadata = ['News', "text", "city", "publication_time"], \
                               ['PrivateAd', "text", "valid_until", "days_left"], \
                               ['Event', "text", "event_location", "event_date"]
        self.create_tables()
        self.write_row_to_table()

    def create_tables(self):
        for table_metadata in self.tables_metadata:
            with self.connection as connection:
                cursor = connection.cursor()
                cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_metadata[0]} '
                               f'{table_metadata[1], table_metadata[2]};')

    def write_row_to_table(self):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(f'WITH cte(c1, c2, c3) AS (SELECT * FROM {self.news_type}) '
                           f'SELECT * FROM cte WHERE c1 = \'{self.row[0]}\' '
                           f'AND c2 = \'{self.row[1]}\' '
                           f'AND c3 = \'{self.row[2]}\' ')
            row_num = cursor.fetchone()
            if row_num is not None:
                print(f'Duplicated row in table {self.news_type} with values'
                      f'\'{self.row[0]}\', \'{self.row[1]}\', \'{self.row[2]}\'')
            else:
                cursor.execute(f'INSERT INTO {self.news_type} VALUES (\'{self.row[0]}\''
                               f',\'{self.row[1]}\''
                               f',\'{self.row[2]}\');')
                self.connection.commit()


DB()

