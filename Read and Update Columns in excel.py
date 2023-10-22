import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'EmployeeDetails.csv'

# Read the CSV file using pandas
data_frame = pd.read_csv(csv_file_path)

# Get the headers (column names) from the DataFrame
headers = data_frame.columns.tolist()

print ("the headers are after List: ",headers)

# Print the headers
for header in headers:
    print(header)

# Count the number of rows (excluding the header)
num_rows = len(data_frame) - 1  # Subtract 1 for the header

print("Number of rows excluding header:", num_rows)

# Update Grade column based on Number of employees
data_frame.loc[data_frame['Number of employees'] > 5000, 'Grade'] = 1
data_frame.loc[(data_frame['Number of employees'] > 1000) & (data_frame['Number of employees'] <= 5000), 'Grade'] = 2

# Save the updated DataFrame back to the CSV file
data_frame.to_csv(csv_file_path, index=False)

