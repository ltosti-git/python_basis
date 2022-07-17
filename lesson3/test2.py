list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
#list_txt=["bene","?","si",".","tu","?","male"]
sum_words=0
for i in range(len(list_txt)):
    if not ("," in list_txt[i] or "." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i] or "stop" in list_txt[i]):    
        sum_words+=1
        #print(i)
print(sum_words)

# txt="Ciao \t\"Enkk\", prova"
# print("Ciao" or "prova" in txt)


# txt2="Silicon Valley"
# print(txt2.split("i"))

# x="-".join(["code","is","ok"])
# x="-".join(txt2)
# print(x)