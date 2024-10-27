import mysql.connector


# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root1",
        password="Lakshita21",
        database="student_management"
    )


# User registration
def register_user(username, password):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("User registered successfully!")
    except mysql.connector.IntegrityError:
        print("Username already exists!")
    finally:
        cursor.close()
        db.close()


# User login
def login_user(username, password):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result and result[0] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


# Create a new student
def create_student(name, age, grade):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    db.commit()
    cursor.close()
    db.close()
    print("Student added successfully!")


# Read all students
def read_students():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    cursor.close()
    db.close()

    if results:
        print("ID\tName\tAge\tGrade")
        for row in results:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    else:
        print("No students found.")


# Update a student's information
def update_student(student_id, name, age, grade):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s", (name, age, grade, student_id))
    db.commit()
    cursor.close()
    db.close()
    print("Student updated successfully!")


# Delete a student
def delete_student(student_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    db.commit()
    cursor.close()
    db.close()
    print("Student deleted successfully!")


# Main menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_user(username, password):
                # If login is successful, show student management options
                while True:
                    print("\n--- Student Management ---")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Update Student")
                    print("4. Delete Student")
                    print("5. Logout")

                    student_choice = input("Enter your choice: ")

                    if student_choice == '1':
                        name = input("Enter name: ")
                        age = int(input("Enter age: "))
                        grade = input("Enter grade: ")
                        create_student(name, age, grade)
                    elif student_choice == '2':
                        read_students()
                    elif student_choice == '3':
                        student_id = int(input("Enter student ID to update: "))
                        name = input("Enter new name: ")
                        age = int(input("Enter new age: "))
                        grade = input("Enter new grade: ")
                        update_student(student_id, name, age, grade)
                    elif student_choice == '4':
                        student_id = int(input("Enter student ID to delete: "))
                        delete_student(student_id)
                    elif student_choice == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
