from datetime import date, timedelta

import os, csv
import pandas as pd


class Manipulate:
    def get_today_file(self):
        today_date = date.today()
        filetype = '.csv'
        return str(today_date) + filetype

    def get_yesterday_file(self):
        today_date = date.today()
        yesterday_date = today_date - timedelta(days=1)
        filetype = '.csv'
        return str(yesterday_date) + filetype

    def get_data_folder_path(self):
        path = 'data//'
        return path

    def return_diff_yesterday_today(self):
        column = "name"

        yesterday_list = self.get_list_from_csv_column(self.get_data_folder_path() + self.get_yesterday_file(), column)
        today_list = self.get_list_from_csv_column(self.get_data_folder_path() + self.get_today_file(), column)

        # Elements in today but not in yesterday
        difference = list(set(today_list) - set(yesterday_list))
        return difference

    def get_prices_from_list(self, filter_list):
        df = pd.read_csv(self.get_data_folder_path() + self.get_today_file())
        filtered_df = df[df['name'].isin(filter_list)]
        result_df = filtered_df[['name', 'price']]
        return result_df

    def get_list_from_csv_column(self, name: str, column: str):
        df = pd.read_csv(name)
        return df[column].tolist()

    def output_blu_rays(self, blu_ray_all):
        filename = self.get_data_folder_path() + self.get_today_file()
        headers = ["id", "name", "price"]
        print(filename)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            for index, blu_ray in enumerate(blu_ray_all):
                writer.writerow([index, blu_ray.title, blu_ray.price])

    def get_repo_path_from_script(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        return script_dir

    def cleanup_files(self):
        file_today = self.get_today_file()
        file_yesterday = self.get_yesterday_file()
        self.delete_other_csvs(file_today, file_yesterday)

    def delete_other_csvs(self, file1: str, file2: str):
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
