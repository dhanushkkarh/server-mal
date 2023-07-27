import http.server
import socketserver
import socket

# Set the folder you want to share here (e.g., "C:/SharedFolder")
shared_folder = "C:"

# Set the port number for the server (choose an available port)
port = 8000

Handler = http.server.SimpleHTTPRequestHandler

# Change the current directory to the shared folder
import os
os.chdir(shared_folder)

# Get the IP address of the laptop
def get_laptop_ip():
    try:
        # Create a socket to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error:
        return "localhost"  # If unable to fetch IP, default to localhost

# Start the server
with socketserver.TCPServer(("", port), Handler) as httpd:
    laptop_ip = get_laptop_ip()
    print(f"Server started at: http://{laptop_ip}:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

print("Server stopped.")
