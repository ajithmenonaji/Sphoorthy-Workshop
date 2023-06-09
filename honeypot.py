import socket

def start_honeypot():
    # Specify the IP address and port number you want the honeypot to listen on
    listen_ip = '0.0.0.0'  # Listens on all available network interfaces
    listen_port = 22  # SSH port
    
    try:
        # Create a socket object
        honeypot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the IP address and port
        honeypot_socket.bind((listen_ip, listen_port))
        
        # Start listening for incoming connections
        honeypot_socket.listen(5)
        
        print(f"[+] Honeypot listening on {listen_ip}:{listen_port}")
        
        while True:
            # Accept incoming connection
            client_socket, client_address = honeypot_socket.accept()
            
            print(f"[+] Connection established from: {client_address[0]}:{client_address[1]}")
            
            # Send a fake response to the client
            response = "SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.10\r\n"  # Fake SSH banner
            client_socket.send(response.encode())
            
            # Close the connection
            client_socket.close()
            
    except Exception as e:
        print(f"[-] An error occurred: {str(e)}")

# Start the honeypot
start_honeypot()
