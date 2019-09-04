from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def login_interface(username, pwd):
    teacher_obj = models.Teacher.select(username)
    # 1 判断用户是否存在
    if not teacher_obj:
        return False, f'{username}用户不存在'

    if teacher_obj.pwd == pwd:
        return True, F"{username}登录成功"
    else:
        return False, "用户名或密码错误"


def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    teacher_course_list = teacher_obj.check_course()
    return True, teacher_course_list


def choose_course_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    # 1 查看课程是否选择
    flag, teacher_course_list = check_course_interface(teacher_name)
    if course_name in teacher_course_list:
        return False, f'{course_name}课程已存在'

    teacher_obj.choose_course(course_name)
    return True, f"{teacher_name}选择{course_name}课程选择成功"


def check_student_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    # 2 让老师去产看课程下的学生
    student_list = teacher_obj.check_student(course_name)

    if student_list:
        return True, student_list
    else:
        return False, "课程下没有学生"


def change_score_interface(teacher_name, course_name, student_name, score):
    teacher_obj = models.Teacher.select(teacher_name)

    # 让老师去修改课程成绩
    teacher_obj.change_score(course_name, student_name, score)
    return True, '修改成功'

