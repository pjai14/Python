SimpleHTTPServer.py:
--------------------

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
    
 index.html:
 -----------
 
 <html>
    <head>
        <title>Python is awesome!</title>
    </head>
    <body>
        <h1>This is a simple HTTP sever program </h1>
        <p>Congratulations! The HTTP Server is working!</p>
    </body>
</html>
