import requests, time, sys

def BaixarArquivo(link:str,nomeArquivo:str):
	resp = requests.get(link)
	if resp.ok:
		with open(nomeArquivo,"wb") as f:
			f.write(resp.content)
			f.close()

def GetUnixTime():
	tm = str(time.time())
	tm = tm[:len(tm)-4].replace('.',"")
	return tm

def Main():
	argumentos = sys.argv
	if(len(argumentos)==1):
		help()
	else:
		SelecionarFio(argumentos[1])

def SelecionarFio(fio:str):
	site = "https://ptchan.org"
	extensoes = (".mp4",".png",".jpg",".jpeg",".webm",".gif")
	jaBaixados = []

	separadoEmLinhas = GetRawSite(fio).splitlines()

	for linha in separadoEmLinhas:
		pedacos = linha.strip().split(' ')

		for pedaco in pedacos:
			if pedaco.startswith('href="/file/'):
				pedacinho = pedaco.split('"')

				for extensao in extensoes:
					if(pedacinho[1].endswith(extensao) and \
						pedacinho[1] not in jaBaixados):
						jaBaixados.append(pedacinho[1])
						BaixarArquivo(site+pedacinho[1],GetUnixTime()+extensao)
						print(site+pedacinho[1],"foi baixado")

def Help():
	print("python3 main.py linkDoFio")
	print("EX:")
	print("python3 main.py 'https://ptchan.org/i/thread/205316.html'")

def GetRawSite(link:str):
	try:
		resp = requests.get(link)
		raw = resp.content.decode('utf-8')
		resp.close()
		return raw
	except:
		print("Algo deu errado, provavelmente você passou um link invalido.")

Main()