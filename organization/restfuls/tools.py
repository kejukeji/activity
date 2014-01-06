# coding: utf-8

from organization.models.t_custom import CustomClass


def get_token(custom_id):
    pub = get_pub(custom_id)
    if pub:
        return str(pub.token)
    raise ValueError


def parse_request(request_dict, args):
    """返回一个字典"""
    return_dict = {}
    for arg in args:
        return_dict[arg] = request_dict.get(arg)
    return return_dict


def get_pub(custom_id):
    return CustomClass.query.filter(CustomClass.open_id == custom_id).first()