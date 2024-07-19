#!/usr/bin/python

"""
Pyifconfig v1.1

Coded by: ViCoder32

Util for get data about your global and local ip, also 
you can get ip ranges and export data in json format

"""
# I am semolina :>>
###########################################################
import json
import requests
import sys
from subprocess import getoutput
import socket


def get_info_ipv4():
    try:
        res = requests.get("https://ifconfig.me/ip")
        ip = res.text
        if len(ip) < 16:
            ipv4 = "v4" + ip
            return ipv4     
        else:
            ipv6 = "v6" + ip
            return ipv6
    except:
        return "None"
def creat_range(ip):
    if ip.startswith("v6"):
        ip = ip[2:] + "/64"
        return ip
    elif ip.startswith("v4"):
        ip = ip[2:] + "/24"
        return ip
    else:
        return None
def get_local_ipv4():
    try:    
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = "v4" + s.getsockname()[0]
        return ip
    except:
        return "None"


def output():
    local_ip = get_local_ipv4()[2:]
    ip = get_info_ipv4()[2:]  
    local_range = creat_range(get_local_ipv4())
    global_range = creat_range(get_info_ipv4())
    print(f"""
Pyifconfig v1.0

        
    Global ip: {ip}  
            
    Local ip: {local_ip} 
            
    Global range: {global_range}
            
    Local range: {local_range}    


          """) 

def parse_argument(key):
    try: 
        index = sys.argv.index(key) + 1
        option = sys.argv[index]
        return option
    
    except:
        return None

def man_page():
    print("""
Pyifconfig v1.0
Coded by: ViCoder32
    
    Simple, but effective util for definition ipv4 in LAN&WAN, also print ip ranges and have function for export data in JSON format. 
    This util can help people which conducting pentest, setup network, or just want get need information for 2 seconds.
    Maybe in new commits will new functions


    --help 
        Print in terminal man page which see right now
    
    --json <path/filename>
        Saved data in good json format and print in stdout, also you can save 
        data in file
        
    None 
        Just print data in comfortable format, horewer this you should already know :>> 





          """)
    sys.exit()

def get_json():
    sip = get_info_ipv4()
    if sip.startswith("v4"): 
        ip = sip[2:]
        local_ip = get_local_ipv4()[2:] 
        ip_range = creat_range(get_info_ipv4())
        lrange = creat_range(get_local_ipv4())
        raw = [ip ,local_ip, lrange, ip_range]
        data = json.dumps(raw)    
        return data
    else:
        ip = sip[2:]
        local_ip = get_local_ipv4() 
        ip_range = creat_range(get_info_ipv4())
        lrange = creat_range(get_local_ipv4)
        raw = [ip ,local_ip, lrange, ip_range]
        data = json.dumps(raw)    
        return data

def argument_handler():
    if len(sys.argv) <= 1:
        output()
        sys.exit()
    elif "--help" in sys.argv:
        man_page()

    elif "--json" in sys.argv:
        option = parse_argument("--json")
        if option == None:
            sys.exit(get_json())
        else:
            if option.endswith(".json"):
                data = get_json()
                with open(option, "w") as f:
                    f.write(data)
                    sys.exit("Json file was created")
                 
            else:
                name = option + ".json"
                data = get_json()
                with open( name, "w") as f:
                    f.write(data)
                    sys.exit("Json file was created")
                                                    
    else:
        man_page()

def main():
    argument_handler()


if __name__ == '__main__':
    main()
