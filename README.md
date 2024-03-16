# Introdução ao MQTT com MicroPython na Tosconf[4]
Repositório do tutorial Introdução ao MQTT com MicroPython apresentado na [Tosconf[4]](https://2024.tosconf.lhc.net.br/) do [Laboratório Hacker de Campinas](https://lhc.net.br/) em 23/03/2024.

# Sobre o MicroPython
O MicroPython é uma implementação enxuta e eficiente da linguagem de programação Python 3 que inclui um pequeno subconjunto da biblioteca padrão do Python e é otimizada para execução em microcontroladores e em ambientes restritos.

Ele possui recursos avançados, como prompt interativo, list comprehensions, generators, tratamento de exceções e muito mais. No entanto, é compacto o suficiente para caber e funcionar em apenas 256k de espaço de código e 16k de RAM.

Além disso, o MicroPython pretende ser o mais compatível possível com o Python normal para permitir a transferência de código com facilidade do desktop para um microcontrolador ou sistema embarcado.

## Exercício 0: Instalando o Thonny
Iremos utilizar a IDE Thonny para realizar a edição do código e gerenciamento dos arquivos na placa.

Essa IDE possui um gerenciador para o sistema de arquivos da pasta, além de um terminal que se conecta automaticamente ao REPL da placa.

As instruções para instalação do Thonny podem ser encontradas no [Exercício 0](exercicios/exercicio_0.md).

## Exercício 1: Controlando um LED com MicroPython
O primeiro exercício será composto por 2 partes, onde iremos controlar um LED de duas maneiras diferentes.

Para ambos os exercícios iremos utilizar o mesmo circuito, portanto monte-o de acordo com a imagem abaixo:

![Circuito do Blink](exercicios/imagens/blink.png)

## Exercício 1.1: Blink
A primeira parte do exercício é o Blink, o clássico Hello World da programação embarcada.

Nesse exercício, iremos fazer o LED piscar a cada 0.5s.

A resolução desse exercício pode ser encontrada no [Exercício 1.1](exercicios/exercicio_1_1.py).

## Exercício 1.2: Fade
A segunda parte do exercício é o Fade, onde iremos fazer o LED ir de 0 a 100% de brilho e voltar a 0% de brilho.

A resolução desse exercício pode ser encontrada no [Exercício 1.2](exercicios/exercicio_1_2.py).

## Exercício 2: Potenciômetro
Nesse exercício, iremos ler o valor do potenciômetro e exibir no terminal.

Para esse exercício, monte o circuito de acordo com a imagem abaixo:

![Circuito do Potenciômetro](exercicios/imagens/potenciometro.png)

A resolução desse exercício pode ser encontrada no [Exercício 2](exercicios/exercicio_2.py).

# Sobre o MQTT
O MQTT é um protocolo de mensagens para Internet das Coisas (IoT).

Ele é projetado como um transporte de mensagens extremamente leve de publisher/subscriber, ideal para conectar dispositivos remotos com pouca capacidade de armazenamento e largura de banda de rede mínima.

O MQTT é usado hoje em uma ampla variedade de setores, como automotivo, manufatura, telecomunicações, petróleo e gás, dentre outros.

## Exercício 3: Instalando o Mosquitto
Iremos utilizar o Mosquitto como broker para o MQTT. O Mosquitto é um broker de código aberto que implementa o protocolo MQTT.

As instruções para instalação do Mosquitto podem ser encontradas no [Exercício 3](exercicios/exercicio_3.md).

## Exercício 4: mosquitto_sub e mosquitto_pub
Nesse exercício, iremos utilizar o mosquitto_sub e o mosquitto_pub para publicar e subscrever mensagens.

As instruções para esse exercício podem ser encontradas no [Exercício 4](exercicios/exercicio_4.md).

# Usando MQTT com MicroPython
Agora vamos utilizar um client MQTT dentro do MicroPython para podemos realizar a publicação e subscrição de mensagens.

Essa parte do tutorial irá utilizar duas placas ESP32, uma para publicar mensagens e outra para subscrever mensagens.

<b>Preste bastante atenção no Thonny para saber em qual placa você está rodando o código. Cada placa estará conectada em uma porta diferente, identifique qual porta está conectada a qual placa para evitar sobrescrever o código na placa errada.</b>

## Exercício 5: Publicando com MicroPython
Nesse exercício, iremos publicar mensagens utilizando o MicroPython.

A resolução desse exercício pode ser encontrada no [Exercício 5](exercicios/exercicio_5.py).

## Exercício 6: Subscrevendo com MicroPython
Nesse exercício, iremos subscrever mensagens utilizando o MicroPython.

A resolução desse exercício pode ser encontrada no [Exercício 6](exercicios/exercicio_6.py).

## Desafio: Controlando o LED via potenciômetro
Para finalizar o tutorial, após ter feito todos os exercícios você estará pronto para juntar tudo que aprendeu e realizar o desafio!

<b>Controle o LED de uma das placas ESP32 utilizando o potenciômetro da outra placa ESP32.</b>

Para isso, use uma das placas para publicar o valor do potenciômetro em um tópico, enquanto a outra placa irá subscrever no mesmo tópico e utilizar o valor lido para controlar o LED.

<i>Não se esqueça de salvar os códigos anteriores no computador caso não queira sobrescrevê-los.</i>

# Conclusão
Com isso, finalizamos o tutorial de Introdução ao MQTT com MicroPython. Espero que tenha sido útil e que você tenha aprendido bastante!

Caso tenha alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo:
- Email: julianaklulo@gmail.com
- Telegram: https://t.me/julianaklulo
- Linkedin: https://linkedin.com/in/julianaklulo
