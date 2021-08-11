"""
Programa: Super BOT de visualizacao no youtube, facebook com 10 Threads
"""

# Biblioteca
import requests
from os import system
from time import sleep
from threading import Thread

# Apresentacao
def apresentacao():

    # Comando de sistema
    system("clear")
    print("\033[01;31m # DARK PROGRAMMER 000 \033[01;37m")

    # IP externo
    system("echo -n ' # IP [externo]: '")
    system("curl ifconfig.me --silent | awk {'print $1'}")

    # IP interno
    system("echo -n ' # IP [interno]: '")
    system("hostname -I | awk {'print $1'}")

    # Simbolo
    print('''\033[01;32m
                  ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      ::::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
           ::::::::::88::88::88:::88::::::::::'
             ::::::::88::88::P::::88::::::::'
               ::::::88::88:::::::88::::::'
                ::::::::::::::::::::
                       ::::::::::
                       \033[01;37m''')

# Mensagem
def msg():

    # Mensagem
    print("\033[01;35m\n\n # Ativando Super BOT de visualizacao \033[01;37m")

    lista = ["...", "......", ".................."]

    for i in range(0, len(lista)):
        print("\033[01;32m\n Loading \033[01;37m", end=" ")
        print(str("\033[01;33m " + lista[i] + "\033[01;37m"))
        sleep(1)

    system("clear")

# Metodo: Visualizacoes
def visualizacao(args):

    while True:

        print("\n = Controle: " + str(args))

        try:
            # Configuracao

            # url = "http://127.0.0.1"
            proxy = {"http": "http://45.235.44.93:8080"}
            header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"}

            # Requisicao
            # requisicao = requests.get(url=url, headers=header, proxies=proxy)
            requisicao = requests.get(url=url, headers=header)

            # Saida de dados
            print("\n - Site: " + str(requisicao.url))
            print(" - Requisicao: " + str(requisicao.request))
            print(" - Codigo de saida: " + str(requisicao.status_code))

            for i, j in requisicao.headers.items():
                print(" - " + str(i) + ": " + str(j))
        except:
            continue

# Apresentacao
apresentacao()

# Entrada de dados
url = str(input(" - Host (https://www.folha.uol.com.br/): "))

# Mensagem
msg()

# Criacao das Thread
t_visual_1 = Thread(target=visualizacao, args=["1"])
t_visual_2 = Thread(target=visualizacao, args=["2"])
t_visual_3 = Thread(target=visualizacao, args=["3"])
t_visual_4 = Thread(target=visualizacao, args=["4"])
t_visual_5 = Thread(target=visualizacao, args=["5"])
t_visual_6 = Thread(target=visualizacao, args=["6"])
t_visual_7 = Thread(target=visualizacao, args=["7"])
t_visual_8 = Thread(target=visualizacao, args=["8"])
t_visual_9 = Thread(target=visualizacao, args=["9"])
t_visual_10 = Thread(target=visualizacao, args=["10"])
t_visual_11 = Thread(target=visualizacao, args=["11"])
t_visual_12 = Thread(target=visualizacao, args=["12"])
t_visual_13 = Thread(target=visualizacao, args=["13"])
t_visual_14 = Thread(target=visualizacao, args=["14"])
t_visual_15 = Thread(target=visualizacao, args=["15"])
t_visual_16 = Thread(target=visualizacao, args=["16"])
t_visual_17 = Thread(target=visualizacao, args=["17"])
t_visual_18 = Thread(target=visualizacao, args=["18"])
t_visual_19 = Thread(target=visualizacao, args=["19"])
t_visual_20 = Thread(target=visualizacao, args=["20"])
t_visual_21 = Thread(target=visualizacao, args=["21"])
t_visual_22 = Thread(target=visualizacao, args=["22"])
t_visual_23 = Thread(target=visualizacao, args=["23"])
t_visual_24 = Thread(target=visualizacao, args=["24"])
t_visual_25 = Thread(target=visualizacao, args=["25"])
t_visual_26 = Thread(target=visualizacao, args=["26"])
t_visual_27 = Thread(target=visualizacao, args=["27"])
t_visual_28 = Thread(target=visualizacao, args=["28"])
t_visual_29 = Thread(target=visualizacao, args=["29"])
t_visual_30 = Thread(target=visualizacao, args=["30"])

# Executar
t_visual_1.start()
t_visual_2.start()
t_visual_3.start()
t_visual_4.start()
t_visual_5.start()
t_visual_6.start()
t_visual_7.start()
t_visual_8.start()
t_visual_9.start()
t_visual_10.start()
t_visual_11.start()
t_visual_12.start()
t_visual_13.start()
t_visual_14.start()
t_visual_15.start()
t_visual_16.start()
t_visual_17.start()
t_visual_18.start()
t_visual_19.start()
t_visual_20.start()
t_visual_21.start()
t_visual_22.start()
t_visual_23.start()
t_visual_24.start()
t_visual_25.start()
t_visual_26.start()
t_visual_27.start()
t_visual_28.start()
t_visual_29.start()
t_visual_30.start()
