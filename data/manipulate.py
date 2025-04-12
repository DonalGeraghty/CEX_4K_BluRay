import os
from datetime import date, timedelta

import csv
import pandas as pd

class Manipulate:
    def read_csv(self, filename: str, filetype: str):
        df = pd.read_csv(filename + filetype)
        print(df.to_string())

    def compare_old_new(self):
        folder = 'data' + '//'
        filetype = '.csv'
        column = 'name'

        today_date = date.today()
        yesterday_date = today_date - timedelta(days=1)

        yesterday = self.get_list_from_csv_column(folder + str(yesterday_date) + filetype, column)
        today = self.get_list_from_csv_column(folder + str(today_date) + filetype, column)

        # Elements in today but not in yesterday
        difference = list(set(today) - set(yesterday))
        for index, ele in enumerate(difference):
            print(str(index) + " " + ele)

    def get_list_from_csv_column(self, name: str, column: str):
        df = pd.read_csv(name)
        return df[column].tolist()

    def output_blu_rays(self, blu_ray_all):
        filename = 'data' + '//' + str(date.today()) + '.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["id", "name", "price"])
            for index, blu_ray in enumerate(blu_ray_all):
                writer.writerow([index, blu_ray.title, blu_ray.price])

    def get_repo_path_from_script(self):
        """Gets the directory of the current Python script."""
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        return script_dir

    def delete_other_csvs(self, file1: str, file2: str):
        """Deletes all CSV files in a folder except for 'data1.csv' and 'data2.csv'.

        Args:
            folder_path (str): The path to the folder containing the CSV files.
        """
        folder_path = self.get_repo_path_from_script()
        print(folder_path)
        try:
            for filename in os.listdir(folder_path):
                if filename.endswith(".csv") and filename not in [file1, file2]:
                    file_path = os.path.join(folder_path, filename)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            print("Finished checking and deleting CSV files.")
        except FileNotFoundError:
            print(f"Error: Folder not found at '{folder_path}'")
        except Exception as e:
            print(f"An error occurred: {e}")