import socket as s
import argparse

def varredura_portas(alvo, portas):

    try:
        for porta in portas:
            client = s.socket(s.AF_INET, s.SOCK_STREAM)
            client.settimeout(0.05)

            if client.connect_ex((alvo, porta)) == 0:
                print(f"Porta aberta ==> {porta}")
            client.close()
    except s.gaierror:
        print("Erro: Endereço do alvo inválido.")
    except s.timeout:
        print("Erro: Tempo limite da conexão excedido.")
    except ConnectionRefusedError:
        print("Erro: Conexão recusada pelo alvo.")
    except OSError as e:
        print(f"Erro de sistema operacional: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alvo")
    parser.add_argument("-p", "--portas", default="1-1024")
    args = parser.parse_args()

    alvo = args.alvo
    portas_input = args.portas

if "-" in portas_input:
    inicio, fim = map(int, portas_input.split("-"))
    portas = range(inicio, fim + 1)
else:
    portas = [int(p) for p in portas_input.split(",")]

varredura_portas(alvo, portas)
