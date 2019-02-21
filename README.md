pyredis
![](https://img.shields.io/badge/python%20-%203.7-brightgreen.svg)
========
> provide redis api 

## `Install`
` pip install git+https://github.com/zhouxianggen/pyredis.git`

## `Upgrade`
` pip install --upgrade git+https://github.com/zhouxianggen/pyredis.git`

## `Uninstall`
` pip uninstall pyredis`

## `Basic Usage`
```python
from pyredis import PyRedis

r = PyRedis(host='localhost', port=6379, pswd='', db=1, 
        version='test', expiry=1)
r.set('foo', 'bar')
print(r.get('foo'))

```
