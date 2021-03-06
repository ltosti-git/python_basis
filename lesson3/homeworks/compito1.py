'''
Creare un programma che prenda in input dall'utente una serie di parole o punteggiatura (sono ammessi solo . , ! e ?), una per volta. L'inserzione si deve interrompere quando l'utente inserisce la stringa "stop".

Finita l'inserzione si stampi la serie di frasi risultante, andando a capo dopo ogni frase (ossia dopo ogni ., ! o ?). Assicurarsi che non vi siano spazi prima della , e che le maiuscole siano corrette.

Riportare poi un po' di statistiche in merito al testo, ed in particolare:

Numero di parole ricevute (non si contino i segni di interpunzione)
Numero di segni di interpunzione
Numero di frasi
Il carattere più frequente
Il carattere meno frequente
'''
print("____________________________________________\n")
print("compito 1\n___________________\n")

list_txt=[]

while "stop" not in list_txt:
    txt=input("Please, insert a single word or \", ! ?\" characters: ")
    txt_strip=txt.strip()
    #memo: implements checks and controls for admitting only following punctuation ', . ! ?' and [a-z][A-Z] text
    if txt_strip!="":
        
        if txt_strip.find(" ")!=-1:
            print(f"error! space detected in {txt_strip}. Remind: insert just ONE word")
        else:
            list_txt.append(txt_strip)

            if "stop" in list_txt[-1]:
                list_txt[0]=list_txt[0].capitalize()
                #loop for capitalize all the words after full stop and marks
                for i in range(len(list_txt)):
                    if ("." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i]):               
                        if list_txt[i+1]!="stop":
                            list_txt[i+1]=list_txt[i+1].capitalize()   

                join_list_txt=" ".join(list_txt)
                index_stop=join_list_txt.find("stop")
                join_list_txt=join_list_txt[:index_stop-1]+" "       

                #loop for paragraph after punctuation
                for c in join_list_txt:
                    
                    if ("." in c or "!" in c or "?" in c):                  
                        c=c.strip()      
                        join_list_txt=join_list_txt.replace(f" {c} ",f"{c}\n")
                        
                        
                    if ("," in c):
                        c=c.strip()                        
                        join_list_txt=join_list_txt.replace(f" {c} ",f"{c} ")                     
                               
    else:
        print("Empty!")

    
print(join_list_txt)

print("\n Inserts completed! \n Now, some useful stats:")