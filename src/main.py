from frota import *
import pickle

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro1.ligar()
    elif op == 2:
        carro1.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro1.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Digite o nivel do tanque: '))
    cm = float(input('Digite o consumo medio do carro: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    print('Cadastre segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Digite o nivel do tanque: '))
    cm = float(input('Digite o consumo medio do carro: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    carros = {}
    carro1[id(carro1)] = carro1
    carro2[id(carro2)] = carro2

    try:
        with open('carros.pkl', 'wb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)

    '''
    Controlando o carro até ele atingir 600 Km ou acabar a gasolina dos carros
    '''
    while carro1.get_odometro() < 10000:
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Digite as opcoes[1-3]:"))
            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)
    if carro1.motor_on is True:
        carro1.desligar()
    if carro2.motor_on is True:
        carro2.desligar()
    print(carro1)
    print(carro2)

    if carro1.tanque == 0 and carro2.tanque == 0:
        print('Acabou a gasolina dos carros')