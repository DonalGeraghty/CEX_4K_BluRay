import pandas as pd

class Data:
    def read_csv(self):
        df = pd.read_csv('data.csv')
        print(df.to_string())