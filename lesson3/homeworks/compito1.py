'''
Creare un programma che prenda in input dall'utente una serie di parole o punteggiatura (sono ammessi solo . , ! e ?), una per volta. L'inserzione si deve interrompere quando l'utente inserisce la stringa "stop".

Finita l'inserzione si stampi la serie di frasi risultante, andando a capo dopo ogni frase (ossia dopo ogni ., ! o ?). Assicurarsi che non vi siano spazi prima della , e che le maiuscole siano corrette.
'''
print("\n____________________________________________\n\n")
print("compito 1\n___________________\n")

list_txt=[]

while "stop" not in list_txt:
    txt=input("Please, insert a single word or \", ! ?\" characters: ")
    txt_strip=txt.strip()
#memo: quale controllo implementare per ammettere solo la punteggiatura ', . ! ?' e anche solo testo a-z/A-Z??
    if txt_strip!="":
        if txt_strip.find(" ")!=-1:
            print(f"error! space detected in {txt_strip}. Remind: insert just ONE word")
        else:
            list_txt.append(txt_strip)
            join=" ".join(list_txt)
            if "stop" in join:
                index_stop=join.find("stop")
                join=join[:index_stop-1]+" "
                for c in join:
                    if ("," in c or "." in c or "!" in c or "?" in c):
                        c=c.strip()
                        join=join.replace(f" {c} ",f"{c}\n")
#memo: capitalize delle lettere dopo la punteggiatura?
    else:
        print("Empty!")

    
print(join)