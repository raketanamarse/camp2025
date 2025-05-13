import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

AUTHOR = os.getenv('AUTHOR', 'Unknown Author')

class EchoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)

        response = f"""
        <html>
            <head>
                <title>Echo Server</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #333; }}
                    .info {{ background-color: #f4f4f4; padding: 25px; border-radius: 10px; }}
                </style>
            </head>
            <body>
                <h1>Echo Server</h1>
                <div class="info">
                    <p><strong>Hostname:</strong> {hostname}</p>
                    <p><strong>IP Address:</strong> {host_ip}</p>
                    <p><strong>Author:</strong> {AUTHOR}</p>
                </div>
            </body>
        </html>
        """
        

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, EchoRequestHandler)
    print(f"Server running on port 8000... {server_address}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
