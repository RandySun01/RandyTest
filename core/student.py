from lib import common
from interface import student_interface, common_interface

"""
@author RansySun
@create 2019-08-31-15:31
"""
student_user = {'user': None}


def register():
    username, pwd = common.input_username_pwd()
    flag, msg = student_interface.register_interface(username, pwd)
    if flag:
        print(msg)
    else:
        print(msg)


def login():
    username, pwd = common.input_username_pwd()
    flag, msg = student_interface.login_interface(username, pwd)
    if flag:
        print(msg)
        student_user['user'] = username
    else:
        print(msg)


@common.login_auth("student")
def choose_school():
    """
    学生选择学校
    """
    while True:
        # 1 获取学校列表
        school_list = common_interface.get_school_list()
        if not school_list:
            print("学校为空")
        # 2 打印课程，并选择学校
        for indx, school in enumerate(school_list):
            print(f"学校编号{indx} {school}")

        choice = input("请输入学校编号").strip()
        if choice == 'q':
            break

        if not choice.isdigit():
            print("必须是数字")
            continue

        choice = int(choice)
        if choice not in range(len(school_list)):
            print("学校不存在")
            continue

        # 3 获取学校名称
        school_name = school_list[choice]

        # 3 调用接口
        flag, msg = student_interface.choose_school_interface(student_user.get('user'), school_name)

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth("student")
def choose_course():
    """
    学生选择课程
    """
    while True:

        # 1 获取当前学生所在学校的课程
        flag, course_list = student_interface.get_school_course(student_user.get('user'))

        if (not flag) or (not course_list):
            print("课程不存在")

        # 2 打印课程信息
        for indx, course in enumerate(course_list):
            print(f"课程不编号: {indx} {course}")

        # 3 选择课程
        choice = input("请输入课程比编号").strip()

        if choice == 'q':
            break

        if not choice.isdigit():
            print("输入必须是数字")
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print("课程不存在")
            continue

        course_name = course_list[choice]

        # 4 调用接口
        flag, msg = student_interface.choose_course_interface(student_user.get('user'), course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth("student")
def check_score():
    flag, msg = student_interface.check_score_interface(student_user.get('user'))
    if flag:
        print(msg)
    else:
        print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}


def student_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看成绩
        q.退出
        ''')

        choice = input("请输入学生功能编号：").strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print("输入错误")
            continue
        func_dic.get(choice)()
