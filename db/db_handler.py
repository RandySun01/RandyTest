from conf import settings
import os
import pickle

"""
@author RansySun
@create 2019-08-31-15:32
"""


def save(obj):
    """
    保存对象信息
    :param obj:
    """
    class_name = obj.__class__.__name__
    file_path = os.path.join(settings.DB_PATH, class_name)
    # 判断文件是否存在
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    # 保存数据
    user_path = os.path.join(file_path, obj.name)
    with open(user_path, 'wb') as fw:
        pickle.dump(obj, fw)
        fw.flush()


def select(cls, username):
    """
    查询用户是否存在
    :param cls:
    :param username:
    :return:
    """
    class_name = cls.__name__

    file_path = os.path.join(settings.DB_PATH, class_name)

    # 判断用户是否存在，存在返回对象
    if os.path.isdir(file_path):

        user_path = os.path.join(file_path, username)
        if os.path.exists(user_path):
            with open(user_path, 'rb') as fr:
                return pickle.load(fr)
