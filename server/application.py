import http.server
import socketserver

class TestMe:
    def take_five(self):
        return 5
    def port(self):
        return 8000
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    PORT = 8000
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
