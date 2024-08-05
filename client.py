import socket
def client(host = 'localhost', port=8082): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address)

    def print_table():
        table_data = [
            ["Importante ", "Significativo ", "Valoroso", "Respeitável"],
            ["Apresentar ", "Expor", "Exibir", "Publicar"],
            ["Processo", "Método", "Decurso", "Sequencia"],
            ["Trabalho", "Ofício", "Ocupação", "Serviço"],
            ["Necessário ", "Indispensável ", "Fundamental", "Substancial"],
            ["Feliz", "Alegre", "Afortunado", "Bem-aventurado"],
            ["Computar", "Estivar", "Calcular", "Avaliar"],
            ["Através", "Mediante", "Transversalmente ", "Por meio de"]
        ]
  
        col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table_data)]

        for i, col_width in enumerate(col_widths):
            print(f"{table_data[0][i]:<{col_width}}", end="")
        print()

        for row in table_data[1:]:
            for i, col_width in enumerate(col_widths):
                print(f"{row[i]:<{col_width}}", end="")
            print()


    try: 
        # Send data
        print("\n ## Escolha uma palavra mostrada abaixo ##")
        print_table()
        
        nome = input("\n\n Qual palavra foi escolhida ? ")
        
        message = nome 
        print ("Enviando palavra:  %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message)
        while amount_received < amount_expected: 
            data = sock.recv(1024) 
            amount_received += len(data)
            lista_recebida = data.decode('utf-8')
            
            print ("\nPalavras sinonimas: ",lista_recebida)

    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Fechando a conexão com o servidor") 
        sock.close() 
client()