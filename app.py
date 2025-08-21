#!/usr/bin/env python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    PORT = 5001
    os.chdir('/home/ubuntu/automatic-ads-frontend-enhanced')
    
    with socketserver.TCPServer(("0.0.0.0", PORT), CORSRequestHandler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT}")
        httpd.serve_forever()

