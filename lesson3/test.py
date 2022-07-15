# txt="Ciao \t\"Enkk\", prova"
# print("Ciao" or "prova" in txt)


# txt2="Silicon Valley"
# print(txt2.split("i"))

# x="-".join(["code","is","ok"])
# x="-".join(txt2)
# print(x)

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

                print(list_txt)

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

    
print(join_list_txt)


print("\n Inserts completed! \n Now, some useful info:")

join_list_txt_dict={}
join_list_txt=join_list_txt.replace("\n","")
join_list_txt=join_list_txt.replace(",","")
print(join_list_txt)
for one_char in join_list_txt:
    if ("," in one_char or " " in one_char or "." in one_char or "!" in 
    one_char or "?" in one_char or " " in one_char):
        join_list_txt=join_list_txt.replace(f"{one_char}",f"")

    if one_char in join_list_txt_dict.keys():
        join_list_txt_dict[one_char]+=1
    else:
        join_list_txt_dict[one_char]=1
print(join_list_txt_dict)

prova=["zero",",","uno"]
for i in range(len(prova)):
    if "," in prova[i]:
        #print(prova[i])
        prova[i]=prova[i].replace(prova[i],"")
        #print(asd)
    print(prova[i])
    
