import json
import requests
import sys
from subprocess import getoutput
from termcolor import colored
import socket
def get_info_ipv4():
    res = requests.get("https://ifconfig.me/ip")
    ip = res.text
    return ip



def get_local_ipv4():
    try:    
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ip
    except:
        sys.exit(colored("[ERROR] Connect to network and try again" ,"red"))



def output():
    local_ip = get_local_ipv4()
    ip = get_info_ipv4()  
    local_range = local_ip + "/24"
    global_range = ip + "/24"
    print(f"""
Pyifconfig v 1.0

        
    Global ipv4: {ip}  
            
    Local ipv4: {local_ip} 
            
    Provider range: {global_range}
            
    Local ipv4: {local_range}


Note:    
    Add --json to get json
                  """) 
def get_json():
    local_ip = get_local_ipv4() 
    ip = get_info_ipv4()
    ip_range = ip + "/24"
    lrange = local_ip + "/24"
    raw = [ip ,local_ip, lrange, ip_range]
    data = json.dumps(raw)    
    return data
def main():
    if len(sys.argv) <= 1:
        output()
        sys.exit()
    elif "--json" in sys.argv:
        output = get_json()
        print(output)
    else:
        sys.exit(colored("[!] Invalid arguments" ,"red"))
if __name__ == '__main__':
    main()
