# coding: utf8 
import hashlib
import redis


class PyRedis(object):
    def __init__(self, host, port, pswd, db, 
            version='', expiry=0, hash_key=False):
        self._redis = redis.StrictRedis(host=host, port=port, 
                password=pswd, db=db)
        self._version = version
        self._expiry = expiry
        self._hash_key = hash_key

    def mkkey(self, key):
        if type(key) == type(u''):
            key = key.encode('utf8')
        key = self._version + str(key)
        if self._hash_key:
            key = hashlib.md5(bytes(key, encoding='utf8')).hexdigest()
        return key

    def get(self, key, default=None):
        return self._redis.get(self.mkkey(key)) or default

    def set(self, key, value, expire=0):
        key = self.mkkey(key)
        self._redis.set(key, value)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)

    def incr(self, key, count=1, expire=0):
        key = self.mkkey(key)
        r = self._redis.incr(key, count)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)
        return r
    
    def hset(self, key, field, value, expire=0):
        key = self.mkkey(key)
        self._redis.hset(key, field, value)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)

    def hmset(self, key, values, expire=0):
        key = self.mkkey(key)
        self._redis.hmset(key, values)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)

    def hincrby(self, key, field, count=1, expire=0):
        key = self.mkkey(key)
        self._redis.hincrby(key, field, count)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)
    
    def mget(self, keys):
        return self._redis.mget([self.mkkey(key) for key in keys])

    def mset(self, keys_values, expire=0):
        self._redis.mset(keys_values)
        if expire or self._expiry:
            self._redis.expire(keys_values, expire or self._expiry)

    def hget(self, key, field):
        return self._redis.hget(self.mkkey(key), field)

    def hgetall(self, key):
        key = self.mkkey(key)
        return self._redis.hgetall(key)
    
    def hlen(self, key):
        key = self.mkkey(key)
        return self._redis.hlen(key)

    def delete(self, key):
        key = self.mkkey(key)
        return self._redis.delete(key)

    def lpush(self, key, value, expire=0):
        key = self.mkkey(key)
        r = self._redis.lpush(key, value)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)
        return r
    
    def rpush(self, key, value, expire=0):
        key = self.mkkey(key)
        r = self._redis.rpush(key, value)
        if expire or self._expiry:
            self._redis.expire(key, expire or self._expiry)
        return r

    def lpop(self, key):
        key = self.mkkey(key)
        return self._redis.lpop(key)

    def rpop(self, key):
        key = self.mkkey(key)
        return self._redis.rpop(key)

    def llen(self, key):
        key = self.mkkey(key)
        return self._redis.llen(key)

    def lrange(self, key, start, end):
        key = self.mkkey(key)
        return self._redis.lrange(key, start, end)
    
