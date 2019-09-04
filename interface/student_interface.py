from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def register_interface(username, pwd):
    """

    :param username:
    :param pwd:
    :return:
    """
    student_obj = models.Student.select(username)
    # 1 判断用户是否存在
    if student_obj:
        return False, f"{username}用户已经存在"

    # 2 不存在创建学生
    models.Student(username, pwd)
    return True, f"{username}注册成功！"

    pass


def login_interface(username, pwd):
    """

    :param username:
    :param pwd:
    :return:
    """
    student_obj = models.Student.select(username)
    # 1 判断用户是否存在
    if not student_obj:
        return False, f"{username}用户不存在"

    # 2 判断密码是否相同
    if student_obj.pwd == pwd:
        return True, f"{username}用户登录成功"
    else:
        return False, F"用户或密码错误！"


def choose_school_interface(student_name, school_name):
    """
    选择学校接口
    :param student_name:
    :param school_name:
    :return:
    """
    student_obj = models.Student.select(student_name)
    # 1 判断用户是否存在
    if not student_obj:
        return False, f"{student_name}用户不存在"

    # 2 判断学生是否选择了学校
    if student_obj.school:
        return False, f"{school_name}已经选择了学校"

    # 3 通过学生类保存学校
    student_obj.choose_school(school_name)
    return True, f"{student_name}选择了{school_name}学校"


def get_school_course(student_nmae):
    """
    通过获取学生选择的学校中的课程
    :param student_nmae:
    :return:
    """
    student_obj = models.Student.select(student_nmae)

    if student_obj.school:
        school_name = student_obj.school
        school_obj = models.School.select(school_name)
        return True, school_obj.school_course_list

    else:
        return False, '请先选择学校!'


def choose_course_interface(student_name, course_name):
    student_obj = models.Student.select(student_name)
    # 1 判断用户是否存在
    if not student_obj:
        return False, f"{student_name}用户不存在"
    # 2 判断课程是否已经选择
    if course_name in student_obj.student_course_list:
        return False, "该课程已经被选择"
    # 2 通过学生类添加课程
    student_obj.choose_course(course_name)
    return True, f'{student_name}选择{course_name}课程'


def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    # 1 判断用户是否存在
    if not student_obj:
        return False, f"{student_name}用户不存在"

    # 2 获取课程
    return True, student_obj.check_score()
