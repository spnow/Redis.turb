# Redisturb
## Redis.io Penetration Testing 

##### Intro

*Redis.io* is an open source in-memory database developed to store volatile data like messages, cache, cookie, etc.

##### Misconfiguration

I beg you to read [url:redis.io/security](http://redis.io/topics/security) if you have any intention to setup *Redis.io* in production mode.

##### discover misconfigured *Redis.io* using *Shodan* and *Nmap*

*Shodan* give us a powerful tool to find several misconfigured servers.

` { product:"Redis key-value store", port:"6379" } `

#### Security Best Practice
Add to **redis.conf**

`bind 127.0.0.1`

Allow access only from loopback (implied that the application that needs *Redis.io* running on the same host).
