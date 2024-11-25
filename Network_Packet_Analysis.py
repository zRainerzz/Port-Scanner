import pyshark
import os
from colorama import init, Fore


init(autoreset=True)

class colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    RESET = Fore.RESET

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{colors.RESET}"

windows_interfaces = [
    "Ethernet", "Wi-Fi", "Loopback Adapter"
]
unix_interfaces = [
    "eth0", "wlan0", "lo", "enp0s3", "wlp2s0", "docker0", "tun0", "br0", "veth0", "peth0"
]
specialized_interfaces = [
    "ppp0", "vlan0", "bond0"
]

def print_network_interfaces():
    print("Windows Network Interfaces:", windows_interfaces)
    print("Linux/macOS/BSD Network Interfaces:", unix_interfaces)
    print("Specialized Network Interfaces:", specialized_interfaces)

def live_capture(interface):
    try:
        print(f"Starting live capture on interface: {interface}")
        print("Estimated capture duration is 60 seconds")
        capture = pyshark.LiveCapture(interface=interface)
        

        print("Setting up capture...")


        def packet_callback(packet):
            print("-->", colors.colorize(f"{packet}", colors.YELLOW), "\n")


        print("Starting sniffing...")
        capture.apply_on_packets(packet_callback, timeout=60)

    except Exception as e:
        print(colors.colorize(f"Error during live capture: {e}", colors.RED))

def file_capture_tcp():
    try:
        capture = pyshark.FileCapture('captured_packets.pcap', display_filter='tcp')
        for packet in capture:
            print("-->", colors.colorize(f"{packet}", colors.YELLOW), "\n")
    except Exception as e:
        print(colors.colorize(f"Error while reading the pcap file: {e}", colors.RED))

def file_capture_all():
    try:
        capture = pyshark.FileCapture('captured_packets.pcap')
        for packet in capture:
            print("-->", colors.colorize(f"{packet}", colors.YELLOW), "\n")
    except Exception as e:
        print(colors.colorize(f"Error while reading the pcap file: {e}", colors.RED))

def check_interface(interface_type, interface_name):
    if interface_type == 'W':
        if interface_name.lower() not in [i.lower() for i in windows_interfaces]:
            print(colors.colorize('This is not a Windows interface.', colors.RED))
            return False
    elif interface_type == 'U':
        if interface_name.lower() not in [i.lower() for i in unix_interfaces]:
            print(colors.colorize('This is not a recognized UNIX/Mac OS interface.', colors.RED))
            return False
    elif interface_type == 'S':
        if interface_name.lower() not in [i.lower() for i in specialized_interfaces]:
            print(colors.colorize('This is not a recognized Specialized interface.', colors.RED))
            return False
    return True

def main():
    print("This Code should ", colors.colorize(" Run as administrator.", colors.RED))
    print("You should choose your interface!\n")
    x = input("Need help? Enter " + colors.colorize("H", colors.BLUE) + " to list all network interfaces, or press any key to continue: ")
    
    if x.capitalize() == 'H':
        print_network_interfaces()

    print('\nWhich interface will you be using?')
    interface_type = input("Windows interface: " + colors.colorize("W", colors.BLUE) + 
                           ", / Unix-Mac OS interfaces: " + colors.colorize("U", colors.BLUE) + 
                           ", / Specialized interface: " + colors.colorize("S", colors.BLUE) + "\n")
    
    interface1 = None
    if interface_type.capitalize() == 'W':
        interface1 = input("Input your Windows interface: ")
        if not check_interface('W', interface1):
            return

    elif interface_type.capitalize() == 'U':
        interface1 = input("Type your Unix/Mac OS interface: ")
        if not check_interface('U', interface1):
            return

    elif interface_type.capitalize() == "S":
        interface1 = input("Type your Specialized interface: ")
        if not check_interface('S', interface1):
            return

    operation = input("Enter operation type: " + colors.colorize("L", colors.GREEN) + " for Live Capture, " + 
                      colors.colorize("T", colors.CYAN) + " for TCP File Capture, " + 
                      colors.colorize("A", colors.BLUE) + " for All File Capture: ")
    
    if operation.capitalize() == 'L':
        live_capture(interface1)
    elif operation.capitalize() == 'T':
        file_capture_tcp()
    elif operation.capitalize() == 'A':
        file_capture_all()
    else:
        print(colors.colorize("Invalid operation type.", colors.RED))

if __name__ == "__main__":
    main()
