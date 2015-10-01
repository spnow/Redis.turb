from sulley import *
import node

node.init()

sess = sessions.session(session_filename="redis.session")
target = sessions.target("192.168.109.135", 6379)

sess.connect(s_get("set"))

hf = open("flowchart.udg", "w+")
hf.write(sess.render_graph_udraw())
hf.close()

sess.add_target(target)
sess.fuzz()
