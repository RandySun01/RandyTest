from lib import common
from interface import admin_interface, common_interface

"""
@author RansySun
@create 2019-08-31-15:31
"""
admin_user = {'user': None}


def register():
    """
    管理员注册
    """
    while True:
        username, pwd = common.input_username_pwd()
        flag, msg = admin_interface.register_interface(username, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


def login():
    """
    管理员登录
    """
    while True:

        username, pwd = common.input_username_pwd()
        flag, msg = admin_interface.login_interface(username, pwd)
        if flag:
            print(msg)
            admin_user['user'] = username
            break
        else:
            print(msg)
            break

@common.login_auth("admin")
def create_school():
    """
    管理员创建学校
    """
    while True:
        school_name = input("请输入学校名称")
        school_addr = input("请输入学校地址")
        flag, msg = admin_interface.create_school_interface(admin_user.get('user'), school_name, school_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

@common.login_auth("admin")
def create_teacher():
    """
    管理员创建老师
    """
    teacher_name = input("请输入老师姓名").strip()
    flag, msg = admin_interface.create_teacher_interface(admin_user.get('user'), teacher_name)
    if flag:
        print(msg)

    else:
        print(msg)

@common.login_auth("admin")
def create_course():
    """
    管理员为学校创建课程
    """
    while True:

        # 1获取学校列表信息
        school_list = common_interface.get_school_list()
        if not school_list:
            print("学校为空，请去创建学校")

        # 2 打印课程
        for indx, school in enumerate(school_list):
            print(f"学校编号：{indx}  {school}")

        # 3 选择学校并判断
        choice_school = input("请输入学校编号")
        if not choice_school.isdigit():
            print("必须是数字")
            continue
        if choice_school == 'q':
            break

        choice_school = int(choice_school)
        if choice_school not in range(len(school_list)):
            print("学校不存在")
        school_name = school_list[choice_school]

        # 4 输入学校信息
        course_name = input("请输入课程名称").strip()
        if choice_school == 'q':
            break

        # 5 调用接口实现功能
        flag, msg = admin_interface.create_course_interface(admin_user['user'], school_name, course_name)
        if flag:

            print(msg)
            break

        else:
            print(msg)
            break


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course,
}


def admin_view():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建老师
        5.创建课程
        q.退出
        ''')

        choice = input("请输入管理员功能").strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print("输入错误")
            continue
        func_dic.get(choice)()
