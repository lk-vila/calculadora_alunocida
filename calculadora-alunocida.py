# Esse eh um programa para o calculo de medias suicidas
def main():
    #Calcula a media das notas das provas
    n_notas_p = int(input("Digite o numero de notas de provas: "))
    media_p = cal_media(n_notas_p, 1)
    print("\n A media das notas das suas provas eh ", media_p,"\n")

    #Calcula a media das notas dos trabalhos
    n_notas_t = int(input("Digite o numero de notas de trabalhos: "))
    media_t =cal_media(n_notas_t, 2)
    print("\n A media das notas dos seus trabalhos eh", media_t,"\n")

    #Calcula a media final das duas medias
    media_final = cal_media_final(media_p, media_t)
    print("A sua nota final eh: ", media_final,"\n")
    #Define qual vai ser o comentario sobre a nota
    if media_final >= 5:
        if  media_final == 5:
            print("Parabens, 5 eh 10!")
        else:
            print("Parabens, aprovado!")
    else:
        if media_final >= 3:
            print("Vish, ta de REC.")
        else:
            print("Vish, ta de DP.")

def cal_media(n_notas, id):
    lista_notas = []
    pass_p = 0

    #Define se as notas sao de provas ou trabalhos
    if id == 1:
        tipo_nota = "da prova"
    else:
        tipo_nota = "do trabalho"

    #Cria a lista de notas
    while pass_p != n_notas:
        lista_notas.append(float(input("\n Digite o valor da nota {} {}: ".format(tipo_nota, pass_p + 1))))
        pass_p = pass_p+1

    #Retorna a soma das notas % pelo numero de notas
    media = sum(lista_notas)/n_notas
    return media

def cal_media_final(media_p, media_t):
    #Coloca as medias em ordem crescente
    lista_medias = [media_p, media_t]
    lista_medias.sort()

    #Define se vai haver media suicida ou nao
    if media_p < 5 or media_t < 5:
        return lista_medias[0]
    else:
        return media_p*0.6 + media_t*0.4

main()