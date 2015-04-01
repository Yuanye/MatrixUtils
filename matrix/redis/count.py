# -*- coding: utf-8 -*- 

class Counter(object):

    def __init__(self, redis, name=None):
        self.redis = redis
        self.name = name 
        
    def _byID(self, key):
        if not self.name:
            return self.redis.get(key)
        return self.redis.hget(self.name, key)

    def _incr(self, key, value=1):
        if not self.name:
            return self.redis.incrby(key, value)
        return self.redis.hincrby(self.name, key, value)

    def _decr(self, key, value):
        if not self.name:
            return self.redis.decrby(key, value)
        return self.redis.hincrby(self.name, key, -value)

class SetCounter(object):
    """
        Set Counter
    """

    def __init__(self, redis, name):
        self.redis = redis
        self.name = name 

    def add(self, value):
        return self.redis.sadd(self.name, value)

    @property
    def count(self):
        return self.redis.scard(self.name)

    def delete(self, value):
        return self.redis.srem(self.name, value)

if __name__ == "__main__":
    pass

