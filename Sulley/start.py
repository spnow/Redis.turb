from sulley import *
import node

# import nodes
node.init()

sess = sessions.session(session_filename="fuzz.session")
with open("fuzz.flow.udg", "w+") as hf:
    hf.write(sess.render_graph_udraw())

# Scenario
sess.connect(s_get("restore"))
sess.connect(s_get("set"), s_get("append"))
sess.connect(s_get("rpush"), s_get("lpush"))
sess.connect(s_get("lpush"), s_get("rpush"))

target = sessions.target("192.168.109.138", 6379)
sess.add_target(target)
sess.fuzz()
