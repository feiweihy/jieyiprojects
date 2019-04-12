# coding=UTF-8
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
es_index = 't_log_cash_test'
oracle_ip = '192.168.1.96'
oracle_port = '1521'
oracle_sid = 'orcl'
oracle_username = 'jtb_lygbus'
oracle_userpwd = '111111'

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
                        "debitsettleseq": {
                            "type": "keyword"
                        },
                        "acqorgid": {
                            "type": "text"
                        },
                        "unitid": {
                            "type": "text"
                        },
                        "branchid": {
                            "type": "text"
                        },
                        "txntype": {
                            "type": "text"
                        },
                        "transtype": {
                            "type": "text"
                        },
                        "sendtxnseq": {
                            "type": "text"
                        },
                        "termid": {
                            "type": "text"
                        },
                        "localseq": {
                            "type": "text"
                        },
                        "posid": {
                            "type": "text"
                        },
                        "posseq": {
                            "type": "text"
                        },
                        "samid": {
                            "type": "text"
                        },
                        "posoprid": {
                            "type": "text"
                        },
                        "cardid": {
                            "type": "text"
                        },
                        "cardcsn": {
                            "type": "text"
                        },
                        "debitcounter": {
                            "type": "text"
                        },
                        "cardmodel": {
                            "type": "text"
                        },
                        "cardvalid": {
                            "type": "text"
                        },
                        "cardproduct": {
                            "type": "text"
                        },
                        "cardkind": {
                            "type": "text"
                        },
                        "childcardkind": {
                            "type": "text"
                        },
                        "befbalance": {
                            "type": "text"
                        },
                        "debitmoney": {
                            "type": "text"
                        },
                        "pricetype": {
                            "type": "text"
                        },
                        "origamt": {
                            "type": "text"
                        },
                        "issorgcode": {
                            "type": "text"
                        },
                        "debitdate": {
                            "type": "text",
                            "fielddata": True
                        },
                        "debittime": {
                            "type": "text",
                            "fielddata": True
                        },
                        "tac": {
                            "type": "text"
                        },
                        "cardrand": {
                            "type": "text"
                        },
                        "eccissappdata": {
                            "type": "text"
                        },
                        "txnamtcode": {
                            "type": "text"
                        },
                        "otheramt": {
                            "type": "text"
                        },
                        "termcountrycode": {
                            "type": "text"
                        },
                        "termchkrst": {
                            "type": "text"
                        },
                        "ecctranstp": {
                            "type": "text"
                        },
                        "eccaip": {
                            "type": "text"
                        },
                        "cardversion": {
                            "type": "text"
                        },
                        "tmtktype": {
                            "type": "text"
                        },
                        "keyver": {
                            "type": "text"
                        },
                        "computflag": {
                            "type": "text"
                        },
                        "keyindex": {
                            "type": "text"
                        },
                        "cardorg": {
                            "type": "text"
                        },
                        "errcode": {
                            "type": "text"
                        },
                        "pkgid": {
                            "type": "text"
                        },
                        "recordno": {
                            "type": "text"
                        },
                        "recollectflag": {
                            "type": "text"
                        },
                        "opercardid": {
                            "type": "text"
                        },
                        "selloperid": {
                            "type": "text"
                        },
                        "sellcardid": {
                            "type": "text"
                        },
                        "pretype": {
                            "type": "text"
                        },
                        "preamt": {
                            "type": "text"
                        },
                        "prenum": {
                            "type": "text"
                        },
                        "changeunitid": {
                            "type": "text"
                        },
                        "changeposid": {
                            "type": "text"
                        },
                        "changelineid": {
                            "type": "text"
                        },
                        "changetime": {
                            "type": "text"
                        },
                        "changeindustry": {
                            "type": "text"
                        },
                        "currinustry": {
                            "type": "text"
                        },
                        "changersvd": {
                            "type": "text"
                        },
                        "uptime": {
                            "type": "text"
                        },
                        "uptermid": {
                            "type": "text"
                        },
                        "upbusid": {
                            "type": "text"
                        },
                        "uplineid": {
                            "type": "text"
                        },
                        "upstationid": {
                            "type": "text"
                        },
                        "dwnbusid": {
                            "type": "text"
                        },
                        "dwnlineid": {
                            "type": "text"
                        },
                        "dwnstationid": {
                            "type": "text"
                        },
                        "direction": {
                            "type": "text"
                        },
                        "testflag": {
                            "type": "text"
                        },
                        "cchssettdate": {
                            "type": "text"
                        },
                        "cchserrcode": {
                            "type": "text"
                        },
                        "susatt": {
                            "type": "text"
                        },
                        "checkintime": {
                            "type": "text"
                        },
                        "reserved": {
                            "type": "text"
                        },
                        "oprsipcode": {
                            "type": "text"
                        },
                        "upinstid": {
                            "type": "text"
                        },
                        "panseq": {
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
    row_dict['debitsettleseq'] = row[0]
    row_dict['acqorgid'] = row[1]
    row_dict['unitid'] = row[2]
    row_dict['branchid'] = row[3]
    row_dict['txntype'] = row[4]
    row_dict['transtype'] = row[5]
    row_dict['sendtxnseq'] = row[6]
    row_dict['termid'] = row[7]
    row_dict['localseq'] = row[8]
    row_dict['posid'] = row[9]
    row_dict['posseq'] = row[10]
    row_dict['samid'] = row[11]
    row_dict['posoprid'] = row[12]
    row_dict['cardid'] = row[13]
    row_dict['cardcsn'] = row[14]
    row_dict['debitcounter'] = row[15]
    row_dict['cardmodel'] = row[16]
    row_dict['cardvalid'] = row[17]
    row_dict['cardproduct'] = row[18]
    row_dict['cardkind'] = row[19]
    row_dict['childcardkind'] = row[20]
    row_dict['befbalance'] = row[21]
    row_dict['debitmoney'] = row[22]
    row_dict['pricetype'] = row[23]
    row_dict['origamt'] = row[24]
    row_dict['issorgcode'] = row[25]
    row_dict['debitdate'] = row[26]
    row_dict['debittime'] = row[27]
    row_dict['tac'] = row[28]
    row_dict['cardrand'] = row[29]
    row_dict['eccissappdata'] = row[30]
    row_dict['txnamtcode'] = row[31]
    row_dict['otheramt'] = row[32]
    row_dict['termcountrycode'] = row[33]
    row_dict['termchkrst'] = row[34]
    row_dict['ecctranstp'] = row[35]
    row_dict['eccaip'] = row[36]
    row_dict['cardversion'] = row[37]
    row_dict['tmtktype'] = row[38]
    row_dict['keyver'] = row[39]
    row_dict['computflag'] = row[40]
    row_dict['keyindex'] = row[41]
    row_dict['cardorg'] = row[42]
    row_dict['errcode'] = row[43]
    row_dict['pkgid'] = row[44]
    row_dict['recordno'] = row[45]
    row_dict['recollectflag'] = row[46]
    row_dict['opercardid'] = row[47]
    row_dict['selloperid'] = row[48]
    row_dict['sellcardid'] = row[49]
    row_dict['pretype'] = row[50]
    row_dict['preamt'] = row[51]
    row_dict['prenum'] = row[52]
    row_dict['changeunitid'] = row[53]
    row_dict['changeposid'] = row[54]
    row_dict['changelineid'] = row[55]
    row_dict['changetime'] = row[56]
    row_dict['changeindustry'] = row[57]
    row_dict['currinustry'] = row[58]
    row_dict['changersvd'] = row[59]
    row_dict['uptime'] = row[60]
    row_dict['uptermid'] = row[61]
    row_dict['upbusid'] = row[62]
    row_dict['uplineid'] = row[63]
    row_dict['upstationid'] = row[64]
    row_dict['dwnbusid'] = row[65]
    row_dict['dwnlineid'] = row[66]
    row_dict['dwnstationid'] = row[67]
    row_dict['direction'] = row[68]
    row_dict['testflag'] = row[69]
    row_dict['cchssettdate'] = row[70]
    row_dict['cchserrcode'] = row[71]
    row_dict['susatt'] = row[72]
    row_dict['checkintime'] = row[73]
    row_dict['reserved'] = row[74]
    row_dict['oprsipcode'] = row[75]
    row_dict['upinstid'] = row[76]
    row_dict['panseq'] = row[77]
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://' + es_ip + ':' + es_port + '/' + es_index + '/bus', headers=headers,
                 data=json.dumps(row_dict))
    print(response)
    print(response.text)


