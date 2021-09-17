import redis
import json
redis = redis.StrictRedis(host='localhost', port=6379, charset='utf-8', decode_responses=True, db=0)

redis.set('A', 'candidato 1')
redis.set('B', 'candidato 2')
redis.set('C', 'candidato 3')
redis.set('D', 'candidato 4')
redis.set('E', 'candidato 5')
redis.set('F', 'candidato 6')
redis.set('G', redis.get('A') + ' Ollyver')

mydict = { 'var1' : 5, 'var2' : 9, 'var3': [1, 5, 9] }
rval = json.dumps(mydict)
redis.set('key1', rval)

data = redis.get('key1')
print(data)
result = json.loads(data)
arr = result['var3']
print(result)
print(arr)