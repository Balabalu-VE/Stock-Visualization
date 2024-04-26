import csv
from collections import defaultdict

def filter_csv(input_file, output_file, column_index):
    # Dictionary to store counts of each value in the column
    value_counts = defaultdict(int)
    
    # Read the CSV file and count occurrences of each value in the column
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row
        
        # Find the column index by name if column_index is a string
        if isinstance(column_index, str):
            column_index = header.index(column_index)
        
        # Count occurrences of each value in the column
        for row in reader:
            value = row[column_index]
            value_counts[value] += 1
    
    max_value = max(value_counts.values())

    # Open the output file for writing filtered rows
    with open(output_file, 'w', newline='') as outfile:
        print(max_value)
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header row
        
        # Read the input file again to write filtered rows
        with open(input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header row
            
            # Write rows where the value appears at least three times
            for row in reader:
                value = row[column_index]
                if value_counts[value] >= max_value:
                    writer.writerow(row)

# Example usage
input_file = 'output.csv'
output_file = 'final_stock.csv'
column_index = 'Date'  # Specify the column name or index

filter_csv(input_file, output_file, column_index)



