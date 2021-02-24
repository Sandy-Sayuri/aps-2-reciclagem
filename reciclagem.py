print( """   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  
    =
  =                                        FOX RECICLA!                                                 =   
  =  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 
 
 Este software foi desenvolvido  para te auxiliar a achar um local de descarte adequado ao seu lixo.
 Basta dcigitar os pares de cordenadas(x,y) da sua casa, e o tipo de lixo (papel,plástico,hospitalar,eletronico)
 que quer descartar e o software irá retornar a localidade do descarte mais próximo """)
from math import sqrt
px=[-22.884042,-22.902334,-22.879458,-22.876182,-22.156468]#comceito de lista reciclagem na latitude
py=[-47.055729,-47.052901,-47.879458,-47.036126,-47.154948]#comceito de lista reciclagem na logitude
hx=[-24.856463,-24.986875,-24.94885,-24.5498569,-24.515611]#comceito de lista hospitalar na latitude
hy=[-32.84484,-32.84464,-32,4598784,-32.6464644,-32.454645]#comceito de lista hospitalar na longitude
ex=[-55.86471236,-56.465468,-55.86128,55.8665464,-55.44544]#comceito de lista eletrônico na latitude
ey=[-23.888656,-23.987915,-23.4774547,-23.894949,-23.44684]#conceito de lista eletrônico na logitude
ma=0 #distancia máxima
me=99999999999999999999999999999999999999999999999999999#distancia mínima
encerra="s"
corx=0
cory=0
tipo=0
cort=0
corw=0
d1=0
while(encerra=="s"):
    tipo = int(input("qual tipo de material vc deseja reciclar:\n 1-papel\n2-plástico\n3-vidro\n4-sucata\n5-lixo hospitalar(lixo vindo de hospitais)\n6-lixo eletronico(computador,celular,tablet)/"))
    corx = float(input('digite a coordenada em x:'))#coordenada da latitude
    cory = float(input('digite a coordenada em y:'))#coordenada de longitude        
    if(tipo==1 or tipo == 2 or tipo== 3 or tipo== 4):
        if(tipo== 1):
            print('o tempo de degradação do papel é de 4 á 6 meses')
            print('os cuidados para o armazenamento é seja cauteloso no transporte,Evite a exposição ao ambiente,')
            print('Mantenha seus documentos organizados,Preserve a embalagem do papel,Leia as instruções do fabricante')
        elif(tipo==2):
            print('O tempo de degradação do plástico é de mais de 400 anos')
            print('os cuidados para o armazenamento do plástico mantenha sempre longe de locais descobertos e se for')
            print('um recipiente que pode comter água sempre de cabeça para baixo')
        elif(tipo==3):
            print('o tempo de degradação do metal é de  mais de 100 anos')
            print('os cuidados para o armazenamento do plástico mantenha sempre longe de locais descobertos e se for')
            print('um recipiente que pode comter água sempre de cabeça para baixo')
        elif(tipo==4):
            print('O tempo de degradação do vidro é de mais de 1000 anos')
            print('os cuidados para o armazenamento mantenha sempre longe de locais descobertose se for')
            print('um recipiente que pode comter água sempre de cabeça para baixo') 
    def calculo(corx,cory,px,py):
        d1=(sqrt((corx - px[0]) ** 2) + ((cory-py[0]) ** 2)) 
        d2=(sqrt((corx - px[1]) ** 2) + ((cory-py[1]) ** 2)) 
        d3=(sqrt((corx - px[2]) ** 2) + ((cory-py[2]) ** 2))
        d4=(sqrt((corx - px[3]) ** 2) + ((cory-py[3]) ** 2))
        d5=(sqrt((corx - px[4]) ** 2) + ((cory-py[4]) ** 2))
        if(d1<d2 and d1<d3 and d1<d4 and d1<d5):
            print('O ponto de coleta mais próxima é: ',px[0],py[0])
        elif(d2<d1 and d2<d3 and d2<d4 and d2<d5):
            print('O ponto de coleta mais próxima é: ',px[1],py[1])
        elif(d3<d1 and d3<d2 and d3<d4 and d3<d5):
            print('O ponto de coleta mais próxima é: ',px[2],py[2])
        elif(d4<d1 and d4<d2 and d4<d3 and d4<d5):
            print('O ponto de coleta mais próxima é: ',px[3],py[3])
        elif(d5<d1 and d5<d2 and d5<d3 and d5<d4):       
            print('O ponto de coleta mais próxima é: ',ex[4],ey[4])
    calculo(corx,cory,px,py)   
    if(tipo==5):
        print('O tempo de degradação do lixo eletronico é dividido emtre seus compomentes:')
        print('-chumbo com 15 anos') 
        print('-O níquel com 1,5 milhões de anos') 
        print('-mércurio com 10 anos')
        print('-O zinco com 300 anos')
        print('os cuidados para o armazenamento mantenha sempre longe de locais descobertose se for')
        print('um recipiente que pode comter água sempre de cabeça para baixo, se tenah certasa que o local de armasenameto tenha algum tipo de proteção para que ')
        print('os elemento quimicos prensentes nas bateria do esquipamentos eletronicos não infectem o solo')
    def calculo2(corx,cory,px,py):
        d1=(sqrt((corx - ex[0]) ** 2) + ((cory-ey[0]) ** 2)) 
        d2=(sqrt((corx - ex[1]) ** 2) + ((cory-ey[1]) ** 2)) 
        d3=(sqrt((corx - ex[2]) ** 2) + ((cory-ey[2]) ** 2))
        d4=(sqrt((corx - ex[3]) ** 2) + ((cory-ey[3]) ** 2))
        d5=(sqrt((corx - ex[4]) ** 2) + ((cory-ey[4]) ** 2))
        if(d1<d2 and d1<d3 and d1<d4 and d1<d5):
            print('O ponto de coleta mais próxima é: ',ex[0],ex[0])
        elif(d2<d1 and d2<d3 and d2<d4 and d2<d5):
            print('O ponto de coleta mais próxima é: ',ex[1],ey[1])
        elif(d3<d1 and d3<d2 and d3<d4 and d3<d5):
            print('O ponto de coleta mais próxima é: ',ex[2],ey[2])
        elif(d4<d1 and d4<d2 and d4<d3 and d4<d5):
            print('O ponto de coleta mais próxima é: ',ex[3],ey[3])
        elif(d5<d1 and d5<d2 and d5<d3 and d5<d4):       
            print('O ponto de coleta mais próxima é:',ex[4],ey[4])
        calculo2(corx,cory,px,py)
    if(tipo ==6):
        print('tempo de degradação do lixo hospitalar é de 500 anos')
        print('os cuidados para o armazenamento mantenha em locais onde esse material tenha pouco ou nenhum cotato os pessoa que podem e sempre mande para os locais de')
        print('descarte adequedo o mais rapido possivel')
    def calculo3(corx,cory,px,py):
        d1=(sqrt((corx - hx[0]) ** 2) + ((cory-hy[0]) ** 2))
        d2=(sqrt((corx - hx[1]) ** 2) + ((cory-hy[1]) ** 2))
        d3=(sqrt((corx - hx[2]) ** 2) + ((cory-hy[2]) ** 2))
        d4=(sqrt((corx - hx[3]) ** 2) + ((cory-hy[3]) ** 2))
        d5=(sqrt((corx - hx[4]) ** 2) + ((cory-hy[4]) ** 2))
        if(d1<d2 and d1<d3 and d1<d4 and d1<d5):
            print('O ponto de coleta mais próxima é: ',hx[0],hx[0])
        elif(d2<d1 and d2<d3 and d2<d4 and d2<d5):
            print('O ponto de coleta mais próxima é: ',hx[1],hy[1])
        elif(d3<d1 and d3<d2 and d3<d4 and d3<d5):
            print('O ponto de coleta mais próxima é: ',hx[2],hy[2])
        elif(d4<d1 and d4<d2 and d4<d3 and d4<d5):
            print('O ponto de coleta mais próxima é: ',hx[3],hy[3])
        elif(d5<d1 and d5<d2 and d5<d3 and d5<d4):       
            print('O ponto de coleta mais próxima é: ',hx[4],hy[4])
        calculo3(corx,cory,px,py)
        if(tipo !=1 and 2 and 3 and 4 and 5 and 6):
            print('[ERRO]erro em tipo de lixo')
    encerra=input('deseja continuar?(N/S)')
