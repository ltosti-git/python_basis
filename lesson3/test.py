# txt="Ciao \t\"Enkk\", prova"
# print("Ciao" or "prova" in txt)


# txt2="Silicon Valley"
# print(txt2.split("i"))

# x="-".join(["code","is","ok"])
# x="-".join(txt2)
# print(x)

list_txt=[]
list_pr=["ciao","come","stai",",","tutto","bene","?","si","grazie"]
list_pr=list_pr[:-1]
print(list_pr)

while "stop" not in list_txt:
    txt=input("Please, insert a single word or \", ! ?\" characters: ")
    txt_strip=txt.strip()

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
                        join=join.replace(f" {c} ",f"{c}\n")
                        # if ("," not in c):
                        #     print(c)                    
    else:
        print("Empty!")

    
print(join)

print("\n Inserts completed! \n Now, some useful info:")
for c in join:
    if ("," not in c or "." not in c or "!" not in c or "?" not in c or " " not in c):
        total=sum(len(c))
print(total)
