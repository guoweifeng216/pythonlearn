import json
r = input("input:")
dic = json.load(r)
bk = dic['backend']
rd = "server %s %s weight %d maxcon %d"%(dic['record']['server'],
                                              )