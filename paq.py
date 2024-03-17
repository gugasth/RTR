def encontraPaq(dado, paq):
    timeSlot = []

    A = 256
    fim = 512
    
    # Procura o PAQ
    if dado[A : A+1] == '1' and dado[fim : fim + 8] == paq:
        print(dado[0:fim], end='')
        # Adiciona na lista 'timeSlot', de 8 em 8 bits
        timeSlot = [dado[j : j+8] for j in range(0, fim, 8)]    
    return timeSlot

with open('RX(vetor)MQ_v2.txt') as arq:
    dado = arq.read()
    dado = dado.replace(' ', '')
    start = 0

    quadro = []
    paq = '10011011'
    paqVerd = []
    
    print('\nBits alinhados:')

    while True:
        start = dado.find(paq, start)

        # Ao terminar o arquivo, sai do loop
        if start == -1:
            break
        # Enquanto não terminar o arquivo
        else:
            timeSlot = encontraPaq(dado[start:], paq)
            print(timeSlot)
            print(start)
            start += 1