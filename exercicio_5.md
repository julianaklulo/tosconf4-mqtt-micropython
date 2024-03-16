# Usando o mosquitto_sub
1. Abra um terminal
1. Caso esteja no Windows, abra o Powershell e navegue até a pasta de instalação do Mosquitto
```
cd 'C:\Program Files\mosquitto\'
```
1. Digite o comando `mosquitto_sub -h localhost -t "teste" -v`

# Usando o mosquitto_pub
1. Abra um terminal
1. Caso esteja no Windows, abra o Powershell e navegue até a pasta de instalação do Mosquitto
```
cd 'C:\Program Files\mosquitto\'
```
1. Digite o comando `mosquitto_pub -h localhost -t "teste" -m "teste"`
1. Verifique no terminal onde o `mosquitto_sub` está rodando que a mensagem foi recebida