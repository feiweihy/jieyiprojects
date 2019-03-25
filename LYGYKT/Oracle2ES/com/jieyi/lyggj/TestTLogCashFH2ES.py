import cx_Oracle
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200, 'timeout': 3600}])


def create_index():
    # _index_mappings = {
    #     "mappings": {
    #         'bus': {
    #             "properties": {
    #                 "settdate": {
    #                     "type": "text",
    #                     "index": "not_analyzed"
    #                 },
    #                 "censeq": {
    #                     "type": "text",
    #                     "index": True
    #                 },
    #                 "termid": {
    #                     "type": "string",
    #                     "index": "not_analyzed"
    #                 },
    #                 "txndate": {
    #                     "type": "string",
    #                     "index": "not_analyzed"
    #                 },
    #                 "txntime": {
    #                     "type": "string",
    #                     "index": "not_analyzed"
    #                 }
    #             }
    #         }
    #
    #     }
    # }

    _index_mappings = {
        "bus":{
            "properties": {
                "settdate": {
                    "type": "keyword"
                },
                "censeq": {
                    "type": "keyword"
                },
                "termid": {
                    "type": "text"
                },
                "txndate": {
                    "type": "text"
                },
                "txntime": {
                    "type": "text"
                }
            }
        }

    }

    if es.indices.exists(index='t_log_cashsv111') is not True:
        res = es.indices.create(index='t_log_cashsv111', body={'mappings': _index_mappings})
        print(11)
        print(res)
    else:
        print(33)


# create_index()

print(es.search(index='book', q='*'))

conn_core = cx_Oracle.connect('jtb_lygbus/111111@192.168.1.96:1521/orcl')
curs_core = conn_core.cursor()
sql_t_log_cash = 'SELECT * FROM T_LOG_CASHFH'
rr = curs_core.execute(sql_t_log_cash)
row = curs_core.fetchone()
print(row)
curs_core.close()
conn_core.close()
