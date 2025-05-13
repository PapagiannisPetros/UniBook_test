import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        # Get the absolute path to the DB file
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "database", "unibook.db")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # To get dict-like rows
        self.cursor = self.conn.cursor()
        
    def get_all_courses(self):
        self.cursor.execute("SELECT course_id, course_name FROM Course")
        return self.cursor.fetchall()

        
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE User (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                username VARCHAR(20) UNIQUE NOT NULL,
                password VARCHAR(30) NOT NULL
            );
        ''')

        self.cursor.execute('''
           CREATE TABLE Student (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_id INTEGER UNIQUE NOT NULL,
                am INTEGER UNIQUE NOT NULL,
                university VARCHAR(30),
                department VARCHAR(20),
                enrollment_year INTEGER,
                FOREIGN KEY(user_id) REFERENCES User(id)
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_id INTEGER UNIQUE NOT NULL,
                name VARCHAR,
                FOREIGN KEY(user_id) REFERENCES User(id)
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Profile (
                profile_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                am INTEGER UNIQUE NOT NULL,
                name VARCHAR(50),
                email VARCHAR(50),
                birth_date DATE,
                gender TEXT,
                address VARCHAR(50),
                tel_num INTEGER,
                bio VARCHAR(200),
                FOREIGN KEY(am) REFERENCES Student(am)
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Course (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                course_name VARCHAR(30),
                semester INTEGER
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Post (
                post_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                course_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                FOREIGN KEY(course_id) REFERENCES Course(course_id),
                FOREIGN KEY(student_id) REFERENCES Student(student_id)
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Subscription (
                subscription_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                profile_id INTEGER,
                subscription_type TEXT,
                start_date DATE,
                end_date DATE,
                FOREIGN KEY(profile_id) REFERENCES Profile(profile_id)
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE Comment (
                comment_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                author_id INTEGER NOT NULL,
                comment_text VARCHAR(255),
                upload_time DATETIME,
                post_id INTEGER NOT NULL,
                FOREIGN KEY(author_id) REFERENCES Student(student_id),
                FOREIGN KEY(post_id) REFERENCES Post(post_id)
            );
        ''')
        
        self.cursor.execute('''
            CREATE TABLE Chat (
                chat_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                course_id INTEGER NOT NULL,
                FOREIGN KEY(course_id) REFERENCES Course(course_id)
            );
        ''')
        
        self.cursor.execute('''
            CREATE TABLE Message (
                message_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                chat_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                message_text TEXT,
                send_time DATETIME,
                FOREIGN KEY(chat_id) REFERENCES Chat(chat_id),
                FOREIGN KEY(student_id) REFERENCES Student(student_id)
            );
        ''')
        
        self.cursor.execute('''
           CREATE TABLE Report (
                report_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                post_id INTEGER NOT NULL,
                reporter_id INTEGER NOT NULL,
                report_type TEXT,
                status TEXT,
                comment_text TEXT,
                report_time DATE,
                FOREIGN KEY(post_id) REFERENCES Post(post_id),
                FOREIGN KEY(reporter_id) REFERENCES Student(student_id)
            );
        ''')

        self.conn.commit()
        
    def insert_sample_data(self):
        try:
            # Insert into User
            self.cursor.execute('''
                INSERT INTO User (username, password) VALUES (?, ?)
            ''', ('jdoe', 'securepassword123'))

            # Insert into Student
            self.cursor.execute('''
                INSERT INTO Student (user_id, am, university, department, enrollment_year)
                VALUES (?, ?, ?, ?, ?)
            ''', (1, 1001, 'Example University', 'Computer Science', 2021))

            # Insert into Admin
            self.cursor.execute('''
                INSERT INTO Admin (user_id, name) VALUES (?, ?)
            ''', (1, 'John Doe'))

            # Insert into Profile
            self.cursor.execute('''
                INSERT INTO Profile (am, name, email, birth_date, gender, address, tel_num, bio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1001, 'John Doe', 'jdoe@example.com', '2000-01-01', 'Male',
                '123 Main St', 1234567890, 'Hello, I\'m John.'))

            # Insert into Course
            self.cursor.execute('''
                INSERT INTO Course (course_name, semester) VALUES (?, ?)
            ''', ('Introduction to Databases', 2))

            # Insert into Post
            self.cursor.execute('''
                INSERT INTO Post (course_id, student_id) VALUES (?, ?)
            ''', (1, 1))

            # Insert into Subscription
            self.cursor.execute('''
                INSERT INTO Subscription (profile_id, subscription_type, start_date, end_date)
                VALUES (?, ?, ?, ?)
            ''', (1, 'Premium', '2025-01-01', '2025-12-31'))

            # Insert into Comment
            self.cursor.execute('''
                INSERT INTO Comment (author_id, comment_text, upload_time, post_id)
                VALUES (?, ?, ?, ?)
            ''', (1, 'This is a sample comment.', '2025-05-10 10:00:00', 1))

            # Insert into Chat
            self.cursor.execute('''
                INSERT INTO Chat (course_id) VALUES (?)
            ''', (1,))

            # Insert into Message
            self.cursor.execute('''
                INSERT INTO Message (chat_id, student_id, message_text, send_time)
                VALUES (?, ?, ?, ?)
            ''', (1, 1, 'Hello everyone!', '2025-05-10 10:05:00'))

            # Insert into Report
            self.cursor.execute('''
                INSERT INTO Report (post_id, reporter_id, report_type, status, comment_text, report_time)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (1, 1, 'Spam', 'Open', 'This post looks like spam.', '2025-05-10'))

            self.conn.commit()
            print("Sample data inserted successfully.")

        except sqlite3.IntegrityError as e:
            print("Integrity error:", e)
        except Exception as e:
            print("An error occurred:", e)


    def close(self):
        self.conn.close()