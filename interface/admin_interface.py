from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def register_interface(username, pwd):
    admin_obj = models.Admin.select(username)
    # 1 判断管理员是否存在
    if admin_obj:
        return False, f"{username}管理员已经存在"

    models.Admin(username, pwd)
    return True, f"{username}注册成功！"


def login_interface(username, pwd):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        return False, f"{username}用户不存在"

    if admin_obj.pwd == pwd:
        return True, f"{username}登录成功"
    else:
        return False, f"用户名或密码错误！"


def create_school_interface(admin_user, school_name, school_addr):
    # 判断学校是否存在
    school_obj = models.School.select(school_name)

    if school_obj:
        return False, f"{school_name}学校已经存在"

    # 2 保存学校信息
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_school(school_name, school_addr)

    return True, f"{school_name}学校创建成功"

    pass


def create_teacher_interface(admin_user, teacher_name, pwd='123'):
    # 查看老师是否纯在
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False, f"{teacher_name}老师已存在"

    # 2 通过管理员创建老师
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_teacher(teacher_name, pwd)

    return True, f"{teacher_name}老师创建成功"


def create_course_interface(admin_user, school_name, course_name):
    # 1 判断学校是否存在
    school_obj = models.School.select(school_name)
    if not school_obj:
        return False, "你输入的学校不存在"

    # 2 判断课程是否已添加
    if course_name in school_obj.school_course_list:
        return False, f"{school_name}学校已有{course_name}课程"

    # 3 通过管理员添加课程
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_course(school_name, course_name)
    return True, f"{school_name}添加了{course_name}课程"
