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
Pyifconfig v1.0

        
    Global ipv4: {ip}  
            
    Local ipv4: {local_ip} 
            
    Provider range: {global_range}
            
    Local ipv4: {local_range}    
                      """) 

def parse_argument(key):
    index = sys.argv.index(key) + 1
    option = sys.argv[index]
    return option

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
        option = parse_argument("--json")
        if option != None:
            if option.endswith(".json"):
                with open(option, "w") as f:
                    f.write(output)
                    if "/" in option:
                        print(f"Json file saved to {option}")
                        sys.exit()
                    else:
                        print(f"Json file was created {option}")
            else:
                option = option + ".json"
                with open(option, "w") as f:
                    f.write(option)
                    if "/" in option:
                        print(f"Json file saved to {option}")
                        sys.exit()
                    elif '/' not in option:
                        print(f"Json file was created")
 
    elif "--help" in sys.argv:
        man_page()

    else:
        sys.exit('Usage: pyifconfig <option> <data> \n For get man page use "--help" ')
if __name__ == '__main__':
    main()
