import sqlite3 as sqlite

# Connect to the SQLite database
con = sqlite.connect('report_data.db')
cursor = con.cursor()

# Execute the SQL query to select all rows from the 'report_data' table
cursor.execute("SELECT * FROM report_data")


# Retrieve the result and print 
print(*list(cursor), sep='\n')

