#gustavo garcia pereira

import math
global constante_K

constante_K = 9*10**9

def demonstracao():
    rad = 0.523599
    print(rad)
    print(round(math.radians(30),6))


    #funcao matematica recebe em radiano
    #conver o gral para radiano

    print((-128*10**-9)*math.cos(round(math.radians(30),6))+(128*10**-9)*math.cos(round(math.radians(30),6))+(-256*10**-9)*math.cos(round(math.radians(30),6)))
    print((-128*10**-9)*math.sin(round(math.radians(30),6))+(-128*10**-9)*math.sin(round(math.radians(30),6))+(+256*10**-9)*math.sin(round(math.radians(30),6)))
    
    v1=[]
    v2=[]
    v3=[]
    
    v1.append((-128*10**-9)*math.cos(round(math.radians(30),6)))
    v1.append((-128*10**-9)*math.sin(round(math.radians(30),6)))
    
    v2.append((128*10**-9)*math.cos(round(math.radians(30),6)))
    v2.append((-128*10**-9)*math.sin(round(math.radians(30),6)))
    
    v3.append((-256*10**-9)*math.cos(round(math.radians(30),6)))
    v3.append((+256*10**-9)*math.sin(round(math.radians(30),6)))
    

    print('x',v1[0])
    print('y',v1[1])

    print('x',v1[0])
    print('y',v1[1])

    print('x',v1[0])
    print('y',v1[1])
    


    vetorT=[]
    vetorT.append(v1[0]+v2[0]+v3[0])
    vetorT.append(v1[1]+v2[1]+v3[1])

    print('{:0.4}'.format(vetorT[0]))
    print('{:0.4}'.format(vetorT[1]))

    # print('1 ',(-128*10**-9)*math.sin(30))
    # print('2 ',(-128*10**-9)*math.sin(30))
    # print('3 ',(156*10**-9)*math.sin(30))

    # print('1 ',(-128*10**-9)*-5614.986)
    # print('2 ',(-128*10**-9)*-5614.986)
    # print('3 ',(156*10**-9)*-5614.986)

    # print(math.cos(30))
    
def demonstracao2():
    print("Programa de fisica")


    #print("Calculo do Campo Eletrico")


    #dcm = 1.3 #em centimetro
    dcm = 15
    dm  = dcm/100 #converter para m
    #r = 0.0092
    # q1 = 12*10**-9
    # q2 = -24*10**-9
    # q3 = 31*10**-9
    # q4 = 17*10**-9
    q1 = 3.2*10**-19 
    q2 = -3.2*10**-19
    q3 = -6.4*10**-19


    #q5 = 3.2*10**-19

    #print('Calculo Potencial P1 = {0:.2f}'.format(calculoPotencial(q1,q2,q3,q4)))


    #teste = calculoPotencialT(q1)+calculoPotencialT(q2)+calculoPotencialT(q3)+calculoPotencialT(q4)

    #print('Calculo Potencial  Teste1 = {0:.2f}'.format(teste))


    print('Calculo Campo Eletrico E1 = {}'.format(calculoCampoEletrico(q1)))
    print('Calculo Campo Eletrico E2 = {}'.format(calculoCampoEletrico(q2)))
    print('Calculo Campo Eletrico E3 = {}'.format(calculoCampoEletrico(q3)))
    #print('Calculo Campo Eletrico E4 = {}'.format(calculoCampoEletrico(q4)))


    E1 = calculoCampoEletrico(q1)
    E2 = calculoCampoEletrico(q2)
    E3 = calculoCampoEletrico(q3)
    #E4 = calculoPotencialT(q4)
    print('ddddd = ',E1)
    print('ddddd = ',E2)
    print('ddddd = ',E3)

    vetor1 = []
    vetor2 = []
    vetor3 = []
    #vetor4 = []

    anguloVetorEmGraus = 30
    


    vetor1.append(-E1*math.cos(round(math.radians(anguloVetorEmGraus),6)))
    vetor1.append(-E1*math.sin(round(math.radians(anguloVetorEmGraus),6)))

    vetor2.append(E2*math.cos(round(math.radians(anguloVetorEmGraus),6)))
    vetor2.append(-E2*math.sin(round(math.radians(anguloVetorEmGraus),6)))

    vetor3.append(-E3*math.cos(round(math.radians(anguloVetorEmGraus),6)))
    vetor3.append(E3*math.sin(round(math.radians(anguloVetorEmGraus),6)))

    #vetor4.append(E4*math.cos(round(math.radians(45),6)))
    #vetor4.append(-E4*math.sin(round(math.radians(45),6)))

    print('')
    print('vetor1 x {:0.4}'.format(vetor1[0]))
    print('vetor1 y {:0.4}'.format(vetor1[1]))
    print('')
    print('vetor2 x {:0.4}'.format(vetor2[0]))
    print('vetor2 y {:0.4}'.format(vetor2[1]))
    print('')
    print('vetor3 x {:0.4}'.format(vetor3[0]))
    print('vetor3 y {:0.4}'.format(vetor3[1]))
    print('')
    #print('vetor4 x',vetor4[0])
    #print('vetor4 y',vetor4[1])


    vetorR = []

    vetorR.append(vetor1[0]+vetor2[0]+vetor3[0])
    vetorR.append(vetor1[1]+vetor2[1]+vetor3[1])
    print('vetorR x {:0.4}'.format(vetorR[0]))
    print('vetorR y {:0.4}'.format(vetorR[1]))

