from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import cgi
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', '/login.html'):
            self.serve_static_file('/login.html')
        else:
            self.send_error(404, "File not found")
    def serve_static_file(self, file_path):
        try:
            with open(file_path[1:], 'rb') as file: 
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")
    def do_POST(self):
        if self.path == '/submit-login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fields = urllib.parse.parse_qs(post_data.decode('utf-8'))
            username = fields.get('username', [None])[0]
            password = fields.get('password', [None])[0]
            if username == "mohammad@loay.com" and password == "ML123456":
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Login successful")
            else:
                self.send_response(401)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Login failed")
        else:
            self.send_error(404, "File not found")
def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}/")
    httpd.serve_forever()
if __name__ == "__main__":
    run()
