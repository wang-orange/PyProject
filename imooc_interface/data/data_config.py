#coding:utf-8

class global_val:
    ''' caseID '''
    Id = 0
    request_name = 1
    url = 2
    run = 3
    request_way = 4
    header = 5
    case_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect = 10
    result = 11
# 获取caseid
def get_id():
    return global_val.Id
# 获取url
def get_url():
    return global_val.url

def get_run():
    return global_val.run

def get_request_way():
    return global_val.request_way

def get_header():
    return global_val.header

def get_header_data():
    header = {
        'header':'123455',
        'cookie':'mushishi'
    }
    return header

def get_case_depend():
    return global_val.case_depend

def get_data_depend():
    return global_val.data_depend

def get_field_depend():
    return global_val.field_depend

def get_data():
    return global_val.data

def get_expect():
    return global_val.expect

def get_result():
    return global_val.result


