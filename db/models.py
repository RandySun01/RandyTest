from db import db_handler

"""
@author RansySun
@create 2019-08-31-15:31
"""


class Base:

    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls, username):
        return db_handler.select(cls, username)


class Admin(Base):
    def __init__(self, username, pwd):
        self.name = username
        self.pwd = pwd
        self.save()

    def create_school(self, school_name, school_addr):
        """
        通过管理员创建学校
        :param school_name:
        :param school_addr:
        """
        School(school_name, school_addr)

    def create_teacher(self, teacher_name, teacher_pwd):
        """
        通过管理员创建老师
        :param teacher_name:
        :param teacher_pwd:
        """
        Teacher(teacher_name, teacher_pwd)

    def create_course(self, school_name, course_name):
        """
        1 通过管理员为学校添加课程
        2 创建课程
        :param school_name:
        :param course_name:
        """
        # 1 为学校添加课程
        school_obj = School.select(school_name)
        # 2 创建课程
        Course(course_name)
        school_obj.add_school_course(course_name)


class School(Base):
    def __init__(self, school_name, school_addr):
        self.name = school_name
        self.addr = school_addr
        # 学校的课程， teacher_name
        self.school_course_list = []
        self.save()

    def add_school_course(self, course_name):
        self.school_course_list.append(course_name)
        self.save()


class Teacher(Base):
    def __init__(self, teacher_name, pwd):
        self.name = teacher_name
        self.pwd = pwd
        # 老师的课程，去找课程下面的学生
        self.teacher_course_list = []
        self.save()

    def check_course(self):
        """
        查看教师选择的课程
        """
        return self.teacher_course_list

    def add_tacher_course(self, course_name):
        """
        添加老师选择的课程课程
        :param course_name:
        """
        self.teacher_course_list.append(course_name)
        self.save()

    def check_student(self, course_name):
        """
        获取课程下的学生
        :param course_name:
        :return:
        """
        course_obj = Course(course_name)
        return course_obj.course_student_list

    def change_score(self, course_name, student_name, score):
        """
        老师修改课程成绩
        :param student_name:

        """

        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        # 将创建的学生添加到课程
        self.course_student_list = []
        self.save()

    def add_student(self, student_name):
        """
        将学生选择的课程添加到相应的课程中
        :param student_name:
        """
        self.course_student_list.append(student_name)
        self.save()
        print("将学生添加可课程成功",self.course_student_list)


class Student(Base):
    def __init__(self, student_name, student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        # 学校
        self.school = None
        # 学生课程列表
        self.student_course_list = []
        # 学生课程成绩
        self.score = {}
        self.save()

    def check_score(self):
        """
        查看成绩
        :return:
        """
        return self.score

    def choose_school(self, school_name):
        """
        通过学生类选择学生
        :param school_name:
        """
        self.school = school_name
        self.save()

    def choose_course(self, course_name):
        # 1 添加学生选择的课程
        self.student_course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

        # 2 将学生绑定到课程
        course_obj = Course(course_name)
        course_obj.add_student(self.name)



#
# from db import db_handler
#
# """
# @author RansySun
# @create 2019-08-31-15:31
# """
#
#
# class Base:
#
#     def save(self):
#         db_handler.save(self)
#
#     @classmethod
#     def select(cls, username):
#         return db_handler.select(cls, username)
#
#
# class Admin(Base):
#     def __init__(self, username, pwd):
#         self.name = username
#         self.pwd = pwd
#         self.save()
#
#     def create_school(self, school_name, school_addr):
#         # 创建学校
#         School(school_name, school_addr)
#
#     def create_teacher(self, teacher_name, teacher_pwd):
#         # 创建老师
#         Teacher(teacher_name, teacher_pwd)
#
#     def create_course(self, school_name, course_name):
#         # 为学校创建课程
#         school_obj = School.select(school_name)
#         Course(course_name)
#
#         # 将课程绑定给学校
#         school_obj.add_school_course(course_name)
#
#
# class School(Base):
#     def __init__(self, school_name, school_addr):
#         self.name = school_name
#         self.addr = school_addr
#         self.school_course_list = []
#         self.save()
#
#     def add_school_course(self, course_name):
#         self.school_course_list.append(course_name)
#         self.save()
#
#
# class Teacher(Base):
#     def __init__(self, teacher_name, teacher_pwd):
#         self.name = teacher_name
#         self.pwd = teacher_pwd
#         self.teacher_course_list = []
#         self.save()
#
#     def add_teacher_course(self, course_name):
#         self.teacher_course_list.append(course_name)
#         self.save()
#
#     def check_course(self):
#         return self.teacher_course_list
#
#     def choose_course(self, course_name):
#         self.teacher_course_list.append(course_name)
#         self.save()
#
#     def check_student(self, course_name):
#         course_obj = Course.select(course_name)
#         student_list = course_obj.course_student_list
#         return student_list
#
#     def change_score(self, course_name, student_name, score):
#         student_obj = Student.select(student_name)
#         student_obj.score[course_name] = score
#         student_obj.save()
#
#
#
#
#
# class Course(Base):
#     def __init__(self, course_name):
#         self.name = course_name
#         self.course_student_list = []
#         self.save()
#
#     def add_course_student(self, student_name):
#         self.course_student_list.append(student_name)
#         self.save()
#         print(f"课程中的学生{self.course_student_list}")
#
#
#
# class Student(Base):
#     def __init__(self, student_name, student_pwd):
#         self.name = student_name
#         self.pwd = student_pwd
#         self.school = None
#         self.student_course_list = []
#         self.score = {}
#         self.save()
#
#     def choose_school(self, school_name):
#         # 选择学校
#         self.school = school_name
#         self.save()
#
#     def choose_course(self, course_name):
#         # 添加课程可成绩
#         self.student_course_list.append(course_name)
#         self.score[course_name] = 0
#         self.save()
#
#         # 将学生绑定到选择的课程上面
#         course_ojb = Course.select(course_name)
#         course_ojb.add_course_student(self.name)
#
#     def check_score(self):
#         return self.score
