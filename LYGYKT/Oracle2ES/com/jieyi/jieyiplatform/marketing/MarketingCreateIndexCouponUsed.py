# coding=UTF-8
'''
从带日期的日表当中导入到ES当中
执行的时候是全部导入的
'''
import requests
import json
import sys

#es_ip = '192.168.1.169'
es_ip = 'es-cn-mp9152m5e000quczd.public.elasticsearch.aliyuncs.com'
es_port = '9200'
es_index = 't_coupon_used'

#创建es的索引
def create_es_index():
    #response = requests.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    s = requests.Session()
    s.auth = ('elastic', 'Zht@2019%(yx')
    response = s.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    print(response.status_code)
    print('11111111111111')
    if response.status_code == 200:
        print('index exists ,no need to create it!')
    else:
        _index_mappings = {
            'mappings': {
                "coupon": {
                    "properties": {
                        "coupon_id": {
                            "type": "keyword",
                            "fielddata": True
                        },
                        "coupon_status": {
                            "type": "text"
                        },
                        "activity_id": {
                            "type": "text",
                            "fielddata": True
                        },
                        "activity_instid": {
                            "type": "text",
                            "fielddata": True
                        },
                        "activity_instname": {
                            "type": "text",
                            "fielddata": True
                        },
                        "activity_mchntid": {
                            "type": "text",
                            "fielddata": True
                        },
                        "activity_mchntname": {
                            "type": "text"
                        },
                        "activity_coupon_type": {
                            "type": "text"
                        },
                        "discountrule_id": {
                            "type": "text"
                        },
                        "coupon_type": {
                            "type": "text"
                        },
                        "coupon_value": {
                            "type": "integer"
                        },
                        "coupon_nickname": {
                            "type": "text"
                        },
                        "use_begin_time": {
                            "type": "text"
                        },
                        "use_end_time": {
                            "type": "text"
                        },
                        "coupon_usagecount": {
                            "type": "integer"
                        },
                        "surplus_usagecount": {
                            "type": "integer"
                        },
                        "off_value_per_use": {
                            "type": "integer"
                        },
                        "send_date": {
                            "type": "text"
                        },
                        "send_time": {
                            "type": "text"
                        },
                        "get_user_phone": {
                            "type": "text"
                        },
                        "get_user_joininstid": {
                            "type": "text"
                        },
                        "get_user_joininst_uniid": {
                            "type": "text"
                        },
                        "get_user_joininst_name": {
                            "type": "text"
                        },
                        "coupon_holder": {
                            "type": "text"
                        },
                        "coupon_holder_name": {
                            "type": "text"
                        },
                        "writeoff_date": {
                            "type": "text"
                        },
                        "writeoff_time": {
                            "type": "text"
                        },
                        "send_batch_id": {
                            "type": "text"
                        },
                        "rec_crt_time": {
                            "type": "text"
                        },
                        "rec_upd_time": {
                            "type": "text"
                        }
                    }
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        #response = requests.put('http://'+es_ip+':'+es_port+'/'+es_index+'/coupon/1', headers=headers, data=json.dumps(_index_mappings))
        response = s.put('http://' + es_ip + ':' + es_port + '/' + es_index + '/coupon/1', headers=headers,data=json.dumps(_index_mappings))
        print(response)
        print(response.text)


# 函数入口
if __name__ == '__main__':
    try:
        # 初始化，创建es索引
        create_es_index()
    except:
        print('Exception!!!')
    finally:
        print('End!!!')
