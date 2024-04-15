import csv
import os

def merge_csv_files(input_folder, output_file):
    # List all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Open the output file in write mode
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header row
        writer.writerow(['StockName', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
        
        # Iterate over each CSV file in the input folder
        for csv_file in csv_files:
            with open(os.path.join(input_folder, csv_file), 'r', newline='') as infile:
                reader = csv.reader(infile)
                
                # Skip header
                next(reader)
                
                # Write rows from the current CSV file to the output file
                for row in reader:
                    # Insert filename without extension as the first column
                    filename_without_extension = os.path.splitext(csv_file)[0]
                    row.insert(0, filename_without_extension)
                    writer.writerow(row)

input_folder = 'Stocks/ETF'
output_file = 'output.csv'

merge_csv_files(input_folder, output_file)
