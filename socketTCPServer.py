import socket
import requests
from processors import decoder, interscityManager
# loop que fica "escutando" a porta que será de comunicaçao com a TM4C

TCP_IP='192.168.1.250'
TCP_PORT=7891
FLAG_TCP_ON=1
BUFFER_SIZE=15488
DEFAULT_UUID = '9c0772b8-c809-4865-bec7-70dd2013bc37'

def upaupa_servidor_tcp(n_eventos):
    global FLAG_TCP_ON, SOCKET_TCP_RX
    cont = 0
    print("cont=", cont)
    print("n_eventos=", n_eventos)

    #while cont < n_eventos:
    while FLAG_TCP_ON:
        vem = []
        msg = []
        print("Monta servidor...")
        try:
            SOCKET_TCP_RX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except OSError as msg_:
            SOCKET_TCP_RX = None
            FLAG_TCP_ON = False  # teste!!!!
            #continue
        try:
            SOCKET_TCP_RX.bind((TCP_IP, TCP_PORT))
            SOCKET_TCP_RX.listen(1)
        except OSError as msg_:
            SOCKET_TCP_RX.close()
            SOCKET_TCP_RX = None
            #continue
        if SOCKET_TCP_RX is None:
            print('could not open socket')
            FLAG_TCP_ON = False  # teste!!!!
            #break
            return -1
            #sys.exit(1)
        """
        SOCKET_TCP_RX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKET_TCP_RX.bind((TCP_IP, TCP_PORT))
        SOCKET_TCP_RX.listen(2)
        """
        print("Esperando dados...")
        # fica parado aqui esperando conexao de algum cliente
        try:
            conn, addr = SOCKET_TCP_RX.accept()
        except:
            print("To saindo foraa....")
            break
        print('Connection address:', addr)
        while True:
            #msg = conn.recv(BUFFER_SIZE)
            vem = conn.recv(1024)

            msg+=vem

            if len(msg) == BUFFER_SIZE:
                #print ("received data:", data)
                print("OK HEADER RECEIVED")
                #print("len data:", len(msg))
                """
                print("HEADER:")
                for i in range(40):
                    print("[%u] = %X"%(i, msg[i]))
                """
                break
            #elif not msg:
            """
            else:
                print("erro de BUFFER_SIZE")
                print("len msg = ", len(msg))
            """
            #conn.send(data)  # echo
        conn.close()
       # files = open("conjuntoTeste.txt","a+")
        dados = decoder.processData_decode(msg)
        #files.write(str(msg))
        #files.write("FIMDOEVENTO")
        #files.close()
        
        datajson = {
        "event_type": dados.Event,
        "energy_ativa": dados.energy_ativa,
        "voltage_real_rms": dados.rmsVoltage_real,
        "phase_real_rms": dados.rmsPhase_real,
       # "total_energy_daily": interscityManager.getDataDaily(DEFAULT_UUID)
        }
        requests.post("http://127.0.0.1:1880/attstatus", data=datajson)

        interscityManager.sendInfoToInterSCity(dados)
        print("EVENTO:", dados)
        if cont == n_eventos:
            print("CHEGAAAAAAAAAAAAAAAAAAA")
            return cont
        print("socket closed ", addr)


upaupa_servidor_tcp(1)