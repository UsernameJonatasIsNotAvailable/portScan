# PortScanner em Python
Nescessário ter o Python instalado:</br>
==> <https://www.python.org/></br>
</br>
Para rodar o código basta ir no local do arquivo via terminal e digitar:<br>
==> ```python port_scanner.py <Digitar o IPv4/Domínio do alvo>```</br>
Ficaria assim: python port_scanner.py google.com</br>
Por padrão ele vai scannear as portas de 1-1024.</br>
</br>
Caso queira especificar as portas a serem analisadas:</br>
==> ```python port_scanner.py <Digitar o Ip/Domínio do alvo> -p <Px: 80,21,443>```</br>
Ficaria assim: python port_scanner.py 125.115.28.231 -p 80,21,443</br>
</br>
Caso queira scannear a porta entre um intervalo basta digitar a porta de partida e a de chegada, por exemplo, 1-8080:</br>
==> ```python port_scanner.py <Digitar o IPv4/Domínio do alvo> -p <Px: 1-8080>```</br>
Ficaria assim: python port_scanner.py 192.168.55.7 -p 1-8080
