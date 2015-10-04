from sulley import *
import node

# import nodes
node.init()

sess = sessions.session(session_filename="fuzz.session")
with open("fuzz.flow.udg", "w+") as hf:
    hf.write(sess.render_graph_udraw())

# Scenario
sess.connect(s_get("restore"))

target = sessions.target("192.168.109.138", 6379)
sess.add_target(target)
sess.fuzz()
