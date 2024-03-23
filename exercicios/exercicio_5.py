"""
Exercício 5: Publisher no ESP32.

Esse script irá publicar uma mensagem num tópico do broker.
Use o broker "broker.hivemq.com" para testar a comunicação,
ou um broker local.
"""
from umqtt.simple import MQTTClient


SERVER = "broker.hivemq.com"
PORT = 1883
TOPIC = b""  # crie um nome único para não conflitar com outros usuários

client = MQTTClient("publisher", SERVER, port=PORT, keepalive=30)
client.connect()

while True:
    message = f"Testando o tópico {TOPIC}"

    try:
        client.publish(TOPIC, message)
    except:
        print("Envio da mensagem falhou")
        client.disconnect()
        client.connect()
