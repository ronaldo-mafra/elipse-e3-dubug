import socket
import sys

helpOpt = ["-h","-H","--help","--HELP"]

def Main(p,m):
    host = socket.gethostbyname("localhost")
    port = int(p)

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = m
    mySocket.send(message.encode())

    mySocket.close()


def help():
    print("""[!] Uso do client:
        e3DebugCli.py ["-h","-H","--help","--HELP"] => Exibe o help
        e3DebugCli.py [porta] [msg] ============> Manda msg. para o server
                                                  Exemplo: e3DebugCli.py 4444 "teste teste" """)
    sys.exit(1)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] in helpOpt:
            help()
        if len(sys.argv) > 2:
            if sys.argv[1].isalpha():
                help()
            else:
                Main(sys.argv[1], sys.argv[2])
    else:
        help()
