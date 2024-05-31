import socket
import psutil
import platform
import os
import shutil
import colorama
from colorama import *
os.system('cls')
def get_ip_address():
    # Pobierz adres IP
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_mac_address():
    # Pobierz adres MAC
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == psutil.AF_LINK:
                return address.address

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "Node Name": platform.node(),
        "Windows": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()
    }
    return system_info

def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    memory_info = {
        "Total": virtual_memory.total,
        "Available": virtual_memory.available,
        "Used": virtual_memory.used,
        "Percentage": virtual_memory.percent
    }
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        partition_info = shutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "Mountpoint": partition.mountpoint,
            "Filesystem Type": partition.fstype,
            "Total Size": partition_info.total,
            "Used": partition_info.used,
            "Free": partition_info.free,
            "Percentage Used": partition_info.used / partition_info.total * 100
        }
    return disk_info

if __name__ == "__main__":
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    system_info = get_system_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    print(Fore.YELLOW + """
 /$$   /$$                                   /$$           /$$                
| $$  /$$/                                  | $$          | $$                
| $$ /$$/   /$$$$$$  /$$  /$$  /$$  /$$$$$$ | $$  /$$$$$$$| $$   /$$ /$$   /$$
| $$$$$/   /$$__  $$| $$ | $$ | $$ |____  $$| $$ /$$_____/| $$  /$$/| $$  | $$
| $$  $$  | $$  \ $$| $$ | $$ | $$  /$$$$$$$| $$|  $$$$$$ | $$$$$$/ | $$  | $$
| $$\  $$ | $$  | $$| $$ | $$ | $$ /$$__  $$| $$ \____  $$| $$_  $$ | $$  | $$
| $$ \  $$|  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$ /$$$$$$$/| $$ \  $$|  $$$$$$$
|__/  \__/ \______/  \_____/\___/  \_______/|__/|_______/ |__/  \__/ \____  $$
                                                                     /$$  | $$
                                                                    |  $$$$$$/
                                                                     \______/ 
                                1.0 TESTING
""")
    while True:
        response = input("<")
        if response == 'get_*':
            print("==========================")
            print(f"MAC address: {mac_address}")
            print(f"IP address: {ip_address}")
            print("==========================")
            print("System Information:")
            for key, value in system_info.items():
                print(f"{key}: {value}")
            
            print("\nMemory Information:")
            for key, value in memory_info.items():
                print(f"{key}: {value / (1024 ** 3):.2f} GB" if key in ["Total", "Available", "Used"] else f"{key}: {value}%")
            
            print("\nDisk Information:")
            for device, info in disk_info.items():
                print(f"Device: {device}")
                for key, value in info.items():
                    print(f"  {key}: {value / (1024 ** 3):.2f} GB" if key in ["Total Size", "Used", "Free"] else f"  {key}: {value}")
            print("==========================")
        elif response == '#insert get_ram --usage':
                for key, value in memory_info.items():
                    print(f"{key}: {value / (1024 ** 3):.2f} GB" if key in ["Total", "Available", "Used"] else f"{key}: {value}%")
        elif response == '#insert get_disk --space':
                print(f"Device: {device}")
                for key, value in info.items():
                    print(f"  {key}: {value / (1024 ** 3):.2f} GB" if key in ["Total Size", "Used", "Free"] else f"  {key}: {value}")
        else:
            print('Command not found')