import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")
    
    try:
        for port in range(start_port, end_port + 1):
            # Create a socket object
            scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout for the connection attempt
            scanner_socket.settimeout(1)
            
            # Attempt to connect to the target IP and port
            result = scanner_socket.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"Port {port} is open")
            
            # Close the socket
            scanner_socket.close()
    
    except KeyboardInterrupt:
        print("Port scanning stopped by user.")
    
    except socket.gaierror:
        print("Hostname could not be resolved.")
    
    except socket.error:
        print("Could not connect to the server.")

# Usage example
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Start the port scanning
scan_ports(target_ip, start_port, end_port)
