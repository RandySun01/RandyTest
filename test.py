"""
@author RansySun
@create 2019-08-31-21:04
"""
from interface import teacher_interface


def check_student():
    """
    老师查看课程下的学生
    """
    while True:
        # 1 获取所有课程
        flag, course_list = teacher_interface.check_course_interface("tearcher")
        if not course_list:
            print("课程为空")
        # 2 打印课程
        for indx, course in enumerate(course_list):
            print(f"课程编号{indx}  {course}")

        # 3 选择课程
        choice = input("请输入课程编号")
        if choice == 'q':
            break
        if not choice.isdigit():
            print("必须是数字")
            continue

        choice = int(choice)
        print(choice)
        if choice not in range(len(course_list)):
            print("输入课程不存在")
            print(1)
            break

        course_name = course_list[choice]

        # 3 获取当前课程下学生
        flag, msg = teacher_interface.check_student_interface("tearcher", course_name)

        if flag:

            print(f"学生：{msg}")


        else:
            print(msg)

            break


# check_student()

from db import models


def check_student():
    """
    获取课程下的学生
    :param course_name:
    :return:
    """
    course_obj = models.Course.select("英语")
    # course_obj.add_student("student")
    data = course_obj.course_student_list

    print(data)


check_student()


def check_student1():
    """
    获取课程下的学生
    :param course_name:
    :return:
    """
    course_obj = models.Student.select("d")
    data = course_obj.student_course_list
    print(data)


check_student1()
