import sqlite3
import os
from models import Course, Post, Admin, Student, Chat, Message, Comment, Profile, Report
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        # Get the absolute path to the DB file
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "database", "unibook.db")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # To get dict-like rows
        self.cursor = self.conn.cursor()
        self.admins = []
        self.student =  None 
        pass
    def get_students_posts_by_student_id(self, student_id):
        self.cursor.execute("""
            SELECT post_id, course_id, student_id, title, description, date, likes, comments, post_file, file_name, date
            FROM Post
            WHERE student_id = ?
            ORDER BY date DESC
        """, (student_id,))
        
        rows = self.cursor.fetchall()

        posts = []
        for row in rows:
            post = Post(
                post_id=row[0],
                course_id=row[1],
                student_id=row[2],
                title=row[3],
                description=row[4],
                date=row[5],
                likes=row[6],
                comments=row[7],
                post_file=row[8],  # Include PDF as binary
                file_name=row[9]  # Include file name
            )
            posts.append(post)
        
        return posts

    
    def querySaveComment(self, comment_text):
        if not self.current_post:
            return

        post_id = self.current_post.post_id
        student_id = self.logged_in_student.student_id
        send_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.db.insert_comment(post_id, student_id, comment_text, send_time)

        # Refresh comments cache
        comments = self.db.get_comments_by_post_id(post_id)
        self.comments_cache[post_id] = comments
        self.displayComments(comments)
        
    def insert_comment(self, post_id, author_id, comment_text, upload_time):
        self.cursor.execute('''
            INSERT INTO Comment (post_id, author_id, comment_text, upload_time)
            VALUES (?, ?, ?, ?)
        ''', (post_id, author_id, comment_text, upload_time))
        self.conn.commit()
    
    def get_comments_by_post_id(self, post_id):
        self.cursor.execute('''
            SELECT comment_id, author_id, comment_text, upload_time, post_id
            FROM Comment
            WHERE post_id = ?
            ORDER BY upload_time ASC
        ''', (post_id,))
        
        rows = self.cursor.fetchall()
        return [Comment(*row) for row in rows]
    
    def insert_message(self, message):
        self.cursor.execute('''
            INSERT INTO Message (chat_id, student_id, message_text, send_time)
            VALUES (?, ?, ?, ?)
        ''', (message.chat_id, message.student_id, message.message_text, message.send_time))
        self.conn.commit()

    
    def get_or_create_chat_by_course_id(self, course_id):
        self.cursor.execute("SELECT * FROM Chat WHERE course_id = ?", (course_id,))
        row = self.cursor.fetchone()

        if row:
            return Chat(chat_id=row[0], course_id=row[1])
        
        # Chat does not exist; create it
        self.cursor.execute("INSERT INTO Chat (course_id) VALUES (?)", (course_id,))
        self.connection.commit()

        chat_id = self.cursor.lastrowid
        return Chat(chat_id=chat_id, course_id=course_id)


    def get_messages_by_chat_id(self, chat_id):
        self.cursor.execute('''
            SELECT message_id, chat_id, student_id, message_text, send_time
            FROM Message WHERE chat_id = ?
            ORDER BY send_time ASC
        ''', (chat_id,))
        rows = self.cursor.fetchall()
        return [Message(*row) for row in rows]

    
    def create_post(self, course_id, student_id, title, description, date, likes, comments, post_file, file_name):
        try:
            self.cursor.execute('''
                INSERT INTO Post (
                    course_id, student_id, title, description, date, likes, comments, post_file, file_name, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (course_id, student_id, title, description, date, likes, comments, post_file, file_name, "Not Uploaded"))
            self.conn.commit()
            print("Post inserted successfully.")
        except Exception as e:
            print("Error inserting post:", e)
    
    def get_subscription_type_by_student_id(self, student_id):
        print(f"[DEBUG] Querying subscription type for student_id: {student_id}")

        self.cursor.execute('''
            SELECT Subscription.subscription_type
            FROM Student
            JOIN Subscription ON Student.subscription_id = Subscription.subscription_id
            WHERE Student.student_id = ?
        ''', (student_id,))
        
        result = self.cursor.fetchone()
        
        if result:
            print(f"[DEBUG] Subscription type found: {result[0]}")
            return result[0]
        else:
            print("[DEBUG] No subscription type found for the given student_id.")
            return None
    
    def get_all_courses(self):
        self.cursor.execute("SELECT * FROM Course")
        courses = []
        for row in self.cursor.fetchall():
            course = Course(row["course_id"], row["course_name"], row["semester"])
            courses.append(course)
        return courses

    def get_posts_by_course(self, course_id):
        self.cursor.execute('''
            SELECT post_id, course_id, student_id, title, description, date, likes, comments, post_file, file_name
            FROM Post
            WHERE course_id = ? AND status = 'Uploaded'
        ''', (course_id,))
        rows = self.cursor.fetchall()

        posts = []
        for row in rows:
            post = Post(
                post_id=row[0],
                course_id=row[1],
                student_id=row[2],
                title=row[3],
                description=row[4],
                date=row[5],
                likes=row[6],
                comments=row[7],
                post_file=row[8],  # Include PDF as binary
                file_name=row[9]  # Include file name
            )
            posts.append(post)

        return posts

    def get_not_uploaded_posts_by_course(self, course_id):
        self.cursor.execute('''
            SELECT post_id, course_id, student_id, title, description, date, likes, comments, post_file, file_name
            FROM Post
            WHERE course_id = ? AND status = 'Not Uploaded'
        ''', (course_id,))
        rows = self.cursor.fetchall()

        posts = []
        for row in rows:
            post = Post(
                post_id=row[0],
                course_id=row[1],
                student_id=row[2],
                title=row[3],
                description=row[4],
                date=row[5],
                likes=row[6],
                comments=row[7],
                post_file=row[8],  # Include PDF as binary
                file_name=row[9]  # Include file name
            )
            posts.append(post)

        return posts
        
    def getReports(self):
        self.cursor.execute('''
            SELECT report_id, post_id, reporter_id, report_type, status, report_time
            FROM Report
            WHERE status = 'Not Checked'
        ''')
        rows = self.cursor.fetchall()

        reports = []
        for row in rows:
            report = Report(
                report_id=row[0],
                post_id=row[1],
                reporter_id=row[2],
                report_type=row[3],
                status=row[4],
                report_time=row[5]
            )
            reports.append(report)

        return reports
    
    def get_post_by_id(self, post_id):
        self.cursor.execute('''
            SELECT * FROM Post WHERE post_id = ?
        ''', (post_id,))
        row = self.cursor.fetchone()

        if row:
            post = Post(
                post_id=row["post_id"],
                course_id=row["course_id"],
                student_id=row["student_id"],
                title=row["title"],
                description=row["description"],
                date=row["date"],
                likes=row["likes"],
                comments=row["comments"],
                post_file=row["post_file"],
                file_name=row["file_name"]
            )
            return post
    
    def save_report(self, post_id, reporter_id, report_type, status, report_time):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Report (post_id, reporter_id, report_type, status, report_time)
            VALUES (?, ?, ?, ?, ?)
        """, (post_id, reporter_id, report_type, status, report_time))
        self.conn.commit()

    def is_valid_student(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM User u JOIN Student s ON u.id = s.user_id WHERE u.username = ? AND u.password = ?', (username, password))
        result = cursor.fetchone()

        if result:
            new_student = Student(result["student_id"],result["user_id"],result["subscription_id"],result["am"],result["university"],result["department"],result["enrollment_year"])
            self.student = new_student

        return result is not None

    def is_valid_admin(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM User u JOIN Admin a ON u.id = a.user_id WHERE u.username = ? AND u.password = ?', (username, password))
        result = cursor.fetchone()

        if result:
            new_admin = Admin(result["id"],result["user_id"],result["name"])
            self.admins.append(new_admin)

        return result is not None
    
    def uploadPost(self, post_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Post SET status = 'Uploaded' WHERE post_id = ?", (post_id,))
        self.conn.commit()  

        return True 

        
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
                subscription_id INTEGER UNIQUE NOT NULL,
                am INTEGER UNIQUE NOT NULL,
                university VARCHAR(30),
                department VARCHAR(20),
                enrollment_year INTEGER,
                FOREIGN KEY(user_id) REFERENCES User(id),
                FOREIGN KEY(subscription_id) REFERENCES Subscription(subscription_id)
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
                title VARCHAR(50),
                description TEXT,
                date DATETIME,
                likes INTEGER NOT NULL,
                comments INTEGER NOT NULL,
                post_file BLOB,
                file_name TEXT,
                status TEXT,
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

            self.cursor.execute('''
                INSERT INTO User (username, password) VALUES (?, ?)
            ''', ('kef', 'argie'))

            self.cursor.execute('''
                INSERT INTO User (username, password) VALUES (?, ?)
            ''', ('mitro', 'vag'))

            # Insert into Student
            self.cursor.execute('''
                INSERT INTO Student (user_id, subscription_id, am, university, department, enrollment_year)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (1, 1, 1001, 'Example University', 'Computer Science', 2021))

            self.cursor.execute('''
                INSERT INTO Student (user_id, subscription_id, am, university, department, enrollment_year)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (2, 2, 1010, 'Legen University', 'Computer Engineering', 2022))


            # Insert into Admin
            self.cursor.execute('''
                INSERT INTO Admin (user_id, name) VALUES (?, ?)
            ''', (1, 'John Doe'))

            self.cursor.execute('''
                INSERT INTO Admin (user_id, name) VALUES (?, ?)
            ''', (3, 'Vaggelis Mitrogiannis'))

            # Insert into Profile
            self.cursor.execute('''
                INSERT INTO Profile (am, name, email, birth_date, gender, address, tel_num, bio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1001, 'John Doe', 'jdoe@example.com', '2000-01-01', 'Male',
                '123 Main St', 1234567890, 'Hello, I\'m John.'))
            
            self.cursor.execute('''
                INSERT INTO Profile (am, name, email, birth_date, gender, address, tel_num, bio)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1010, 'Argiris Kefalonitis', 'gigikef@example.com', '2004-12-01', 'Male',
                'Kanakari Roufa 16', 6987878787, 'Hello, I\'m Kef.'))

            # Insert into Course
            self.cursor.execute('''
                INSERT INTO Course (course_name, semester) VALUES (?, ?)
            ''', ('Introduction to Databases', 2))

            with open("Robustness-diagram-v0.1.pdf", "rb") as file:
                pdf_data = file.read()
            
            # Insert into Post
            self.cursor.execute('''
                INSERT INTO Post (course_id, student_id, title, description, date, likes, comments, post_file, file_name, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1, 1, 'Sample Not Uploaded Post Title', 'This is a sample post text.', '2025-05-10 10:00:00', 5, 55, pdf_data, 'Robustness-diagram-v0.1.pdf', 'Not Uploaded'))

            self.cursor.execute('''
                INSERT INTO Post (course_id, student_id, title, description, date, likes, comments, post_file, file_name, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1, 1, 'Sample Not Uploaded Post Title 2', 'This is a sample post text.', '2025-05-10 10:00:00', 5, 55, pdf_data, 'Robustness-diagram-v0.1.pdf', 'Not Uploaded'))


            self.cursor.execute('''
                INSERT INTO Post (course_id, student_id, title, description, date, likes, comments, post_file, file_name, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (1, 1, 'Sample Uploaded Post Title', 'This is a sample post text.', '2025-05-10 10:00:00', 5, 55, pdf_data, 'Robustness-diagram-v0.1.pdf', 'Uploaded'))


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
            # Corrected line
            self.cursor.execute('''
                INSERT INTO Report (post_id, reporter_id, report_type, status, report_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (1, 1, 'Spam', 'Open', '2025-05-10'))


            self.conn.commit()
            print("Sample data inserted successfully.")

        except sqlite3.IntegrityError as e:
            print("Integrity error:", e)
        except Exception as e:
            print("An error occurred:", e)


    def close(self):
        self.conn.close()

    def query_fetch_profile(self):
        if not self.student:
            print("No student loaded.")

        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Profile WHERE am = ?", (self.student.am,))
            row = cursor.fetchone()

            if row:
                profile = Profile(
                    profile_id=row["profile_id"],
                    am=row["am"],
                    name=row["name"],
                    email=row["email"],
                    birth_date=row["birth_date"],
                    gender=row["gender"],
                    address=row["address"],
                    tel_num=row["tel_num"],
                    bio=row["bio"]
                )
                return profile
        except Exception as e:
            print("DB Error in query_fetch_profile:", e)

        return None

    def update_profile(self, am, name, email, birth_date, address, tel_num):
        try:
            self.cursor.execute('''
                UPDATE Profile
                SET name = ?, email = ?, birth_date = ?, address = ?, tel_num = ?
                WHERE am = ?
            ''', (name, email, birth_date, address, tel_num, am))
            self.conn.commit()
            return True
        except Exception as e:
            print("DB Error on update_profile:", e)
            return False