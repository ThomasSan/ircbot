from pybot import *
import os
import random
import time
import re
import math

host = "irc.root-me.org"
chan = "#root-me_challenge"
bot_name = "candy"

irc = IRC()
irc.connect(host, chan, "RototoRo")

def chall1(x):
    n1 = int(x.split(' / ')[0])
    n2 = int(x.split(' / ')[1])
    res = math.sqrt(n1) * n2
    return "{0:.2f}".format(res)

while 1:
    text = irc.get_text()
    if re.search('\d+\s\/\s\d+', text):
        x = re.search('\d+\s\/\s\d+', text).group()
        irc.send(bot_name, "!ep1 -rep " + chall1(x))
    print text
    time.sleep(5)
    irc.send(bot_name,"!ep1")
