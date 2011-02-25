import string,cgi,time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import serial
import time

arduino = serial.Serial('/dev/tty.usbserial-A6008cPT', 9600) 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("on"):
            arduino.write("Y")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("lights on - <a href='?action=off'>off</a> - <a href='?action=flash'>flash</a>")
            return
        elif self.path.endswith("off"):
            arduino.write("N")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("lights off - <a href='?action=on'>on</a> - <a href='?action=flash'>flash</a>")
            return
        elif self.path.endswith("flash"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("lights flash - <a href='?action=on'>on</a> - <a href='?action=off'>off</a>")
            arduino.write("Y")
            time.sleep(1)
            arduino.write("N")
            time.sleep(1)
            arduino.write("Y")
            time.sleep(1)
            arduino.write("N")
            time.sleep(1)
            arduino.write("Y")
            time.sleep(1)
            arduino.write("N")
            return
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("huh? - <a href='?action=on'>on</a> or <a href='?action=off'>off</a>")
            return
     
def main():
    try:
        server = HTTPServer(('', 9090), MyHandler)
        print 'started arduino server..' 
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
