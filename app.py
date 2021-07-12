import os
import http.server
import socketserver
import pymysql

from http import HTTPStatus

# Configuration section
http_port = int(os.getenv('HTTP_PORT', 8080))

# Handler used to serve HTTP requests
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello!\n  Path: {path}'.format(path=self.path)
        self.wfile.write(msg.encode())

# Serve the HTTP requests
print('Listening on port %s' % (http_port))
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('', http_port), Handler)
httpd.serve_forever()
