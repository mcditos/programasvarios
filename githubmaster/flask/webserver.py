
# coding: utf-8

# In[8]:

from http.server import BaseHTTPRequestHandler,HTTPServer


# In[10]:

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                output=""
                output +="<html><body>Hellooo</body></html>"
                self.wfile.write(output)
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
        
    if __name__=="__main__":
        main()


# In[ ]:



