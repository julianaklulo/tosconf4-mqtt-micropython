# Usando o mosquitto_sub
1. Abra um terminal
1. Caso esteja no Windows, abra o Powershell e navegue até a pasta de instalação do Mosquitto
```
cd 'C:\Program Files\mosquitto\'
```
1. Digite o comando `mosquitto_sub -h localhost -t "teste"`
1. Caso não tenha um broker local rodando, use um dos brokers de teste
```
mosquitto_sub -h test.mosquitto.org -t "teste"
mosquitto_sub -h broker.hivemq.com -t "teste"
```

# Usando o mosquitto_pub
1. Abra um terminal
1. Caso esteja no Windows, abra o Powershell e navegue até a pasta de instalação do Mosquitto
```
cd 'C:\Program Files\mosquitto\'
```
1. Digite o comando `mosquitto_pub -h localhost -t "teste" -m "teste"`
1. Caso não tenha um broker local rodando, use um dos brokers de teste
```
mosquitto_pub -h test.mosquitto.org -t "teste" -m "teste"
mosquitto_pub -h broker.hivemq.com -t "teste" -m "teste"
```
1. Verifique no terminal onde o `mosquitto_sub` está rodando que a mensagem foi recebida