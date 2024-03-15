## from tkinter import * 

## janela = Tk()
##janela.title("Calculador de médias")
##janela.geometry("400x300")

##label1 = Label(janela, text = "Calculadora de médias escolares", bg='yellow', font=("arial", 10,"bold")).pack()

##janela.mainloop()

def pesos(p1,p2):
    

def LerNotas():
    n = float(input("Digite a nota do aluno:"))
    return n

def tipoMedia(n1,n2):
    tipo = input("Sua escola utilizada media ponderada ou comum?")
    if tipo == "ponderada":
        media = (n1 * 1 + n2 * 2)/3
    elif tipo == "comum":
        media = (n1+n2)/2
    return media

def calculomedia():
    check = True
    a = LerNotas()
    b = LerNotas()
    media = tipoMedia(a,b)
    if (media >= 5.0):
        print("O aluno foi aprovado com: %.1f" % media) 
    else:
        print("O aluno reprovou com: %.1f" % media)
        resposta = input("Deseja fazer recuperação? Responda com S ou N: ")
        if resposta == "S":
            check = True
        else:
            check = False
            
        if check == False:
            print("Você repetiu de ano.")
        else:
            print("Boa sorte, sua recuperação está marcada para 23/04.")
            
calculomedia()

 
            
        

