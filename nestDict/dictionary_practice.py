import sys
import re
import argparse
def dictionary():
    f = open('C:\\Users\\danie\\Desktop\\msci 121\\scan_result (1).log')
    b = {}
    s = {}
    bb = {}
    boo = False
    pattern = "\->(\w+)\s=\s([\w:]+)"
    for line in f.readlines():
        
        if "-----------------------" in line:
                boo = True
                if s.get("bssid") is not None and len(s) == 7:
                    b[s["bssid"]] = s    
                    s = {}
            


        if "=" in line and boo:
            x = re.search(pattern, line)
            if x is not None:
                skey = x.group(1)
                s[skey] = x.group(2)
            # if "-ssid" in line:
            #     x = line.split(" = ")
            #     s["ssid"] = x[1].strip("\n")
            # else:
            #     line_current = line.split(" = ")
            #     line_current2 = line_current[0].split(">")
            #     #print(line_current[0])
            #     skey = line_current2[1]
            #     #creates keys for small dictionary
            #     sval = line_current[1].strip("\n")
            #     s[skey] = sval
    
    for key, value in b.items():
        print(key)
        for key2, value2 in value.items():
           print( "\t", key2, ":", value2)
dictionary()




