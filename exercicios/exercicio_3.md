# Instalando o Mosquitto

1. Baixar o Mosquitto broker com os clients em https://mosquitto.org/download
1. Instalar de acordo com o SO do seu computador

# Configurando o broker no Linux
1. Após instalar o mosquitto, abrir o arquivo `/etc/mosquitto/mosquitto.conf` e adicionar:
    ```
    allow_anonymous true
    listener 1883 0.0.0.0
    ```
1. Habilitar e iniciar o serviço
    ```
    sudo systemctl enable mosquitto.service
    sudo systemctl start mosquitto.service
    ```

# Configurando o broker no Windows
1. Abrir Powershell como administrador
1. Navegar até a pasta de instalação do Mosquitto
    ```
    cd 'C:\Program Files\mosquitto\'
    ```
1. Abrir o arquivo `mosquitto.conf`
    ```
    notepad .\mosquitto.conf
    ```
1. Adicionar as seguintes duas linhas ao final do arquivo e salvar as alterações
    ```
    allow_anonymous true
    listener 1883 0.0.0.0
    ```
1. Rodar o serviço com o arquivo editado
    ```
    .\mosquitto -c .\mosquitto.conf -v
    ```
1. Caso o serviço já esteja rodando pelo Windows, abrir o gerenciador de serviços e parar o serviço Mosquitto Broker antes de rodar o comando acima

# Configurar o broker no MacOS - Homebrew
1. Abrir o arquivo `/opt/homebrew/etc/mosquitto/mosquitto.conf` e adicionar
    ```
    allow_anonymous true
    listener 1883 0.0.0.0
    ```
1. Habilitar e iniciar o serviço
    ```
    brew services start mosquitto
    ```
