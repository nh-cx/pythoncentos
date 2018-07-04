#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
"""
Start Linux http server to 80 port
"""

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port:' + str(httpd.server_port))
httpd.serve_forever()
