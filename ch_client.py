from flask import Flask,jsonify,request,Response,json,Request
import requests
import json, bisect
import md5

"""Implement a consistent hashing ring."""
class ConsistentHashRing(object):

    def __init__(self, replicas=1):
        self.replicas = replicas
        self._keys = []
        self._nodes = {}

    def _hash(self, key):
        return long(md5.md5(key).hexdigest(), 16)

    def _repl_iterator(self, nodename):
        return (self._hash("%s:%s" % (nodename, i)) for i in xrange(self.replicas))

    def __setitem__(self, nodename, node):
        for hash_ in self._repl_iterator(nodename):
            if hash_ in self._nodes:
                raise ValueError("Node name %r is already present" % nodename)
            self._nodes[hash_] = node
            bisect.insort(self._keys, hash_)

    def __delitem__(self, nodename):
        for hash_ in self._repl_iterator(nodename):
            del self._nodes[hash_]
            index = bisect.bisect_left(self._keys, hash_)
            del self._keys[index]

    def __getitem__(self, key):
        hashed_key = self._hash(key)
        start = bisect.bisect(self._keys, hashed_key)
        if start == len(self._keys):
            start = 0
        return self._nodes[self._keys[start]]

#Initializing hashing ring Object
cr = ConsistentHashRing() 

cr.__setitem__("appinstance1","5000")
cr.__setitem__("appinstance2","6000")
cr.__setitem__("appinstance3","7000")


urllist = {}
for id in range(1,11):
    '''making the POST requests'''
    port = cr.__getitem__(str(id))
    url = "http://192.168.99.100:%s/v1/expenses" % (port)
    urllist[str(id)] = url
    payload = {
        "id": id,
        "name": "Foo %s"%(id),
        "email": "foo%s@bar.com"%(id),
        "category": "office supplies",
        "description": "iPad for office use",
        "link": "http://www.apple.com/shop/buy-ipad/ipad-pro",
        "estimated_costs": "700",
        "submit_date": "12-10-2016"
    } 

    r = requests.post(url, json=payload)
    
for id in range (1,11):
    '''making the GET requests'''
    port = cr.__getitem__(str(id))
    url = "http://192.168.99.100:%s/v1/expenses/%s" % (port,id)
    response = requests.get(url)
    #data = json.loads(response.content)
    print "Request: %s"%(id)
    print response.text

   


