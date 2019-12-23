#importar bibliotecas
from datetime import datetime
import matplotlib.pyplot as plt
import serial
import time

#configuração da conexão
#definição da porta do Arduino
porta = 'COM4'
#Configuração da velocidade de transmissão Serial
velocidade = 9600
#variável com as configuração de porta e serial
conexao = serial.Serial(porta, velocidade)
#variável de controle de amostras
a = 0

#traz as informações referentes a data e hora
data_e_hora=datetime.now()
#define o formato de apresentação da data
data_e_hora_txt=data_e_hora.strftime('%d%m%Y%H')
#define o nome do arquivo(dia mês ano hora minuto)
nome_arquivo= data_e_hora_txt

def programa():
    #cria novo arviquvo
    #diretório + data e hora(dia mês ano hora minuto) + extensão do arquivo, configuração para leitura e escrita de arquivo) 
    arquivo = open(nome_arquivo+".csv","w+") 

    #variável de controle de amostras
    a = 0
    
    #contagem do número de amostras
    while(a < 10):
    #variável de controle (aumento de 1 em 1)
        a += 1
    #variável que extrai dados de "print" do Arduino
    #readline(x) -> x número máximo de bytes retornados
        leitura = conexao.readline().decode().strip()
    #escreve valor da variável teste
        arquivo.write(str(leitura)+";"+str(a))
        arquivo.write('\n')
    #fecha arquivo
    arquivo.close()

    #abre arquivo
    dataset = open(nome_arquivo+".csv","r")

    #transforma de texto para coluna com separação de ponto e vírgula(;)
    x = []
    y = []
    z = []
    for line in dataset:
        X, Y, Z = line.split(';')
        x.append(X)
        y.append(Y)
        z.append(Z)

    
    print("Object Temperature1:"+str(x)+"°C")
    print("Object Temperature1:"+str(y)+"°C")
    #feha arquivo
    dataset.close()

    #define eixo x e y
    plt.bar(z, x, label='Sensor 1 (°C)', color='blue')
    plt.plot(z, y, label='Sensor 2 (°C)', color='red', marker='o')

    #Define o titulos do gráfico
    plt.title('Temperatura x Amostra')
    plt.xlabel('N° Amostras')
    plt.ylabel('Temperatura °C')

    #plota o gráfico
    plt.legend()
    plt.show()

opcao = 0;
    
while opcao != "2":
    opcao = input("Digite 1 para iniciar testes\nDigite 2 para fechar programa\n")
    if opcao == "1":
        programa()
conexao.close()
