import csv
import os

def merge_csv_files(input_folder_etf, input_folder_stocks, output_file):
    # List all CSV files in the input folder
    csv_files_etf = [f for f in os.listdir(input_folder_etf) if f.endswith('.csv')]
    csv_files_stocks = [f for f in os.listdir(input_folder_stocks) if f.endswith('.csv')]

    # Open the output file in write mode
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header row
        writer.writerow(['StockType', 'StockName', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
        
        # Iterate over each CSV file in the input folder for ETFs
        for csv_file in csv_files_etf:
            with open(os.path.join(input_folder_etf, csv_file), 'r', newline='') as infile:
                reader = csv.reader(infile)
                
                # Skip header
                next(reader)

                # Write rows from the current CSV file to the output file
                for row in reader:
                    # Insert filename without extension as the first column
                    row.insert(0, "ETF")
                    filename_without_extension = os.path.splitext(csv_file)[0]
                    row.insert(1, filename_without_extension)
                    writer.writerow(row)
         # Iterate over each CSV file in the input folder for stocks
        for csv_file in csv_files_stocks:
            with open(os.path.join(input_folder_stocks, csv_file), 'r', newline='') as infile:
                reader = csv.reader(infile)
                
                # Skip header
                next(reader)

                # Write rows from the current CSV file to the output file
                for row in reader:
                    # Insert filename without extension as the first column
                    row.insert(0, "Stock")
                    filename_without_extension = os.path.splitext(csv_file)[0]
                    row.insert(1, filename_without_extension)
                    writer.writerow(row)
    

input_folder_etf = 'Stocks/ETF'
input_folder_stocks = 'Stocks/Stock'
output_file = 'output.csv'

merge_csv_files(input_folder_etf, input_folder_stocks, output_file)
