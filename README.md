# download-fio-ptchina

Programa para baixar todas imagens e videos de um fio do ptchina.

# Como usar

Basta abrir o programa com o link do fio que você quer baixar.

```
py main.py https://ptchan.org/br/thread/56421.html
```

Ou pode usar o wget, muito mais simples.

```
wget -r -nd -l1 -A mp4,webm,gif,jpg,jpeg https://ptchan.org/br/thread/56421.html
```