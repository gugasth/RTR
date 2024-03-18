def encontraPaq(dado, paq):
    timeSlot = []

    A = 256
    fim = 512
    
    # Procura o PAQ
    if dado[A : A+1] == '1' and dado[fim : fim + 8] == paq:
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
    
    while True:
        start = dado.find(paq, start)
        print('PAQ encontrado na posição:', start)

        # Ao terminar o arquivo, sai do loop
        if start == -1:
            break
        # Enquanto não terminar o arquivo
        else:
            timeSlot = encontraPaq(dado[start:], paq)
            if len(timeSlot) > 0:
                paq = (timeSlot.pop(0))            
            if len(timeSlot) > 0:
                for idx, i in enumerate(timeSlot):
                    print(f'Quadro {idx}: {i}')
                print('Quadro 63 (paq):', paq)
            #print(i)
            start += 1
