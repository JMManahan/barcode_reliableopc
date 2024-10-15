import sqlite3

# Connect to the SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect('barcode_data.db')
c = conn.cursor()

# Create the table for barcodes
c.execute('''
    CREATE TABLE IF NOT EXISTS barcodes (
        id TEXT PRIMARY KEY,
        name TEXT,
        department TEXT,
        position TEXT
    )
''')

# Insert example data
sample_data = [
    ('85783', 'John Doe', 'Marketing', 'Manager'),
    ('12345', 'Jane Smith', 'Sales', 'Executive'),
    ('67890', 'Alice Johnson', 'IT', 'Developer')
]

# Insert sample data into the database
c.executemany("INSERT OR IGNORE INTO barcodes (id, name, department, position) VALUES (?, ?, ?, ?)", sample_data)
conn.commit()

# Close the connection
conn.close()

print("Database created and sample data inserted.")