# 函数入口
if __name__ == '__main__':
    print('=========='+sys.argv[1])
    cchssettdate = sys.argv[1]
    cchsmonth = cchssettdate[4:6]
    try:
        # 初始化，创建es索引
        create_es_index()
        # 连接oracle取数据
        conn_core = cx_Oracle.connect(oracle_username+'/'+oracle_userpwd+'@'+oracle_ip+':'+oracle_port+'/'+oracle_sid)
        curs_core = conn_core.cursor()
        sql_t_log_cash = 'SELECT * FROM T_LOG_DEBITDETAILM'+cchsmonth+' where cchssettdate='+cchssettdate+' and cchserrcode=0'
        rr = curs_core.execute(sql_t_log_cash)
        # 这里加一段oracle数据总数和es数据总数是否一样，不一样，则清空es，然后再插入，如果一样，则直接跳过，不用做迁移了
        sql_t_log_cash_count = 'SELECT COUNT(1) FROM T_LOG_DEBITDETAILM' + cchsmonth + ' where cchssettdate='+cchssettdate+' and cchserrcode=0'
        curs_core_for_count = conn_core.cursor()
        count = curs_core_for_count.execute(sql_t_log_cash_count)
        sum_in_oracle = curs_core_for_count.fetchone()[0]
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://' + es_ip + ':' + es_port + '/' + es_index + '/bus/_count', headers=headers,
                                 data='{"query": {"match" : {"cchssettdate": "'+cchssettdate+'"}}}')
        row_dict = dict()
        row_dict = json.loads(response.text)
        sum_in_es = row_dict['count']
        # 比较数据库与es的数据，不相等清空es，然后再插入
        if sum_in_oracle != sum_in_es:
            headers = {'Content-Type': 'application/json'}
            response = requests.post('http://' + es_ip + ':' + es_port + '/' + es_index + '/bus/_delete_by_query?conflicts=proceed',
                                     headers=headers,
                                     data='{"query": {"match" : {"cchssettdate": "'+cchssettdate+'"}}}')
            for row in rr:
                print(row)
                insert_into_es(row)
        else:
            print('es no change')
    except:
        print('Exception!!!')
    finally:
        curs_core_for_count.close()
        curs_core.close()
        conn_core.close()
