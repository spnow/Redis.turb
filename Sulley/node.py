from sulley import *

def init():
    s_initialize("append") #APPEND key "value">>
    s_static("APPEND")
    s_delim(" ")
    s_string("key")
    s_delim(" ")
    s_delim("\"")
    s_string("value")
    s_delim("\"")
    s_static("\r\n\r\n")

    s_initialize("auth") #AUTH password>>
    s_static("AUTH")
    s_delim(" ")
    s_string("password")
    s_static("\r\n\r\n")

    s_initialize("bgrewriteaof")
    s_static("BGREWRITEAOF")
    s_static("\r\n\r\n")

    s_initialize("bgsave") #BGSAVE>>
    s_static("BGSAVE")
    s_static("\r\n\r\n")

    s_initialize("bitcount") #BITCOUNT key 0 1>>
    s_static("BITCOUNT")
    s_delim(" ")
    s_string("key")
    s_delim(" ")
    s_string("0")
    s_delim(" ")
    s_string("1")
    s_static("\r\n\r\n")

    s_initialize("bitop")
    s_static("BITOP")
    s_static("\r\n\r\n")

    s_initialize("bitpos")
    s_static("BITPOS")
    s_static("\r\n\r\n")

    s_initialize("blpop")
    s_static("BLPOP")
    s_static("\r\n\r\n")

    s_initialize("brpop")
    s_static("BRPOP")
    s_static("\r\n\r\n")

    s_initialize("brpoplpush")
    s_static("BRPOPLPUSH")
    s_static("\r\n\r\n")

    s_initialize("client kill") #CLIENT KILL 123.123.123.123:1234>>
    s_static("CLIENT KILL")
    s_delim(" ")
    s_string("123.123.123.123:1234")
    s_static("\r\n\r\n")

    s_initialize("client list")
    s_static("CLIENT LIST")
    s_static("\r\n\r\n")

    s_initialize("client getname") #CLIENT GETNAME>>
    s_static("CLIENT GETNAME")
    s_static("\r\n\r\n")

    s_initialize("client pause") #CLIENT PAUSE 10>>
    s_static("CLIENT PAUSE")
    s_delim(" ")
    s_string("10")
    s_static("\r\n\r\n")

    s_initialize("client setname") #CLIENT SETNAME name>>
    s_static("CLIENT SETNAME")
    s_delim(" ")
    s_string("name")
    s_static("\r\n\r\n")

    s_initialize("cluster addslots")
    s_static("CLUSTER ADDSLOTS")
    s_static("\r\n\r\n")

    s_initialize("cluster count-failure-reports")
    s_static("CLUSTER COUNT-FAILURE-REPORTS")
    s_static("\r\n\r\n")

    s_initialize("cluster countkeysinslot")
    s_static("CLUSTER COUNTKEYSINSLOT")
    s_static("\r\n\r\n")

    s_initialize("cluster delslots")
    s_static("CLUSTER DELSLOTS")
    s_static("\r\n\r\n")

    s_initialize("cluster failover")
    s_static("CLUSTER FAILOVER")
    s_static("\r\n\r\n")

    s_initialize("cluster forget")
    s_static("CLUSTER FORGET")
    s_static("\r\n\r\n")

    s_initialize("cluster getkeysinslot")
    s_static("CLUSTER GETKEYSINSLOT")
    s_static("\r\n\r\n")

    s_initialize("cluster info")
    s_static("CLUSTER INFO")
    s_static("\r\n\r\n")

    s_initialize("cluster keyslot")
    s_static("CLUSTER KEYSLOT")
    s_static("\r\n\r\n")

    s_initialize("cluster meet")
    s_static("CLUSTER MEET")
    s_static("\r\n\r\n")

    s_initialize("cluster nodes")
    s_static("CLUSTER NODES")
    s_static("\r\n\r\n")

    s_initialize("cluster replicate")
    s_static("CLUSTER REPLICATE")
    s_static("\r\n\r\n")

    s_initialize("cluster reset")
    s_static("CLUSTER RESET")
    s_static("\r\n\r\n")

    s_initialize("cluster saveconfig")
    s_static("CLUSTER SAVECONFIG")
    s_static("\r\n\r\n")

    s_initialize("cluster set-config-epoch")
    s_static("CLUSTER SET-CONFIG-EPOCH")
    s_static("\r\n\r\n")

    s_initialize("cluster setslot")
    s_static("CLUSTER SETSLOT")
    s_static("\r\n\r\n")

    s_initialize("cluster slaves")
    s_static("CLUSTER SLAVES")
    s_static("\r\n\r\n")

    s_initialize("cluster slots")
    s_static("CLUSTER SLOTS")
    s_static("\r\n\r\n")

    s_initialize("command")
    s_static("COMMAND")
    s_static("\r\n\r\n")

    s_initialize("command count")
    s_static("COMMAND COUNT")
    s_static("\r\n\r\n")

    s_initialize("command getkeys")
    s_static("COMMAND GETKEYS")
    s_static("\r\n\r\n")

    s_initialize("command info")
    s_static("COMMAND INFO")
    s_static("\r\n\r\n")

    s_initialize("config get")
    s_static("CONFIG GET")
    s_static("\r\n\r\n")

    s_initialize("config rewrite")
    s_static("CONFIG REWRITE")
    s_static("\r\n\r\n")

    s_initialize("config set")
    s_static("CONFIG SET")
    s_static("\r\n\r\n")

    s_initialize("config resetstat")
    s_static("CONFIG RESETSTAT")
    s_static("\r\n\r\n")

    s_initialize("dbsize")
    s_static("DBSIZE")
    s_static("\r\n\r\n")

    s_initialize("debug object")
    s_static("DEBUG OBJECT")
    s_static("\r\n\r\n")

    s_initialize("debug segfault")
    s_static("DEBUG SEGFAULT")
    s_static("\r\n\r\n")

    s_initialize("decr")
    s_static("DECR")
    s_static("\r\n\r\n")

    s_initialize("decrby")
    s_static("DECRBY")
    s_static("\r\n\r\n")

    s_initialize("del")
    s_static("DEL")
    s_static("\r\n\r\n")

    s_initialize("discard")
    s_static("DISCARD")
    s_static("\r\n\r\n")

    s_initialize("dump")
    s_static("DUMP")
    s_static("\r\n\r\n")

    s_initialize("echo")
    s_static("ECHO")
    s_static("\r\n\r\n")

    s_initialize("eval")
    s_static("EVAL")
    s_static("\r\n\r\n")

    s_initialize("evalsha")
    s_static("EVALSHA")
    s_static("\r\n\r\n")

    s_initialize("exec")
    s_static("EXEC")
    s_static("\r\n\r\n")

    s_initialize("exists")
    s_static("EXISTS")
    s_static("\r\n\r\n")

    s_initialize("expire")
    s_static("EXPIRE")
    s_static("\r\n\r\n")

    s_initialize("expireat")
    s_static("EXPIREAT")
    s_static("\r\n\r\n")

    s_initialize("flushall")
    s_static("FLUSHALL")
    s_static("\r\n\r\n")

    s_initialize("flushdb")
    s_static("FLUSHDB")
    s_static("\r\n\r\n")

    s_initialize("geoadd")
    s_static("GEOADD")
    s_static("\r\n\r\n")

    s_initialize("geohash")
    s_static("GEOHASH")
    s_static("\r\n\r\n")

    s_initialize("geopos")
    s_static("GEOPOS")
    s_static("\r\n\r\n")

    s_initialize("geodist")
    s_static("GEODIST")
    s_static("\r\n\r\n")

    s_initialize("georadius")
    s_static("GEORADIUS")
    s_static("\r\n\r\n")

    s_initialize("georadiusbymember")
    s_static("GEORADIUSBYMEMBER")
    s_static("\r\n\r\n")

    s_initialize("get")
    s_static("GET")
    s_static("\r\n\r\n")

    s_initialize("getbit")
    s_static("GETBIT")
    s_static("\r\n\r\n")

    s_initialize("getrange")
    s_static("GETRANGE")
    s_static("\r\n\r\n")

    s_initialize("getset")
    s_static("GETSET")
    s_static("\r\n\r\n")

    s_initialize("hdel")
    s_static("HDEL")
    s_static("\r\n\r\n")

    s_initialize("hexists")
    s_static("HEXISTS")
    s_static("\r\n\r\n")

    s_initialize("hget")
    s_static("HGET")
    s_static("\r\n\r\n")

    s_initialize("hgetall")
    s_static("HGETALL")
    s_static("\r\n\r\n")

    s_initialize("hincrby")
    s_static("HINCRBY")
    s_static("\r\n\r\n")

    s_initialize("hincrbyfloat")
    s_static("HINCRBYFLOAT")
    s_static("\r\n\r\n")

    s_initialize("hkeys")
    s_static("HKEYS")
    s_static("\r\n\r\n")

    s_initialize("hlen")
    s_static("HLEN")
    s_static("\r\n\r\n")

    s_initialize("hmget")
    s_static("HMGET")
    s_static("\r\n\r\n")

    s_initialize("hmset")
    s_static("HMSET")
    s_static("\r\n\r\n")

    s_initialize("hset")
    s_static("HSET")
    s_static("\r\n\r\n")

    s_initialize("hsetnx")
    s_static("HSETNX")
    s_static("\r\n\r\n")

    s_initialize("hstrlen")
    s_static("HSTRLEN")
    s_static("\r\n\r\n")

    s_initialize("hvals")
    s_static("HVALS")
    s_static("\r\n\r\n")

    s_initialize("incr")
    s_static("INCR")
    s_static("\r\n\r\n")

    s_initialize("incrby")
    s_static("INCRBY")
    s_static("\r\n\r\n")

    s_initialize("incrbyfloat")
    s_static("INCRBYFLOAT")
    s_static("\r\n\r\n")

    s_initialize("info")
    s_static("INFO")
    s_static("\r\n\r\n")

    s_initialize("keys")
    s_static("KEYS")
    s_static("\r\n\r\n")

    s_initialize("lastsave")
    s_static("LASTSAVE")
    s_static("\r\n\r\n")

    s_initialize("lindex")
    s_static("LINDEX")
    s_static("\r\n\r\n")

    s_initialize("linsert")
    s_static("LINSERT")
    s_static("\r\n\r\n")

    s_initialize("llen")
    s_static("LLEN")
    s_static("\r\n\r\n")

    s_initialize("lpop")
    s_static("LPOP")
    s_static("\r\n\r\n")

    s_initialize("lpush")
    s_static("LPUSH")
    s_static("\r\n\r\n")

    s_initialize("lpushx")
    s_static("LPUSHX")
    s_static("\r\n\r\n")

    s_initialize("lrange")
    s_static("LRANGE")
    s_static("\r\n\r\n")

    s_initialize("lrem")
    s_static("LREM")
    s_static("\r\n\r\n")

    s_initialize("lset")
    s_static("LSET")
    s_static("\r\n\r\n")

    s_initialize("ltrim")
    s_static("LTRIM")
    s_static("\r\n\r\n")

    s_initialize("mget")
    s_static("MGET")
    s_static("\r\n\r\n")

    s_initialize("migrate")
    s_static("MIGRATE")
    s_static("\r\n\r\n")

    s_initialize("monitor")
    s_static("MONITOR")
    s_static("\r\n\r\n")

    s_initialize("move")
    s_static("MOVE")
    s_static("\r\n\r\n")

    s_initialize("mset")
    s_static("MSET")
    s_static("\r\n\r\n")

    s_initialize("msetnx")
    s_static("MSETNX")
    s_static("\r\n\r\n")

    s_initialize("multi")
    s_static("MULTI")
    s_static("\r\n\r\n")

    s_initialize("object")
    s_static("OBJECT")
    s_static("\r\n\r\n")

    s_initialize("persist")
    s_static("PERSIST")
    s_static("\r\n\r\n")

    s_initialize("pexpire")
    s_static("PEXPIRE")
    s_static("\r\n\r\n")

    s_initialize("pexpireat")
    s_static("PEXPIREAT")
    s_static("\r\n\r\n")

    s_initialize("pfadd")
    s_static("PFADD")
    s_static("\r\n\r\n")

    s_initialize("pfcount")
    s_static("PFCOUNT")
    s_static("\r\n\r\n")

    s_initialize("pfmerge")
    s_static("PFMERGE")
    s_static("\r\n\r\n")

    s_initialize("ping")
    s_static("PING")
    s_static("\r\n\r\n")

    s_initialize("psetex")
    s_static("PSETEX")
    s_static("\r\n\r\n")

    s_initialize("psubscribe")
    s_static("PSUBSCRIBE")
    s_static("\r\n\r\n")

    s_initialize("pubsub")
    s_static("PUBSUB")
    s_static("\r\n\r\n")

    s_initialize("pttl")
    s_static("PTTL")
    s_static("\r\n\r\n")

    s_initialize("publish")
    s_static("PUBLISH")
    s_static("\r\n\r\n")

    s_initialize("punsubscribe")
    s_static("PUNSUBSCRIBE")
    s_static("\r\n\r\n")

    s_initialize("quit")
    s_static("QUIT")
    s_static("\r\n\r\n")

    s_initialize("randomkey")
    s_static("RANDOMKEY")
    s_static("\r\n\r\n")

    s_initialize("readonly")
    s_static("READONLY")
    s_static("\r\n\r\n")

    s_initialize("readwrite")
    s_static("READWRITE")
    s_static("\r\n\r\n")

    s_initialize("rename")
    s_static("RENAME")
    s_static("\r\n\r\n")

    s_initialize("renamenx")
    s_static("RENAMENX")
    s_static("\r\n\r\n")

    s_initialize("restore")
    s_static("RESTORE")
    s_static("\r\n\r\n")

    s_initialize("role")
    s_static("ROLE")
    s_static("\r\n\r\n")

    s_initialize("rpop")
    s_static("RPOP")
    s_static("\r\n\r\n")

    s_initialize("rpoplpush")
    s_static("RPOPLPUSH")
    s_static("\r\n\r\n")

    s_initialize("rpush")
    s_static("RPUSH")
    s_static("\r\n\r\n")

    s_initialize("rpushx")
    s_static("RPUSHX")
    s_static("\r\n\r\n")

    s_initialize("sadd")
    s_static("SADD")
    s_static("\r\n\r\n")

    s_initialize("save")
    s_static("SAVE")
    s_static("\r\n\r\n")

    s_initialize("scard")
    s_static("SCARD")
    s_static("\r\n\r\n")

    s_initialize("script exists")
    s_static("SCRIPT EXISTS")
    s_static("\r\n\r\n")

    s_initialize("script flush")
    s_static("SCRIPT FLUSH")
    s_static("\r\n\r\n")

    s_initialize("script kill")
    s_static("SCRIPT KILL")
    s_static("\r\n\r\n")

    s_initialize("script load")
    s_static("SCRIPT LOAD")
    s_static("\r\n\r\n")

    s_initialize("sdiff")
    s_static("SDIFF")
    s_static("\r\n\r\n")

    s_initialize("sdiffstore")
    s_static("SDIFFSTORE")
    s_static("\r\n\r\n")

    s_initialize("select")
    s_static("SELECT")
    s_static("\r\n\r\n")

    s_initialize("set") #SET key value EX 10
    s_static("SET")
    s_delim(" ")
    s_string("key")
    s_delim(" ")
    s_string("value")
    s_delim(" ")
    s_static("EX")
    s_delim(" ")
    s_string("10")
    s_static("\r\n\r\n")

    s_initialize("setbit")
    s_static("SETBIT")
    s_static("\r\n\r\n")

    s_initialize("setex")
    s_static("SETEX")
    s_static("\r\n\r\n")

    s_initialize("setnx")
    s_static("SETNX")
    s_static("\r\n\r\n")

    s_initialize("setrange")
    s_static("SETRANGE")
    s_static("\r\n\r\n")

    s_initialize("shutdown")
    s_static("SHUTDOWN")
    s_static("\r\n\r\n")

    s_initialize("sinter")
    s_static("SINTER")
    s_static("\r\n\r\n")

    s_initialize("sinterstore")
    s_static("SINTERSTORE")
    s_static("\r\n\r\n")

    s_initialize("sismember")
    s_static("SISMEMBER")
    s_static("\r\n\r\n")

    s_initialize("slaveof")
    s_static("SLAVEOF")
    s_static("\r\n\r\n")

    s_initialize("slowlog")
    s_static("SLOWLOG")
    s_static("\r\n\r\n")

    s_initialize("smembers")
    s_static("SMEMBERS")
    s_static("\r\n\r\n")

    s_initialize("smove")
    s_static("SMOVE")
    s_static("\r\n\r\n")

    s_initialize("sort")
    s_static("SORT")
    s_static("\r\n\r\n")

    s_initialize("spop")
    s_static("SPOP")
    s_static("\r\n\r\n")

    s_initialize("srandmember")
    s_static("SRANDMEMBER")
    s_static("\r\n\r\n")

    s_initialize("srem")
    s_static("SREM")
    s_static("\r\n\r\n")

    s_initialize("strlen")
    s_static("STRLEN")
    s_static("\r\n\r\n")

    s_initialize("subscribe")
    s_static("SUBSCRIBE")
    s_static("\r\n\r\n")

    s_initialize("sunion")
    s_static("SUNION")
    s_static("\r\n\r\n")

    s_initialize("sunionstore")
    s_static("SUNIONSTORE")
    s_static("\r\n\r\n")

    s_initialize("sync")
    s_static("SYNC")
    s_static("\r\n\r\n")

    s_initialize("time")
    s_static("TIME")
    s_static("\r\n\r\n")

    s_initialize("ttl")
    s_static("TTL")
    s_static("\r\n\r\n")

    s_initialize("type")
    s_static("TYPE")
    s_static("\r\n\r\n")

    s_initialize("unsubscribe")
    s_static("UNSUBSCRIBE")
    s_static("\r\n\r\n")

    s_initialize("unwatch")
    s_static("UNWATCH")
    s_static("\r\n\r\n")

    s_initialize("wait")
    s_static("WAIT")
    s_static("\r\n\r\n")

    s_initialize("watch")
    s_static("WATCH")
    s_static("\r\n\r\n")

    s_initialize("zadd")
    s_static("ZADD")
    s_static("\r\n\r\n")

    s_initialize("zcard")
    s_static("ZCARD")
    s_static("\r\n\r\n")

    s_initialize("zcount")
    s_static("ZCOUNT")
    s_static("\r\n\r\n")

    s_initialize("zincrby")
    s_static("ZINCRBY")
    s_static("\r\n\r\n")

    s_initialize("zinterstore")
    s_static("ZINTERSTORE")
    s_static("\r\n\r\n")

    s_initialize("zlexcount")
    s_static("ZLEXCOUNT")
    s_static("\r\n\r\n")

    s_initialize("zrange")
    s_static("ZRANGE")
    s_static("\r\n\r\n")

    s_initialize("zrangebylex")
    s_static("ZRANGEBYLEX")
    s_static("\r\n\r\n")

    s_initialize("zrevrangebylex")
    s_static("ZREVRANGEBYLEX")
    s_static("\r\n\r\n")

    s_initialize("zrangebyscore")
    s_static("ZRANGEBYSCORE")
    s_static("\r\n\r\n")

    s_initialize("zrank")
    s_static("ZRANK")
    s_static("\r\n\r\n")

    s_initialize("zrem")
    s_static("ZREM")
    s_static("\r\n\r\n")

    s_initialize("zremrangebylex")
    s_static("ZREMRANGEBYLEX")
    s_static("\r\n\r\n")

    s_initialize("zremrangebyrank")
    s_static("ZREMRANGEBYRANK")
    s_static("\r\n\r\n")

    s_initialize("zremrangebyscore")
    s_static("ZREMRANGEBYSCORE")
    s_static("\r\n\r\n")

    s_initialize("zrevrange")
    s_static("ZREVRANGE")
    s_static("\r\n\r\n")

    s_initialize("zrevrangebyscore")
    s_static("ZREVRANGEBYSCORE")
    s_static("\r\n\r\n")

    s_initialize("zrevrank")
    s_static("ZREVRANK")
    s_static("\r\n\r\n")

    s_initialize("zscore")
    s_static("ZSCORE")
    s_static("\r\n\r\n")

    s_initialize("zunionstore")
    s_static("ZUNIONSTORE")
    s_static("\r\n\r\n")

    s_initialize("scan")
    s_static("SCAN")
    s_static("\r\n\r\n")

    s_initialize("sscan")
    s_static("SSCAN")
    s_static("\r\n\r\n")

    s_initialize("hscan")
    s_static("HSCAN")
    s_static("\r\n\r\n")

    s_initialize("zscan")
    s_static("ZSCAN")
    s_static("\r\n\r\n")
