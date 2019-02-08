# encoding: utf-8

import socket, sys, re

banner = """
d88888b d8888b.   d8888b. d88888b d8888b. db    db  d888b    
88'     VP  `8D   88  `8D 88'     88  `8D 88    88 88' Y8b   
88ooooo   oooY'   88   88 88ooooo 88oooY' 88    88 88          
88~~~~~   ~~~b.   88   88 88~~~~~ 88~~~b. 88    88 88  ooo   
88.     db   8D   88  .8D 88.     88   8D 88b  d88 88. ~8~   
Y88888P Y8888P'   Y8888D' Y88888P Y8888P' ~Y8888P'  Y888P    

        d888888b  .d88b.   .d88b.  db      .d8888.
        `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP
           88    88    88 88    88 88      `8bo.  
           88    88    88 88    88 88        `Y8b.
           88    `8b  d8' `8b  d8' 88booo. db   8D
           YP     `Y88P'   `Y88P'  Y88888P `8888Y'

+--------------------------------------------------------------+
| Python3.7, version 0.1                                       |
|                                                              |
| Dev        : RonaldoMafra                                    |
| Git Dev    : https://github.com/ronaldomafra                 |
| Git Projeto: https://github.com/ronaldomafra/elipseE3Debug   |
+--------------------------------------------------------------+"""

class E3Logger():
    def __init__(self,port,banner):
        self.port   = int(port)
        self.banner = banner

    def run(self):
        host = socket.gethostbyname("localhost")
        try:
            meSk = socket.socket()
            meSk.bind((host, self.port))

            meSk.listen(1)
            print("[+] Server e3-Debug Online, porta:" + str(self.port))

            while True:
                conn, addr = meSk.accept()
                data = conn.recv(1024).decode()
                if self.banner == 0:
                    print("[MSG from: " + str(addr) + "] " + data)
                else:
                    print(data)
                conn.close()

        except(socket.error):
            print("[-] Não foi possivel conectar")
            print("[-] Porta: " + str(self.port))
            print("[-] socket.error: " + str(socket.error))
            sys.exit(1)

print(banner)
portMaxMin = [1,65535]
stage = 0
conf = False
optPass = {"banner":0,"port":None}

print("[+] Configurar LogServer.")
while True:
    try:
        if stage == 0:
            opt = input("[+] Habilita Banner (s/n)? > ")
            if opt.lower() == "s":
                print("[!] Banner habilitado")
                optPass['banner'] = 0
                stage = 1
            elif opt.lower() == "n":
                print("[!] Banner desabilitado")
                optPass['banner'] = 1
                stage = 1
            else:
                print("[-] Opção invalida, digite s/n")

        elif stage == 1:
            opt = input("[+] Selecione a porta > ")
            if range(portMaxMin[0],portMaxMin[1],int(opt)):
                print("[!] Porta selecionada " + opt)
                optPass['port'] = int(opt)
                break
            else:
                print("[-] Porta fora do intervalo, " + str(portMaxMin))
                pass
    except:
        if stage == 0:
            print('[-] Opção invalida, digite "s" ou "n"')
            pass
        elif stage == 1:
            print('[-] Opção invalida, digite valor entre ' + str(portMaxMin))
            pass


print("[+] Iniciando server.")
e3Logger = E3Logger(optPass["port"], optPass["banner"])
e3Logger.run()
