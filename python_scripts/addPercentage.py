import csv
from collections import defaultdict

def add_percent_change_column(input_file, output_file, column_name):
    # Dictionary to store the first value for each StockName
    first_values = defaultdict(float)
    unique_stock_names = set()


    # Read the CSV file and calculate percent change
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader2 = csv.DictReader(infile)
        for row in reader2:
            stock_name = row['StockName']
            unique_stock_names.add(stock_name)

    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['PercentChange']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            stock_name = row['StockName']
            close_value = float(row[column_name])

            # Check if it's the first occurrence of StockName
            if stock_name not in first_values:
                first_values[stock_name] = close_value
                percent_change = 0
            else:
                first_value = first_values[stock_name]
                percent_change = ((close_value - first_value) / first_value) * 100/len(unique_stock_names)

            # Add the percent change to the row
            row['PercentChange'] = percent_change + 100/len(unique_stock_names)

            # Write the row to the output file
            writer.writerow(row)
        
# Example usage
input_file = 'final_stock.csv'
output_file = 'final_stock_percent_change.csv'
column_name = 'Close'  # Specify the column name for which you want to calculate percent change

add_percent_change_column(input_file, output_file, column_name)
