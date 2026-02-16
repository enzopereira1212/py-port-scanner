import socket

def get_service_name(porta):
    try:
        return socket.getservbyport(porta)
    except:
        return "desconhecido"
