'''
从带日期的日表当中导入到ES当中
执行的时候是全部导入的
'''
import cx_Oracle
import requests
import json
import sys

es_ip = '127.0.0.1'
es_port = '9200'
es_index = 't_log_cash_test6'

#创建es的索引
def create_es_index():
    response = requests.get('http://' + es_ip + ':' + es_port + '/'+es_index)
    if response.status_code == 200:
        print('index exists ,no need to create it!')
    else:
        _index_mappings = {
            'mappings':{
                "bus":{
                    "properties": {
                        "settdate": {
                            "type": "keyword"
                        },
                        "censeq": {
                            "type": "keyword"
                        },
                        "centdate": {
                            "type": "text"
                        },
                        "centtime": {
                            "type": "text"
                        },
                        "txncode": {
                            "type": "text"
                        }
                        ,
                        "inntype": {
                            "type": "text"
                        }
                        ,
                        "txndesc": {
                            "type": "text"
                        }
                    }
                }
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put('http://'+es_ip+':'+es_port+'/'+es_index+'/bus/1', headers=headers, data=json.dumps(_index_mappings))
        print(response)
        print(response.text)

def insert_into_es(row):
    row_dict = dict()
    row_dict['settdate'] = row[0]
    row_dict['censeq'] = row[1]
    row_dict['centdate'] = row[2]
    row_dict['centtime'] = row[3]
    row_dict['txncode'] = row[4]
    row_dict['inntype'] = row[5]
    row_dict['txndesc'] = row[6]
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://' + es_ip + ':' + es_port + '/' + es_index + '/bus', headers=headers,
                 data=json.dumps(row_dict))
    print(response)
    print(response.text)


#函数入口
if __name__ == '__main__':
    print('=========='+sys.argv[1])
    cchssettdate = sys.argv[1]
    cchsmonth = cchssettdate[4:6]
    try:
        # 初始化，创建es索引
        create_es_index()
        # 连接oracle取数据
        conn_core = cx_Oracle.connect('jtb_lygbus/111111@192.168.1.96:1521/orcl')
        curs_core = conn_core.cursor()
        sql_t_log_cash = 'SELECT * FROM T_LOG_DEBITDETAILM'+cchsmonth+' where cchserrcode=0'
        rr = curs_core.execute(sql_t_log_cash)
        #这里加一段oracle数据总数和es数据总数是否一样，不一样，则清空es，然后再插入，如果一样，则直接跳过，不用做迁移了

        for row in rr:
            print(row)
            insert_into_es(row)
    except:
        print('Exception!!!')
    finally:
        curs_core.close()
        conn_core.close()
