from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200, 'timeout': 3600}])
# a = es.search(index='book', q='author:"巴金"')
a = es.search(index='book', q='_id:"GGE4mmkBZ0bZ5jInRZJR"')
print(a)