def calculoPotencial(q1,q2,q3,q4):
    #print("Calculo de Potencial eletrico")
    
    r = math.sqrt((((dm)**2)+((dm)**2)))/2
    
    r = round(r,4)     #truncar o r 
    #print(r)
    
    #formula potencial eletrico
    potencial = (constante_K*(q1+q2+q3+q4)/r)
    #print(potencial)
    return potencial

def calculoPotencialT(q):
    #print("Calculo de Potencial eletrico")
    
    r = math.sqrt((((dm)**2)+((dm)**2)))/2
    
    r = round(r,4)     #truncar o r 
    #print(r)
    
    #formula potencial eletrico
    potencial = (constante_K*(q)/r)
    #print(potencial)
    return potencial
    
def calculoCampoEletrico(q):
    if q<0:
    #    #print("q menor que zero {}".format(q))
          q=q*-1
    #      #print("q menor que zero {}".format(q))


    calculoCampoEletrico = (constante_K*(q)/((dm)**2))
    return calculoCampoEletrico

print('')
print('')
print("       Programa de fisica")
print('')

#print("Calculo do Campo Eletrico")


#dcm = 1.3 #em centimetro
dcm = 1.3
dm  = dcm/100 #converter para m
#r = 0.0092
q1 = 12*10**-9
q2 = -24*10**-9
q3 = 31*10**-9
q4 = 17*10**-9



#q5 = 3.2*10**-19
print('')

print('Calculo Potencial P1 = {0:.2f}'.format(calculoPotencial(q1,q2,q3,q4)))

print('')
somatorioDasCargas = calculoPotencialT(q1)+calculoPotencialT(q2)+calculoPotencialT(q3)+calculoPotencialT(q4)

print('Calculo Potencial  Teste1 = {0:.2f}'.format(somatorioDasCargas))
print('')

print('Calculo Campo Eletrico E1 = {0:.6}'.format(calculoCampoEletrico(q1)))
print('Calculo Campo Eletrico E2 = {0:.6}'.format(calculoCampoEletrico(q2)))
print('Calculo Campo Eletrico E3 = {0:.6}'.format(calculoCampoEletrico(q3)))
print('Calculo Campo Eletrico E4 = {0:.6}'.format(calculoCampoEletrico(q4)))

E1 = calculoCampoEletrico(q1)
E2 = calculoCampoEletrico(q2)
E3 = calculoCampoEletrico(q3)
E4 = calculoCampoEletrico(q4)

print('dis',dm)


vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetorR = []

anguloVetorEmGraus = 45

vetor1.append(E1*math.cos(round(math.radians(anguloVetorEmGraus),6)))
vetor1.append(-E1*math.sin(round(math.radians(anguloVetorEmGraus),6)))

vetor2.append(E2*math.cos(round(math.radians(anguloVetorEmGraus),6)))
vetor2.append(E2*math.sin(round(math.radians(anguloVetorEmGraus),6)))

vetor3.append(E3*math.cos(round(math.radians(anguloVetorEmGraus),6)))
vetor3.append(E3*math.sin(round(math.radians(anguloVetorEmGraus),6)))

vetor4.append(-E4*math.cos(round(math.radians(anguloVetorEmGraus),6)))
vetor4.append(E4*math.sin(round(math.radians(anguloVetorEmGraus),6)))


print('')
print('vetor1 x {:0.4}'.format(vetor1[0]))
print('vetor1 y {:0.4}'.format(vetor1[1]))
print('')
print('vetor2 x {:0.4}'.format(vetor2[0]))
print('vetor2 y {:0.4}'.format(vetor2[1]))
print('')
print('vetor3 x {:0.4}'.format(vetor3[0]))
print('vetor3 y {:0.4}'.format(vetor3[1]))
print('')
print('vetor4 x {:0.4}'.format(vetor4[0]))
print('vetor4 y {:0.4}'.format(vetor4[1]))
print('')



vetorR.append(vetor1[0]+vetor2[0]+vetor3[0]+vetor4[0])
vetorR.append(vetor1[1]+vetor2[1]+vetor3[1]+vetor4[1])
print('vetorR x {0:.4}'.format(vetorR[0]))
print('vetorR y {0:.4}'.format(vetorR[1]))

#math.hypot(x, y) reorna a hipotenusa
    
# dcm = 15
# dm  = dcm/100
#demonstracao2()
