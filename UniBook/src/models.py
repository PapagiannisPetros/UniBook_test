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
