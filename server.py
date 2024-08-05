import socket
import json
def server(host = 'localhost', port=8082):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)

    print ("Iniciando o servidor em %s porta %s" % server_address)
    sock.bind(server_address)
    sock.listen(5)

    ##dicionário
    table_data = {
        1: ["Importante", "Significativo", "Valoroso", "Respeitável"],
        2: ["Apresentar", "Expor", "Exibir", "Publicar"],
        3: ["Processo", "Método", "Decurso", "Sequencia"],
        4: ["Trabalho", "Ofício", "Ocupação", "Serviço"],
        5: ["Necessário ", "Indispensável", "Fundamental", "Substancial"],
        6: ["Feliz", "Alegre", "Afortunado", "Bem-aventurado"],
        7: ["Computar", "Estivar", "Calcular", "Avaliar"],
        8: ["Através", "Mediante", "Transversalmente ", "Por meio de"]
    }

    def getValue(data):
        for chave, lista_valores in table_data.items():
            for item in lista_valores:
                if (item == data):
                    return [x for x in table_data[chave] if x != item]
                    
    i = 0
    while True: 
        print ("Esperando para receber mensagem do cliente")
        client, address = sock.accept() 
        data = client.recv(data_payload)
        lista = getValue(data.decode('utf-8'))

        # Serializando a lista para JSON
        lista_json = json.dumps(lista)
        # Codificando em UTF-8
        dados_codificados = lista_json.encode('utf-8')

        if data:
            print ("Data: %s" %data)
            client.send(dados_codificados)
            client.close()
            i+=1
                     
server()