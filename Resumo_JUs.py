#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def resumo():
    ocorrencias=str(input("ocorrencias"))
    print("informe todos os valores de produção")
    total=str(input("unidades totais?"))
    meta=str(input("meta por turno"))
    total_p=int(input("total palets"))
    massas=int(input("massas?"))
    isetup=int(input("meta por turno"))
    fsetup=str(input("meta por turno"))
    rejeito_1=input("rejeito do desmolde?")
    rejeito_2=input("Decoradora?")
    rejeito_3=input("Embalagem 1")
    rejeito_4=input("Embalagem 2")
    
    faltas=str(input("faltas"))
    ferias=str(input("ferias"))
    
    
    print("\n ## AGORA LINHA FAMILIA ## \n\n ")
    
    ocorrencias_f=str(input("ocorrencias"))
    print("informe todos os valores de produção")
    total_f=int(input("unidades totais?"))
    meta_f=int(input("meta por turno"))
    total_p_f=str(input("total palets"))
    massas_f=int(input("massas?"))
    isetup_f=int(input("meta por turno"))
    fsetup_f=int(input("meta por turno"))
    
    rejeito_f1=input("Forma virada?")
    rejeito_f2=input("Cru?")
    rejeito_f3=input("Baixo peso?")
    rejeito_f4=input("Fora de posição?")
    rejeito_f5=str(input("Mordentes"))
    rejeito_f6=str(input("Plastico"))
    pesagem_f=str(input("Pesagem"))
    faltas_f=str(input("Faltas"))
    afastado_f=str(input("Afastado\n"))
    Ferias_f=str(input("ferias?\n"))
    
    return print(""" \nResumo Operacional - Turno 2

Linha 01:

Ocorrência de Segurança/Meio Ambiente: \n
- {}

Produção: \n
- {}
- {}
- {}
- {}
- {}
- {}
Ocorrências: \n
- {}

Rejeito/Perda 01: \n
- Desmolde =  {} kg; \n
- Decoradora = {} kg; \n
- Embalagem 1 = {} kg; \n
- Embalagem 2 = {} kg; \n
- Plástico = {} kg; \n

Linha 02


Produção: \n
- {}
- {}
- {}
- {}
- {}
- {}
Ocorrência de Segurança/Meio Ambiente: \n
- {}



Rejeito/Perda 02:\n
- Forma virada = {} Kg;\n
- Cru= {}Kg\n
- Baixo peso= {}Kg;\n
-Fora de posição= {}Kg;\n
-Mordente= {}Kg;\n
-Plastico: {}Kg.\n

Pesagem:\n
- {}

 

Faltas (nomes):\n
 - {}



Afastado (nomes):\n
-{}


Férias (nomes):\n
- {}.""".format(ocorrencias,total,meta,total_p,massas,isetup,fsetup,rejeito_1, rejeito_2, rejeito_3, rejeito_4,  faltas, ferias,
        ocorrencias_f,total_f,meta,total_p_f,massas_f,isetup_f,fsetup_f,
        rejeito_f1,rejeito_f2,rejeito_f3,rejeito_f4,rejeito_f5,rejeito_f6,pesagem_f,faltas_f,afastado_f,Ferias_f))


# In[ ]:


resumo()
    

