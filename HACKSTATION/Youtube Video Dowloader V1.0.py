#Baixador de Videos do Youtube
#En - Youtuber Dowloader videos
#Feito por Lucas Verissimo
#Versão 1.0

import pytube

link = input("Coloque o Link/URL do video aqui! \n>  ").strip().lower()
yt = pytube. YouTube(link)
yt.streams.first().download()

print(f"Parabéns você conseguiu fazer o dowload do seu video de link/url: {link}")
