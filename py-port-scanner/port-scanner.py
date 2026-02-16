"""
Versão atual do port scanner
"""

import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor
from services import get_service_name


# ===============================
# Banner
# ===============================
def banner(target):
    print("=" * 40)
    print("        PY PORT SCANNER")
    print("=" * 40)
    print(f"Alvo: {target}")
    print("=" * 40)


# ===============================
# Scanner de porta
# ===============================
def scan_port(ip, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        resultado = sock.connect_ex((ip, porta))

        if resultado == 0:
            service = get_service_name(porta)
            print(f"[+] Porta {porta} ABERTA ({service})")

        sock.close()

    except:
        pass


# ===============================
# Argumentos do terminal
# ===============================
def parse_args():
    parser = argparse.ArgumentParser(
        description="Python Port Scanner simples"
    )

    parser.add_argument(
        "target",
        help="IP alvo (ex: 127.0.0.1)"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1000",
        help="Range de portas (ex: 1-5000)"
    )

    return parser.parse_args()


# ===============================
# Converter range de portas
# ===============================
def parse_ports(port_range):
    inicio, fim = port_range.split("-")
    return range(int(inicio), int(fim) + 1)


# ===============================
# Função principal
# ===============================
def main():
    args = parse_args()

    ip = args.target
    portas = parse_ports(args.ports)

    banner(ip)

    inicio = time.time()

    # multithread
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda p: scan_port(ip, p), portas)

    fim = time.time()

    print("\nScan finalizado em {:.2f} segundos".format(fim - inicio))


# ===============================
# Execução principal
# ===============================
if __name__ == "__main__":
    main()
