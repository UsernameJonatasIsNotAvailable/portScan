import socket as s
import argparse
import asyncio

async def varredura_portas(alvo, porta, portas_abertas):
    try:
        client = s.socket(s.AF_INET, s.SOCK_STREAM)
        client.settimeout(0.05)

        if client.connect_ex((alvo, porta)) == 0:
            print(f"Porta aberta ==> {porta}")
            portas_abertas.append(porta)
        client.close()
    except (s.gaierror, s.timeout, ConnectionRefusedError, OSError):
        pass
    except Exception as e:
        print(f"Ocorreu um erro na porta {porta}: {e}")

async def varredura_portas_async(alvo, portas):
    portas_abertas = []
    tarefas = [varredura_portas(alvo, porta, portas_abertas) for porta in portas]
    await asyncio.gather(*tarefas)

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

asyncio.run(varredura_portas_async(alvo, portas))
