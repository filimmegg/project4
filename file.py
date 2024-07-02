import sqlite3

def connect():
    return sqlite3.connect('filmflix.db')

def add_record():
    title = input("Enter film title: ")
    year = int(input("Enter year released: "))
    rating = input("Enter rating: ")
    duration = int(input("Enter duration (in minutes): "))
    genre = input("Enter genre: ")
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, year, rating, duration, genre))
    conn.commit()
    conn.close()
    print("Record added successfully.")

def delete_record():
    film_id = int(input("Enter film ID to delete: "))
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tblfilms WHERE filmID = ?
    ''', (film_id,))
    conn.commit()
    conn.close()
    print("Record deleted successfully.")

def amend_record():
    film_id = int(input("Enter film ID to amend: "))
    title = input("Enter new film title: ")
    year = int(input("Enter new year released: "))
    rating = input("Enter new rating: ")
    duration = int(input("Enter new duration (in minutes): "))
    genre = input("Enter new genre: ")
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tblfilms
        SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?
        WHERE filmID = ?
    ''', (title, year, rating, duration, genre, film_id))
    conn.commit()
    conn.close()
    print("Record amended successfully.")

def print_all_records():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms')
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def print_by_genre():
    genre = input("Enter genre to filter by: ")
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms WHERE genre = ?', (genre,))
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def print_by_year():
    year = int(input("Enter year to filter by: "))
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms WHERE yearReleased = ?', (year,))
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def print_by_rating():
    rating = input("Enter rating to filter by: ")
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tblfilms WHERE rating = ?', (rating,))
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def crud_menu():
    while True:
        print("\nCRUD Menu")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Amend a record")
        print("4. Print all records")
        print("5. Exit")
        
        choice = int(input("Select an option: "))
        
        if choice == 1:
            add_record()
        elif choice == 2:
            delete_record()
        elif choice == 3:
            amend_record()
        elif choice == 4:
            print_all_records()
        elif choice == 5:
            break
        else:
            print("Invalid option. Please try again.")

def report_menu():
    while True:
        print("\nReport Menu")
        print("1. Print details of all films")
        print("2. Print all films of a particular genre")
        print("3. Print all films of a particular year")
        print("4. Print all films of a particular rating")
        print("5. Exit")
        
        choice = int(input("Select an option: "))
        
        if choice == 1:
            print_all_records()
        elif choice == 2:
            print_by_genre()
        elif choice == 3:
            print_by_year()
        elif choice == 4:
            print_by_rating()
        elif choice == 5:
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. CRUD Operations")
        print("2. Reports")
        print("3. Exit")
        
        choice = int(input("Select an option: "))
        
        if choice == 1:
            crud_menu()
        elif choice == 2:
            report_menu()
        elif choice == 3:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
