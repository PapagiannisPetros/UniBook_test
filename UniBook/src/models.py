class Student:
    def __init__(self, student_id, user_id, subscription_id, am, university, department, enrollment_year, validation_status):
        self.student_id = student_id
        self.user_id = user_id
        self.subscription_id = subscription_id
        self.am = am
        self.university = university
        self.department = department
        self.enrollment_year = enrollment_year
        self.validation_status = validation_status


class Admin:
    def __init__(self, admin_id, user_id, name):
        self.admin_id = admin_id
        self.user_id = user_id
        self.name = name


class Profile:
    def __init__(self, profile_id, am, name, email, birth_date, gender, address, tel_num, bio):
        self.profile_id = profile_id
        self.am = am
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.address = address
        self.tel_num = tel_num
        self.bio = bio


class Subscription:
    def __init__(self, subscription_id, profile_id, subscription_type, start_date, end_date):
        self.subscription_id = subscription_id
        self.profile_id = profile_id
        self.subscription_type = subscription_type
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return (f"<Subscription id={self.subscription_id}, profile_id={self.profile_id}, "
                f"type={self.subscription_type}, start={self.start_date}, end={self.end_date}>")


class Report:
    def __init__(self, report_id, post_id, reporter_id, report_type, status, report_time):
        self.report_id = report_id
        self.post_id = post_id
        self.reporter_id = reporter_id
        self.report_type = report_type
        self.status = status
        self.report_time = report_time


class Course:
    def __init__(self, course_id, course_name, semester):
        self.course_id = course_id
        self.course_name = course_name
        self.semester = semester
        self.posts = []  # Will be filled later

    def __repr__(self):
        return f"<Course {self.course_name} (Semester {self.semester})>"


class Post:
    def __init__(self, post_id, course_id, student_id, title, description, date, likes, comments, post_file, file_name):
        self.post_id = post_id
        self.course_id = course_id
        self.student_id = student_id
        self.title = title
        self.description = description
        self.date = date
        self.likes = likes
        self.post_file = post_file  # Binary data of the PDF
        self.file_name = file_name

        #self.image_path = image_path  # Optional: path to image file

    def __repr__(self):
        return f"<Post #{self.post_id} by Student #{self.student_id}>"
    

class Chat:
    def __init__(self, chat_id, course_id):
        self.chat_id = chat_id
        self.course_id = course_id
        self.messages = []

    def __repr__(self):
        return f"<Chat from {self.sender_id} to {self.receiver_id}>"
    

class Message:
    def __init__(self, message_id, chat_id, student_id, message_text, send_time):
        self.message_id = message_id
        self.chat_id = chat_id
        self.student_id = student_id
        self.message_text = message_text
        self.send_time = send_time

    def __repr__(self):
        return f"<Message from {self.sender_id} to {self.receiver_id}>"
    

class Comment:
    def __init__(self, comment_id, student_id, comment_text, upload_time, post_id):
        self.comment_id = comment_id
        self.student_id = student_id
        self.comment_text = comment_text
        self.upload_time = upload_time if isinstance(upload_time, str) else upload_time.strftime("%Y-%m-%d %H:%M:%S")
        self.post_id = post_id

    def __repr__(self):
        return f"<Comment by student {self.author_id} on post {self.post_id}: {self.comment_text}>"
