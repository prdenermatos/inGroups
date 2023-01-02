from elasticsearch7 import Elasticsearch
import json

def connect_db() -> Elasticsearch: 
    # return Elasticsearch("http://3.89.86.153:9200")
    return Elasticsearch("http://44.195.30.159:9200")



# filter = {
#   "query": {
#     "simple_query_string": {
#       "fields": [ "nome_fantasia" ],
#       "query": "mar"
#     }
#   }
# }

# filter2 = {
# 	"query":{
# 		"query_string":{
# 			"query":"(nome_fantasia:MAr)"
# 		}
# 	}
# }

# te = Elasticsearch("http://localhost:9200")
# result = te.search(index="estabelecimentos", 
#     body=filter2)
# print(result)