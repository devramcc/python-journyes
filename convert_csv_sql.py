import csv
import sqlite3

# Replace the values in these variables with your own filenames
csv_filename = 'example.csv'
sql_filename = 'example.sql'

# Open the CSV file and read its contents
with open(csv_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row of the CSV file
    header_row = next(csv_reader)

    # Open the SQL file and start writing to it
    with open(sql_filename, 'w') as sql_file:
        # Establish a connection to an SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        # Create a table with the same number of columns as the CSV file
        num_cols = len(header_row)
        create_table_sql = f"CREATE TABLE example ({', '.join(['col{} TEXT'.format(i) for i in range(1, num_cols+1)])})"
        cursor.execute(create_table_sql)

        # Iterate over each row in the CSV file and insert it into the database
        for row in csv_reader:
            insert_sql = f"INSERT INTO example VALUES ({', '.join(['?' for _ in range(num_cols)])})"
            cursor.execute(insert_sql, row)

        # Generate SQL commands to export the data from the SQLite database to an SQL file
        dump_sql = ''.join(conn.iterdump())

        # Write the SQL commands to the SQL file
        sql_file.write(dump_sql)

        # Close the database connection
        conn.close()

print('CSV file converted to SQL file')