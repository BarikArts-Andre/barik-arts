import http.server, os
os.chdir("/Users/shachar/Desktop/BARIK/website")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=3334, bind="")
