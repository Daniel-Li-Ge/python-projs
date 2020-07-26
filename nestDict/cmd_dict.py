import re
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument('-s','--ssid', type=str, help ='Type the name of an SSID', default=None)
parser.add_argument('-l','--list_all', type=str, help='Type any string to Get a list of SSIDs available')
args = parser.parse_args()

#user_give = input('Please give a file path to your WIFI log')

f = open('C:\\Users\\danie\\Desktop\\msci 121\\WIFILOGS.log')


def dictionary(ssid=None):
    b = {}
    s = {}
    boo = False
    boo2 = False
    l = []
    pattern = "\->(\w+)\s=\s([\-\w: ]+)"
    for line in f.readlines():  
        if "-----------------------" in line:
            boo = True
            if ssid is not None:
                boo2 = True
                if s.get("ssid") is not None and len(s) == 8:
                    current_ssid = s.get("ssid")
                    list_of_keys = b.keys() 
                    b[s["ssid"]] = l
                    if current_ssid in list_of_keys and b.get(ssid) is not None and ssid == s["ssid"]:
                        return_list = b.get(ssid)
                        return_list.append(s)
                    else:
                        b[s["ssid"]] = [s]
                    s={} 
                    
        if "=" in line and boo:
            x = re.search(pattern, line)
            if x is not None:
                skey = x.group(1)
                s[skey] = x.group(2)
                if len(s) == 8 and boo2 == False: 
                    print("==============")
                    for printkey, printitem in s.items():
                        print(printkey, ": ", printitem)
                        s={}

    unpack = b.get(ssid)
    if unpack is not None:
        print('Amount of non-unique ssid(s): ', len(unpack))
        for i in unpack:    
            print("================")
            for k, v in i.items():
                print(k, ": ", v)

def list_ssid(ac=None):
    if ac: 
        pattern =  pattern = "\->ssid\s=\s([\w: ]+)"
        for line in f.readlines():
            y = re.search(pattern, line)
            if y is not None:
                print(y.group(1))


list_ssid(args.list_all)
dictionary(args.ssid)

