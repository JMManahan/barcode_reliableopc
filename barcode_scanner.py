import sqlite3

def lookup_barcode(barcode):
    # Connect to the SQLite database
    conn = sqlite3.connect('barcode_data.db')
    c = conn.cursor()

    # Query the database for the barcode
    c.execute("SELECT * FROM barcodes WHERE id=?", (barcode,))
    result = c.fetchone()

    # Close the connection
    conn.close()

    # Display the result
    if result:
        print(f"ID: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Department: {result[2]}")
        print(f"Position: {result[3]}")
    else:
        print("No information found.")

def main():
    print("Please scan a barcode (input the ID): ")
    scanned_barcode = input()  # Assume the user scans the barcode and inputs it
    lookup_barcode(scanned_barcode)

if __name__ == "__main__":
    main()
