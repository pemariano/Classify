# ********************* QUICK RECURSIVO **********************
def particiona(lista, inicio, fim):
    i, j = inicio, fim
    pivo = lista[fim]
    while True:
        # aumentado i
        while i < j and lista[i] <= pivo: i = i + 1
        if i < j:
            lista[i], lista[j] = pivo, lista[i]
        else: break
        # diminuindo j
        while i <j and lista[j] >= pivo: j = j -1
        if i < j: lista[i], lista[j] = lista[j], pivo
        else: break
    return i
        
def QuickRec(lista, inicio, fim):
    # Se a lista tem mais de um elemento, ela será
    # particionada e as duas partições serão classificadas
    # pelo mesmo método Quick Sort
    if inicio < fim:
        k = particiona(lista, inicio, fim)
        QuickRec(lista, inicio, k -1)
        QuickRec(lista, k + 1, fim)
        
# ******************* QUICK NÂO RECURSIVO ********************
class PilhaLista:

    '''Pilha como uma lista.'''
    
    # Construtor da classe PilhaLista
    def __init__(self):
        self._pilha = [] # lista que conterá a pilha

    # retorna o tamanho da pilha
    def __len__ (self):
        return len(self._pilha)

    # retorna True se pilha vazia
    def is_empty(self):
        return len(self._pilha) == 0

    # empilha novo elemento e
    def push(self, e):
        self._pilha.append(e)

    # retorna o elemento do topo da pilha sem retirá-lo
    # exceção se pilha vazia
    def top(self):
        if self.is_empty( ):
            raise Empty("Pilha vazia")
        return self._pilha[-1]

    # desempilha elemento
    # excessão se pilha vazia
    def pop(self):
        if self.is_empty( ):
            raise Empty("Pilha vazia")
        return self._pilha.pop( )

def particiona(lista, inicio, fim):
    i, j = inicio, fim
    pivo = lista[fim]
    while True:
        # aumentado i
        while i < j and lista[i] <= pivo: i = i + 1
        if i < j:
            lista[i], lista[j] = pivo, lista[i]
        else: break
        # diminuindo j
        while i <j and lista[j] >= pivo: j = j -1
        if i < j: lista[i], lista[j] = lista[j], pivo
        else: break
    return i
    
def Quick(lista):
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(lista) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    while not Pilha.is_empty():
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento
        if fim - inicio > 0:
            k = particiona(lista, inicio, fim)
            # Empilhe as sub-listas resultantes
            Pilha.push((inicio, k - 1))
            Pilha.push((k + 1, fim))
            
# ************************************************************
import time
import copy
    
def VerifClass(lista):
    # verifica se TAB[i] ≤ TAB[i+1]
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def organiza(lista): #recebe lista
    nlista = []
    for i in lista:
        txt = i.split(",")
        txt2 = txt[1].split("/")
        txt3 = [txt[0], txt2[2], txt2[1], txt2[0], txt[2]]
        nlista.append(txt3)
    return nlista #devolve matriz

def desorganiza(lista): #recebe matriz
    nlista = []
    for i in lista:
        nlista.append(str(i[0]) + "," + str(i[3]) + "/" + str(i[2]) + "/" + str(i[1])
                      + "," + str(i[4]))
    return nlista #devolve lista
    
def escreve(nome,lista):
    arquivo = open(nome, "w")
    for i in lista:
        arquivo.write(i)
    arquivo.close()

def main():
    while True:
        arquivo_entrada = str(input("Entre com o nome do arquivo origem: "))
        if arquivo_entrada == "fim": break #para o programa
        try: 
            arquivo_lido = open(arquivo_entrada,"r") #le o arquivo
            lista = arquivo_lido.readlines() #transforma o arquivo numa lista
        except:
            print()
            print("Arquivo digitado inválido")
            continue
        
        #lista = lista com lista[i] = 'nome,dd/mm/aaaa,num/n'
        novalista = organiza(lista) #troca dd/mm/aaaa por aaaa/mm/dd e divide os campos
        #novalista = matriz com lista[i] = ['nome', 'aaaa', 'mm', 'dd', 'num/n'] / ex.: lista[i][2] = 'mm'
        #é com a lista nesse formato que vamos classifica-la
        lista_1 = copy.deepcopy(novalista)
        lista_2 = copy.deepcopy(novalista)
        lista_3 = copy.deepcopy(novalista)
        
        arquivo_destino = input("Entre com o nome do arquivo destino: ")
        
        tempos = []
        # Quick recursivo:
        tempos.append(time.perf_counter()) #tempos[0]
        QuickRec(lista_1, 0, len(lista_1) - 1 )
        tempos.append(time.perf_counter()) #tempos[1]
        if not VerifClass(lista_1):
            print("Método quick recursivo não classificou a lista")
            break
        # Quick não recursivo
        tempos.append(time.perf_counter()) #tempos[2]
        Quick(lista_2)
        tempos.append(time.perf_counter()) #tempos[3]
        if not VerifClass(lista_2):
            print("Método quick não recursivo não classificou a lista")
            break
        # Sort() do Python
        tempos.append(time.perf_counter()) #tempos[4]
        lista_3.sort()
        tempos.append(time.perf_counter()) #tempos[5]
        if not VerifClass(lista_3):
            print("Método sort() do python não classificou a lista")
            break
        
        arquivo_saida = desorganiza(lista_3) #volta os dados pro formato original
        escreve(arquivo_destino,arquivo_saida) #faz o arquivo de saída
        
        print()
        print("Tempo para classificar a tabela:")
        print()
        print("Método Quick Recursivo: {} segundos".format(tempos[1]-tempos[0])) 
        print("Método Quick Não Recursivo: {} segundos".format(tempos[3]-tempos[2])) 
        print("Método Sort() do Python: {} segundos".format(tempos[5]-tempos[4]))
        print()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
               
if __name__ == '__main__':
    main()