'''
Disegnare lo stato della memoria, riga per riga, del seguente programma:
'''
# inserisce nel global frame 'doubler' e punta nell'heap ad una funzione doubler(l)
def doubler(l):
    # riga 7 e 8 non vengono 'allocate' in memoria
	for i in range(len(l)):
		l[i] = l[i]*2
# inserisce nel global frame l1 e punta nell'heap a una lista [1,2,3]	
l1 = [1,2,3]
# richiama la funzione doubler nell'heap, ma non essendo definito l allora restituisce errore
doubler(l)