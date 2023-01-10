import socket
import sys

def send_http_post_proxy(host,port,cmd):
    data = f'config_sequence=;{cmd};'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request = (f'POST /cgi-bin-igd/netcore_set.cgi HTTP/1.1\r\n'
               f'Host: {host}\r\n'
               'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
               'Content-Type: application/x-www-form-urlencoded\r\n'
               f'Content-Length: {len(data)}\r\n'
               '\r\n'
               f'{data}')
    s.sendall(request.encode())
    s.shutdown(socket.SHUT_WR)
    result = b''
    while True:
        buf = s.recv(1024)
        if not buf:
            break
        result += buf
    s.close()
    return result.decode()

if __name__ == '__main__':
    print(send_http_post_proxy(sys.argv[1],int(sys.argv[2]),sys.argv[3]))