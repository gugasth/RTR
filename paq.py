def organiza_timeslots(dado, paq):
    timeslot = []

    # primeiro quadro
    first = 256
    
    # segundo quadro
    second = 512
    
    # Procura o PAQ
    if dado[first : first+1] == '1' and dado[second : second + 8] == paq:
        # Adiciona na lista 'timeSlot', de 8 em 8 bits
        timeslot = [dado[j : j+8] for j in range(0, second, 8)]    
    return timeslot

with open('RX(vetor)MQ_v2.txt') as arq:
    dado = arq.read()
    dado = dado.replace(' ', '')
    start = 0

    PAQ = '10011011'
    quadro = 0
    
    while True:
        # Encontra o PAQ
        
        start = dado.find(PAQ, start)
        # Ao terminar o arquivo, sai do loop
        if start == -1:
            break
        # Enquanto não terminar o arquivo
        else:
            timeslot = organiza_timeslots(dado[start:], PAQ)        
            if len(timeslot) > 0:
                PAQ = (timeslot.pop(0))
                quadro += 1
                print(f'Quadro: {quadro}')
                print(f'timeslot 0 (paq): {PAQ}, encontrado na posição {start}')
                for idx, i in enumerate(timeslot):
                    if idx > 30:
                        if idx == 31:
                            quadro += 1
                            print(f'Quadro: {quadro}')
                        ts = idx - 32
                    else:
                        ts = idx
                    print(f'timeslot {ts + 1}: {i}')
                
            start += 1

