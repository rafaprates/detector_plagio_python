import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    result = []
    while i < len(as_a):
        result.append((abs(as_a[i] - as_b[i]))/6)
        i += 1

    return result

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    lista_frases, lista_palavras, wal = [], [], []
    
    qtdCarSentenca = 0
    for sent in lista_sentencas:
        lista_frases.extend(separa_frases(sent))
        qtdCarSentenca += len(sent)

    qtdCarFrase = 0 
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
        qtdCarFrase += len(frase)

    #Conta o tamanho total das palavras.
    tamTotalPalavras = 0
    for palavra in lista_palavras:
        tamTotalPalavras += len(palavra)
     
    #Conta a quantidade de palavras.
    qtdPalavras = len(lista_palavras)

    #Calcula o tamanho médio das palavras
    wal = (tamTotalPalavras / qtdPalavras)

    #Relação Type-Token
    ttr = n_palavras_diferentes(lista_palavras) / qtdPalavras

    #Razão Hapax Legomana
    hlr = n_palavras_unicas(lista_palavras) / qtdPalavras

    #Tamanho médio de sentença
    sal = qtdCarSentenca / len(lista_sentencas)

    #Calcula a complexidade de sentença
    sac = len(lista_frases) / len(lista_sentencas)

    #Calcula o tamanho médio de frase
    pal = qtdCarFrase / len(lista_frases)

    return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_ass = []

    for texto in textos:
        lista_ass.append(calcula_assinatura(texto))

    for ass in lista_ass:
        results = compara_assinatura(ass, ass_cp)

    i, index = 0, 0 
    while i < len(results):
        ans = results[0]
        if results[i] < ans:
            ans = index
            textoInfectado = i
        i += 1

    print("O autor do texto", textoInfectado, "está infectado por COH-PIAH")

    return textoInfectado

def main():

    ass_cp = le_assinatura()
    
    textos = le_textos()

    avalia_textos(textos, ass_cp)
    
main()
