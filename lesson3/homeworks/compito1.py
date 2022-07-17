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

    
print(f"\nInserts completed!\nYou typed:\n{join_list_txt}")

print("And now, some useful info:")

sum_words=0
for i in range(len(list_txt)):
    if not ("," in list_txt[i] or "." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i] or "stop" in list_txt[i]):    
        sum_words+=1

join_list_txt_dict={}
punctuation_dict={}

join_list_txt=join_list_txt.replace("\n","").replace(" ","")


for c in join_list_txt:
    c=c.lower()
    if not ("," in c or "." in c or "!" in c or "?" in c):        
        if c in join_list_txt_dict.keys():
            join_list_txt_dict[c]+=1
        else:
            join_list_txt_dict[c]=1
    else:
        if c in punctuation_dict.keys():
            punctuation_dict[c]+=1
        else:
            punctuation_dict[c]=1

max=0
min=0
pref_char=""
min_char=""

for word,word_count in join_list_txt_dict.items():
    if word_count > max:
        max=word_count
        pref_char=word
    else:
        min=word_count
        min_char=word

print(f"the preferred character is: {pref_char} with {max} occurrences")
print(f"the less used character is: {min_char} with {min} occurrences")
print(f"the total number of typed words is: {sum_words}")

max=0
min=0
pref_punct=""
min_punct=""
tot_punct=0
phrases=0

for punct,punct_count in punctuation_dict.items():
    tot_punct+=punct_count
    if punct_count > max:
        max=punct_count
        pref_punct=punct
    else:
        min=punct_count
        min_punct=punct
    
    if not("," in punct):
        phrases+=punct_count


print(f"the preferred punctuation sign is: {pref_punct} with {max} occurrences")
print(f"the less used punctuation sign is: {min_punct} with {min} occurrences")
print(f"the total number of typed punctuation signs is: {tot_punct}")

print(f"the total number of phrases is: {phrases}")

# print(join_list_txt_dict)
# print(punctuation_dict)