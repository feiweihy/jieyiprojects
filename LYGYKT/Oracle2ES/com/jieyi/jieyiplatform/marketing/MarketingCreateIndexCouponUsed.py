# coding=UTF-8
'''
从带日期的日表当中导入到ES当中
执行的时候是全部导入的
'''
import requests
import json
import sys

es_ip = '192.168.1.188'
es_port = '9200'
es_index = 't_coupon_used111'

#创建es的索引
def create_es_index():
    response = requests.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    if response.status_code == 200:
        print('index exists ,no need to create it!')
    else:
        _index_mappings = {
            'mappings': {
                "bus": {
                    "properties": {
                        "coupon_id": {
                            "type": "keyword"
                        },
                        "coupon_status": {
                            "type": "text"
                        },
                        "activity_id": {
                            "type": "text"
                        },
                        "activity_instid": {
                            "type": "text",
                            "fielddata": True
                        }
                    }
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put('http://'+es_ip+':'+es_port+'/'+es_index+'/bus/1', headers=headers, data=json.dumps(_index_mappings))
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
