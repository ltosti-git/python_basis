# txt="Ciao \t\"Enkk\", prova"
# print("Ciao" or "prova" in txt)


# txt2="Silicon Valley"
# print(txt2.split("i"))

# x="-".join(["code","is","ok"])
# x="-".join(txt2)
# print(x)

from string import punctuation


list_txt=[]
# list_pr=["ciao","come","stai",",","tutto","bene","?","si","grazie"]
# list_pr=list_pr[:-1]
# print(list_pr)

while "stop" not in list_txt:
    txt=input("Please, insert a single word or \", ! ?\" characters: ")
    txt_strip=txt.strip()

    if txt_strip!="":
        if txt_strip.find(" ")!=-1:
            print(f"error! space detected in {txt_strip}. Remind: insert just ONE word")
        else:
            list_txt.append(txt_strip)

            if "stop" in list_txt[-1]:
                list_txt[0]=list_txt[0].capitalize()

                for i in range(len(list_txt)):
                    if ("." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i]):               
                        if list_txt[i+1]!="stop":
                            list_txt[i+1]=list_txt[i+1].capitalize()   

                join_list_txt=" ".join(list_txt)
                index_stop=join_list_txt.find("stop")
                join_list_txt=join_list_txt[:index_stop-1]+" "                
                
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
    # if ("." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i]):
    #     print(list_txt[0:i-1])

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

for punct,punct_count in punctuation_dict.items():
    tot_punct+=punct_count
    if punct_count > max:
        max=punct_count
        pref_punct=punct
    else:
        min=punct_count
        min_punct=punct

print(f"the preferred punctuation sign is: {pref_punct} with {max} occurrences")
print(f"the less used punctuation sign is: {min_punct} with {min} occurrences")
print(f"the total number of typed punctuation signs is: {tot_punct}")

# print(join_list_txt_dict)
# print(punctuation_dict)







    
