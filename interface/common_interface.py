from conf import settings
import os

"""
@author RansySun
@create 2019-08-31-15:32
"""


def get_school_list():
    """
    获取学校列表信息
    :return:
    """
    file_path = os.path.join(settings.DB_PATH, 'School')
    if os.path.exists(file_path):
        return os.listdir(file_path)


def get_course_list():
    """
    获取课程列表信息
    :return:
    """
    file_opath = os.path.join(settings.DB_PATH, 'Course')
    if os.path.exists(file_opath):
        return os.listdir(file_opath)
