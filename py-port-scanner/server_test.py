"""
SERVIDOR DE TESTE: abre a porta 4444
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 4444))
server.listen(1)

print("Servidor rodando na porta 4444...")

while True:
    client, addr = server.accept()
    print("Conexão recebida de", addr)
