import requests
import json

es_ip = '127.0.0.1'
es_port = '9200'

#GET
# print(requests.get('http://www.baidu.com').text)

#POST
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# #查询所有索引
# print(requests.get('http://'+es_ip+':'+es_port+'/_cat/health?v').text)
#
# #检查ES节点状态：
# print(requests.get('http://'+es_ip+':'+es_port+'/_cat/nodes?v').text)
#
# #查询所有索引
# print(requests.get('http://'+es_ip+':'+es_port+'/_cat/indices?v').text)

# response = requests.get('http://'+es_ip+':'+es_port+'/t_log_cash_test2')
# print(response.status_code)

# _index_mappings = {
#     'mappings':{
# #         "bus":{
# #             "properties": {
# #                 "settdate": {
# #                     "type": "keyword"
# #                 },
# #                 "censeq": {
# #                     "type": "keyword"
# #                 },
# #                 "termid": {
# #                     "type": "text"
#                 },
#                 "txndate": {
#                     "type": "text"
#                 },
#                 "txntime": {
#                     "type": "text"
#                 }
#             }
#         }
#     }
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.put('http://'+es_ip+':'+es_port+'/t_log_cash_test3/bus/3', headers=headers, data=json.dumps(_index_mappings))
# print(response)
# print(response.text)

# print(requests.delete('http://'+es_ip+':'+es_port+'/t_log_cash_test3').text)

# print(requests.get('http://'+es_ip+':'+es_port+'/book/_id/GGE4mmkBZ0bZ5jInRZJR').text)
print(requests.get('http://'+es_ip+':'+es_port+'/t_log_cash_test5/_search?q=*&pretty').text)