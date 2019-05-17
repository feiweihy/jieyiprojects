# coding=UTF-8
'''
从带日期的日表当中导入到ES当中
执行的时候是全部导入的
'''
import requests
import json
import sys

es_ip = '192.168.1.169'
es_port = '9200'
es_index = 't_coupon_dtl'

#创建es的索引
def create_es_index():
    response = requests.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    if response.status_code == 200:
        print('index exists ,no need to create it!')
    else:
        _index_mappings = {
            'mappings': {
                "coupon": {
                     "properties": {
                            "cen_seq": {
                                "type": "keyword"
                            },
                            "cen_date": {
                                "type": "string"
                            },
                            "cen_time": {
                                "type": "string"
                            },
                            "sett_date": {
                                "type": "string",
                                "fielddata": True
                            },
                            "txn_mchntcd": {
                                "type": "string",
                                "fielddata": True
                            },
                            "txn_netcd": {
                                "type": "string",
                                "fielddata": True
                            },
                            "txn_oprid": {
                                "type": "string"
                            },
                            "term_id": {
                                "type": "string"
                            },
                            "term_seq": {
                                "type": "string"
                            },
                            "check_batchno": {
                                "type": "integer"
                            },
                            "txn_type": {
                                "type": "string"
                            },
                            "send_batch_id": {
                                "type": "string"
                            },
                            "coupon_id": {
                                "type": "string"
                            },
                            "activity_id": {
                                "type": "integer"
                            },
                            "activity_instid": {
                                "type": "integer"
                            },
                            "activity_instname": {
                                "type": "integer"
                            },
                            "activity_mchntid": {
                                "type": "string"
                            },
                            "activity_mchntname": {
                                "type": "string"
                            },
                            "discountrule_id": {
                                "type": "string"
                            },
                            "coupon_type": {
                                "type": "string"
                            },
                            "coupon_value": {
                                "type": "string"
                            },
                            "coupon_nickname": {
                                "type": "string"
                            },
                            "use_begin_time": {
                                "type": "string"
                            },
                            "use_end_time": {
                                "type": "string"
                            },
                            "coupon_usagecount": {
                                "type": "string"
                            },
                            "surplus_usagecount": {
                                "type": "string"
                            },
                            "off_value_per_use": {
                                "type": "string"
                            },
                            "send_date": {
                                "type": "string"
                            },
                            "send_time": {
                                "type": "string"
                            },
                            "get_user_phone": {
                                "type": "string"
                            },
                            "get_user_joininstid": {
                                "type": "string"
                            },
                            "get_user_joininst_uniid": {
                                "type": "string"
                            },
                            "coupon_holder": {
                                "type": "string"
                            },
                            "rec_crt_time": {
                                "type": "string"
                            },
                            "rec_upd_time": {
                                "type": "string"
                            }

                        }

                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put('http://'+es_ip+':'+es_port+'/'+es_index+'/coupon/1', headers=headers, data=json.dumps(_index_mappings))
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
