import os



"""
@author RansySun
@create 2019-08-31-15:33
"""


def login_auth(auth):
    """
    三层装饰器
    :param auth:
    :return:
    """
    from core import admin, student, teacher
    def outter(func):
        def innter(*args, **kwargs):

            if auth == 'admin':
                if admin.admin_user.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif auth == 'student':
                if student.student_user.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif auth == 'teacher':
                if teacher.teacher_info.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()

        return innter

    return outter


def input_username_pwd():
    """
    用户输入数据
    :return:
    """
    username = input("请输入用户名")
    pwd = input("请输入密码")

    return username, pwd
