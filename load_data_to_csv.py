"""
Script to load data from json file, help visualize it with pandas library and save data to csv file for easier usage
with pyspark
"""
import json
import pandas as pd

json_file = 'data_gr_A.json'
save_csv_file = 'data_gr_A_csv.csv'


def main():

    with open(json_file, encoding="utf8") as file:
        decoded_data = json.load(file)

    pandas_data = pd.DataFrame(decoded_data['data'], columns=decoded_data['cols'])
    print(pandas_data.to_string(index=False))

    # Saving data to csv file
    pandas_data.to_csv(save_csv_file)


if __name__ == '__main__':
    main()
