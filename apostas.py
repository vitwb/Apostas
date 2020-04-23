from random import randint


#Função Aposta gera uma aposta seguindo as probabilidades do site
def aposta():    
    valor=(randint(0,54))
    if 1<=valor<=26:
        return 'g' 
    if 27<=valor<=43:
        return 'v'
    if 44<=valor<=54:
        return 'b'
    if valor == 0 :
        return 'GG'

#Valores de  inicio
VI = 1800.0  #valor inicial do apostador
vab = 10.0   #valor inicial de aposta da cor vermelha
vaa=10       #valor inicial de aposta da cor azul 
apst=5.0     #multiplicado de ganho para a cor
multi = 1.3  #multiplicador caso o jogador perda a rodada
vmax=0       #armazena a aposta máxima

#rodadas de aposta:
for x in range (10):
    for x in range(1000):        
        apost=aposta()
        #aposta azul
    if vaa>vmax:
        vmax=vaa
    if apost == 'b': 
        saldoa = VI + (vaa *apst)
        vaa= 10
    else:
        saldoa = VI - vaa
        vaa = vaa*multi
        #aposta vermelha
    if vab>vmax:
        vmax=vab
    if apost == 'v':
        saldov = VI + (vab *3.0)
        vab= 10
    else:
        saldov = VI - vab
        vab = vab*1.7
   
#resultados:
   
if saldoa>VI:
        print("lucro")
else:
        print("prejuíso")
                    
print(saldoa, vmax)
print(saldov, vmax)         
    