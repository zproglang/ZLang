#!/usr/bin/python3.11

from string import ascii_letters,digits
from sys import argv
# from time import sleep

rf=open(argv[1]) if len(argv) > 1 else exit()
cont=rf.readlines()
res=""
qot=""
val=""
write=False
ln=ch=0
var={}

while ln<len(cont):
  if cont[ln][ch]==" ":
    ch+=1
    res=""
    continue
  elif cont[ln][ch]=="\n":
    ln+=1
    ch=0
    res=""
    if write:
      write=False
      print()
    continue
  elif cont[ln][ch]==";":
    if write:
      write=False
      print()
    while cont[ln][ch]!="\n":
      ch+=1
    ln+=1
    ch=0
  elif cont[ln][ch]=="/":
    if write:
      write=False
      print()
    while cont[ln][ch]!="\\":
      ch+=1
      if cont[ln][ch]=="\n":
        ln+=1
        ch=0
    ch+=1
  elif cont[ln][ch]=="%":
    res=""
    ch+=1
    while cont[ln][ch] in ascii_letters:
      res+=cont[ln][ch]
      ch+=1
    if write:
      print(var[res],end="")
      # sleep(1)
    res=""
  elif cont[ln][ch] in "\"'":
    qot=cont[ln][ch]
    ch+=1
    while cont[ln][ch] != qot:
      res+=cont[ln][ch]
      ch+=1
    if write:
      print(res,end="")
      res=""
      # sleep(1)
    ch+=1
  elif cont[ln][ch] in ascii_letters:
    while cont[ln][ch] in ascii_letters:
      res+=cont[ln][ch]
      ch+=1
    res=res.lower()
    if res=="print":
      write=True
      res=""
    elif res=="set":
      ch+=1
      res=""
      while cont[ln][ch] in ascii_letters:
        res+=cont[ln][ch]
        ch+=1
      if cont[ln][ch]==" ":
        ch+=1
        if cont[ln][ch] in "\"'":
          qot=cont[ln][ch]
          ch+=1
          while cont[ln][ch]!=qot:
            val+=cont[ln][ch]
            ch+=1
          var[res]=val
          res=""
          val=""
          qot=""
          ln+=1
          ch=0
        if cont[ln][ch] in digits:
          while cont[ln][ch] in digits:
            val+=cont[ln][ch]
            ch+=1
          var[res]=int(val)
          res=""
          val=""
          ln+=1
          ch=0
    elif res=="go":
      res=""
      ch+=1
      if cont[ln][ch]==" ":
        ch+=1
      while cont[ln][ch] in digits:
        res+=cont[ln][ch]
        ch+=1
      ln=int(res)-1
      res=""
      ch=0
    else:
      print("\nL:%d:Unexpected token: `%s'" % (ln,res))
      exit()
  else:
    print("\nL:%d:Unexpected token: `%s'" % (ln,cont[ln][ch]))
    exit()
