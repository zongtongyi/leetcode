#! /usr/bin/env python
# -*- coding:utf-8 -*-
# by Peng Wang 2017-06-12 12:33:50

class Codec:

    import string
    dict_longUrls = {}
    dict_shortUrls = {}
    alphabeat = string.ascii_letters + string.digits
    global_count = 0
    prefix = "http://tinyurl.com/"

    def encode(self, longUrl):

        def enco64(num):
            tiny = ''
            while True:
                tiny = self.alphabeat[num % 62] + tiny
                num //= 62
                if not num:
                    break
            return tiny

        if longUrl in self.dict_longUrls:
            return self.prefix + self.dict_longUrls[longUrl]
        else:
            tiny = enco64(self.global_count)
            self.dict_longUrls[longUrl] = tiny
            self.dict_shortUrls[tiny] = longUrl
            self.global_count += 1
            return self.prefix + tiny

    def decode(self, shortUrl):
        tiny = shortUrl.split('/')[-1]
        return '' if tiny not in self.dict_shortUrls else self.dict_shortUrls[tiny]

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = 'http://2352545.me/asdf/uyp.html'
enurl = codec.encode(url)
print enurl
enurl = codec.encode(url+'as')
print enurl

print codec.decode(enurl)

