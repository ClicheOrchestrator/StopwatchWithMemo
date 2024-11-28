from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, CORSRequestHandler)
print(f"Server running at http://{server_address[0]}:{server_address[1]}")

httpd.serve_forever()