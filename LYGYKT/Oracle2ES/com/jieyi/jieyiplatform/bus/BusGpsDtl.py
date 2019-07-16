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
es_index = 't_bus_gpsdtl'

#创建es的索引
def create_es_index():
    #response = requests.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    s = requests.Session()
    #s.auth = ('elastic', 'Zht@2019%(yx')
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
                        "cen_seq": {
                            "type": "keyword",
                            "fielddata": True
                        },
                        "cen_date": {
                            "type": "string"
                        },
                        "cen_time": {
                            "type": "string"
                        },
                        "term_manufactor": {
                            "type": "text",
                            "fielddata": True
                        },
                        "recv_instid": {
                            "type": "text"
                        },
                        "branch_id": {
                            "type": "text",
                            "fielddata": True
                        },
                        "line_id": {
                            "type": "text",
                            "fielddata": True
                        },
                        "bus_id": {
                            "type": "text",
                            "fielddata": True
                        },
                        "driver_id": {
                            "type": "text",
                            "fielddata": True
                        },
                        "driver_checkstatus": {
                            "type": "text"
                        },
                        "term_id": {
                            "type": "text"
                        },
                        "sam_id": {
                            "type": "text"
                        },
                        "req_date": {
                            "type": "text"
                        },
                        "req_time": {
                            "type": "integer"
                        },
                        "longitude": {
                            "type": "text"
                        },
                        "latitude": {
                            "type": "text"
                        }
                    }
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        #response = requests.put('http://'+es_ip+':'+es_port+'/'+es_index+'/coupon/1', headers=headers, data=json.dumps(_index_mappings))
        response = s.put('http://' + es_ip + ':' + es_port + '/' + es_index + '/gpsdtl/1', headers=headers,data=json.dumps(_index_mappings))
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
