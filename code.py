import mysql.connector as sql

# Database Connection
try:
    conn = sql.connect(host='localhost', user='root', passwd='root', database='book_shop')
    cur = conn.cursor()
except sql.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# Main Menu Function
def main_menu():
    print("\n📚 BOOK SHOP SYSTEM")
    print("1. Add")
    print("2. Display")
    print("3. Delete")
    print("4. Update")
    print("5. Exit")

while True:
    main_menu()
    try:
        choice = int(input("Enter your choice: "))
        
        # 1️⃣ ADD ENTRY
        if choice == 1:
            print("\n1. Entry for Books\n2. Entry for Customer")
            choose = int(input("Enter the choice for entry: "))

            if choose == 1:  # Add Book
                s_no = input("Enter serial number: ")
                book_name = input("Enter book name: ")
                availability = int(input("Enter availability: "))
                price = int(input("Enter price: "))
                
                cur.execute("INSERT INTO Books (s_no, book_name, availability_of_book, price) VALUES (%s, %s, %s, %s)",
                            (s_no, book_name, availability, price))
                conn.commit()
                print("✅ Book entry successful!")
            
            elif choose == 2:  # Add Customer
                name = input("Enter customer name: ")
                age = int(input("Enter age: "))
                place = input("Enter place: ")
                book_name = input("Enter book bought: ")

                # Check availability
                cur.execute("SELECT availability_of_book FROM Books WHERE book_name = %s", (book_name,))
                row = cur.fetchone()
                if row:
                    available_qty = row[0]
                    if available_qty > 0:
                        cur.execute("UPDATE Books SET availability_of_book = availability_of_book - 1 WHERE book_name = %s", (book_name,))
                        cur.execute("INSERT INTO customer (customer_name, age, place, book_bought) VALUES (%s, %s, %s, %s)",
                                    (name, age, place, book_name))
                        conn.commit()
                        print("✅ Customer entry successful!")
                    else:
                        print("❌ Book not available!")
                else:
                    print("❌ Book not found!")

        # 2️⃣ DISPLAY ENTRIES
        elif choice == 2:
            print("\n1. Display Books List\n2. Display Customer List")
            ch = int(input("Enter your choice: "))

            if ch == 1:  # Display Books
                cur.execute("SELECT * FROM Books")
                books = cur.fetchall()
                print("\n📖 List of Books:")
                for row in books:
                    print(f"S.No: {row[0]}, Name: {row[1]}, Available: {row[2]}, Price: ₹{row[3]}")
            
            elif ch == 2:  # Display Customers
                cur.execute("SELECT * FROM customer")
                customers = cur.fetchall()
                print("\n👤 List of Customers:")
                for row in customers:
                    print(f"Name: {row[0]}, Age: {row[1]}, Place: {row[2]}, Book Bought: {row[3]}")

        # 3️⃣ DELETE ENTRY
        elif choice == 3:
            print("\n1. Delete Book Entry\n2. Delete Customer Entry")
            choose = int(input("Enter your choice: "))

            if choose == 1:  # Delete Book
                book_name = input("Enter book name to delete: ")
                cur.execute("DELETE FROM Books WHERE book_name = %s", (book_name,))
                conn.commit()
                print("✅ Book deleted successfully!")

            elif choose == 2:  # Delete Customer
                name = input("Enter customer name to delete: ")
                cur.execute("DELETE FROM customer WHERE customer_name = %s", (name,))
                conn.commit()
                print("✅ Customer deleted successfully!")

        # 4️⃣ UPDATE ENTRY
        elif choice == 4:
            print("\n1. Update Book Availability\n2. Update Customer Details")
            choose = int(input("Enter your choice: "))

            if choose == 1:  # Update Book
                book_name = input("Enter book name to update: ")
                new_qty = int(input("Enter new availability: "))
                cur.execute("UPDATE Books SET availability_of_book = %s WHERE book_name = %s", (new_qty, book_name))
                conn.commit()
                print("✅ Book availability updated!")

            elif choose == 2:  # Update Customer
                name = input("Enter customer name to update: ")
                new_book = input("Enter new book bought: ")
                cur.execute("UPDATE customer SET book_bought = %s WHERE customer_name = %s", (new_book, name))
                conn.commit()
                print("✅ Customer details updated!")

        # 5️⃣ EXIT
        elif choice == 5:
            print("Exiting... 👋")
            conn.close()
            break
        
        else:
            print("❌ Invalid Choice! Try again.")

    except ValueError:
        print("❌ Please enter a valid number!")
    except sql.Error as e:
        print(f"❌ MySQL Error: {e}")
