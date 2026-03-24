import os
import http.server

os.chdir('/Users/oikawatakayuki/Desktop/コーポレートサイト')

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', 8000), handler)
print('Serving on http://localhost:8000')
httpd.serve_forever()
