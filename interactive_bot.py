#!/usr/bin/env python

import aiml
import os
import sys

os.chdir('/home/jerrin/Downloads/program-ab-0.0.4.3/bots/super/aiml')
mybot = aiml.Kernel()
mybot.learn('startup.xml')
mybot.respond('load aiml b')

while True:
  print mybot.respond(raw_input("Enter"))

