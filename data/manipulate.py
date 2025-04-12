import pandas as pd

class Manipulate:
    def read_csv(self):
        df = pd.read_csv('data.csv')
        print(df.to_string())

    def compare_old_new(self):
        yesterday = self.get_list_from_csv_column('data_old.csv', 'name')
        today = self.get_list_from_csv_column('data_new.csv', 'name')

        # Elements in today but not in yesterday
        difference = list(set(today) - set(yesterday))
        print(f"Elements in today but not yesterday: {difference}")

    def get_list_from_csv_column(self, name: str, column: str):
        df = pd.read_csv(name)
        return df[column].tolist()
