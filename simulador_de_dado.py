# Simulador de dado 
# Simular o uso de um dado, gerando um valor de 1 ate 6 
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'voce gostaria de gerar um novo para o dado?'

        def Iniciar(self):
            resposta = input(self.mensagem)
            try:
                if resposta == 'sim' or resposta == 's':
                    self.GerarValorDoDado()
                elif resposta == 'nao' or resposta == 'n':
                    print('Agredecemos a sua participacao!')
                else:
                    print('Favor digitar sim ou nao')
            except:
                print('Ocorreu um erro ao receber sua resposta')

        def GerarValorDoDado(self):
            print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()           