import socket

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET6 if ":" in ip else socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        s.send(b"Hello")
        response = s.recv(1024)
        print(f"[+] Port {port} is open")
        print(f"    Response: {response.decode()}")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        print(f"[-] Port {port} is closed")

def menu():
    print("""
    _       __     __      __               __          
   | |     / /__  / /_  __/ /_  ____ ______/ /_  _______
   | | /| / / _ \/ __ \/ / / /_/ __ `/ ___/ __ \/ ___/ 
   | |/ |/ /  __/ /_/ / /_/ /__, / /__/ / / / (__  )  
   |__/|__/\___/_.___/\__,_/_/____/\___/_/ /_/____/ 
                                                      
   Main Menu:
   1. Scan a target for open ports
   2. Help
   3. Exit
   """)

def help_menu():
    print("""
   Kraken-Port Help:
   - Enter the target address when prompted (IPv4, IPv6, or MAC address)
   - Enter the port range to scan when prompted (e.g. 1-1024)
   - The tool will scan for open ports within the range you specified
   - The tool will then return to the main menu
   """)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            target = input("Enter target address (IPv4, IPv6, or MAC): ")
            try:
                ip = socket.gethostbyname(target)
                print(f"Scanning ports for {ip}...")
                port_range = input("Enter port range to scan (e.g. 1-1024): ")
                start_port, end_port = map(int, port_range.split("-"))
                ports = list(range(start_port, end_port + 1)) + [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389, 8080, 8443, 8888]
                for port in ports:
                    check_port(ip, port)
                input("Press Enter to return to the main menu.")
            except socket.gaierror:
                print("Invalid address format, please try again.")
                continue
            except ValueError:
                print("Invalid port range, please try again.")
                continue
        elif choice == "2":
            help_menu()
            input("Press Enter to return to the main menu.")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
