import csv
import os
import random

def merge_csv_files(input_folders, output_file):
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['StockType', 'StockName', 'Date', 'Close', 'Holdings', "Value"]) 

        for folder_type, folder_path in input_folders.items():
            csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
            for csv_file in csv_files:
                with open(os.path.join(folder_path, csv_file), 'r', newline='') as infile:
                    reader = csv.reader(infile)
                    next(reader)  # Skip header
                    filename_without_extension = os.path.splitext(csv_file)[0]

                    # Generate a random number between 0 and 10 for each unique StockName
                    random_holdings = {filename_without_extension: random.uniform(0, 10)}

                    for row in reader:
                        # Selecting columns StockType, StockName, Date, Close, and Value
                        stock_name = filename_without_extension
                        holdings = random_holdings.get(stock_name, random.uniform(0, 10))
                        value = float(row[4]) * holdings
                        selected_row = [folder_type, stock_name, row[0], row[4], holdings, value]
                        writer.writerow(selected_row)

input_folders = {
    'ETF': 'Stocks/ETF',
    'Stock': 'Stocks/Stock'
}
output_file = 'output.csv'

merge_csv_files(input_folders, output_file)
