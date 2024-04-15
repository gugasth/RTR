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

def encontraPamq(pamq, quadro):
    multiQuadro = []

    for q in quadro:            
        # verifica o timeslot 16
        if q[16][:3] == pamq:  
            if not multiQuadro:
                multiQuadro.append(q)
            else:
                break    
        elif multiQuadro:
            multiQuadro.append(q)

    return multiQuadro

with open('RX(vetor)MQ_v2.txt') as arq:
    dado = arq.read()
    dado = dado.replace(' ', '')
    start = 0

    bits_alinhados = []
    PAQ = '10011011'
    bits_alinhados.append(PAQ)
    
    while True:
        # Encontra o PAQ
        
        start = dado.find(PAQ, start)
        
        # Ao terminar o arquivo, sai do loop
        if start == -1:
            break
        # Enquanto não terminar o arquivo
        else:
            timeslot = organiza_timeslots(dado[start:], PAQ)  
            bits_alinhados.extend(timeslot)      
            if len(timeslot) > 0:
                PAQ = (timeslot.pop(0))
                for idx, i in enumerate(timeslot):
                    print(f'timeslot {idx}: {i}')
                print(f'timeslot 63 (paq): {PAQ}, encontrado na posição {start}')
            start += 1

    quadro_alinhado = ''.join(map(str, bits_alinhados))
    print(quadro_alinhado)
    
    
    
    
    
    
    