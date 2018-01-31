#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler,HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                output=""
                output +="<html><body>Hellooo</body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
	return
            if self.path.endswith(“/Ciao”):
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                output=""
                output +="<html><body>Ciao<a href="http://localhost:8080/hello”>de vuelta a hello</a></body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
                return
        except IOError:
                self.send_error(404,"No se encontro el archivo %s" % self.path)
def main():
    try:
        port=8080
        server=HTTPServer(("",port),webserverHandler)
        print("El servidor web esta ejecutandose en el puerto "+str(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print("El servidor ha sido interrumpido por el usuario , cerrando ...")
        server.socket.close()
        
if __name__ == '__main__':
	main()



