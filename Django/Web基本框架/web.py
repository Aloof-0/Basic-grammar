# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 15:16
# @Author  : Frosty 
# @Email   : 935722505@qq.com
# @File    : web.py
# @Time : 2020/7/25 15:16
# @Software: PyCharm

import socket

def handle_request(client):

    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    with open("text.html", "rb") as f:
        lodo = f.read()
    client.send(lodo)

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8001))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()