
# init-scripts/init_sample_data.py

import sys
sys.path.insert(0, '../src')

from data_insertion import create_table_from_csv

# Specify the path to the CSV file
csv_file_path = "./sample_data_5_Add_Mat_Extrusion_FFF.csv"

# Specify the name of the table to be created
table_name = "sample_data_5_Add_Mat_Extrusion_FFF"

# Call the function to create the table from the CSV file
create_table_from_csv(csv_file_path, table_name)
