import socket

def scan(target_ip,target_port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.getdefaulttimeout(1)

        result=sock.connect_ex((target_ip,target_port))
        if result==0:
            print(f'Port {target_port} is open on {target_ip}')
        sock.close()
    except socket.error:
        print("No connection with host")
    except KeyboardInterrupt:
        print("Scanning interrupt")
    except socket.gaierror:
        print("Bad ip address or host")
        exit()

def main():
    print("-" * 50)
    print("Scanner")
    print("-" * 50)

    target_ip=input("Input ip address to scan")
    target_ip=socket.gethostbyname(target_ip)
    #exit()

    target_ports=input("Enter a host range separated by commas: ").strip().split(',')
    exit()
    for port in target_ports:
        scan(target_ip,int(port))

if __name__ == "__main__":
    main()
