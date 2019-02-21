# coding: utf8 
from pyredis import PyRedis

r = PyRedis(host='192.168.9.226', port=6379, pswd='', db=1)
r.set('foo', 'bar')
print(r.get('foo'))

