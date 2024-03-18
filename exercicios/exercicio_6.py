"""
Exercício 6: Subscriber no ESP32.

Esse script irá receber mensagens de um tópico do broker.
Use o broker "broker.hivemq.com" para testar a comunicação,
ou um broker local.
"""
from umqtt.simple import MQTTClient


SERVER = "broker.hivemq.com"
PORT = 1883
TOPIC = b""  # crie um nome único para não conflitar com outros usuários


def callback_message(topic: bytes, data: bytes):
    """
    Função que será chamada sempre que uma mensagem for recebida.
    """
    message = data.decode("utf-8")
    print(f"Mensagem recebida: {message}")


client = MQTTClient("subscriber", SERVER, port=PORT, keepalive=10)
client.set_callback(callback_message)


while True:
    try:
        client.connect()
        client.subscribe(TOPIC)
        client.wait_msg()  # função bloqueante
    except Exception:
        print("Failed to receive message, disconnecting.")
        client.disconnect()
