import redis

r = redis.Redis(host='localhost', port=6379, db=0)
keys = r.keys('*')
values = r.mget(keys)
for key, value in zip(keys, values):
    print(f'{key.decode()}: {value.decode()}')
