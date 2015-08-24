
import SimpleHTTPServer

class CORSHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):

        # Chrome won't load fonts without this header
        self.send_header('Access-Control-Allow-Origin', '*')

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=CORSHandler)
