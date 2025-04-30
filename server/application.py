import http.server
import socketserver

class TestMe: #Класс для тестирования работы
    def take_five(self): #Возвращает число 5
        return 5
    def port(self): #Возвращает порт по умолчанию
        return 8000
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    PORT = 8000
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
