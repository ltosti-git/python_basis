list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male","."]
#list_txt=["bene","?","si",".","tu","?","male"]

join_list_txt=" ".join(list_txt)
if (join_list_txt[-1]):
    print(join_list_txt[-1])

#join_list_txt=join_list_txt[:-1]+" "
join_list_txt=join_list_txt.capitalize()
                
for c in range(len(join_list_txt)):
    find_c=join_list_txt[c]                        
    # print(find_c)
    # print(join_list_txt[find_c])          
    if ("." in find_c or "!" in find_c or "?" in find_c):                       
        #c=c.strip()
        # find_c=join_list_txt[c]                         
        #print(find_c)
        
        join_list=join_list_txt.replace(f" {find_c} ",f"{find_c}\n")
        #join_list=join_list.capitalize()
        
                        
                        
    if ("," in find_c):
        #c=c.strip()                        
        join_list=join_list_txt.replace(f" {find_c} ",f"{find_c} ")


    
print(join_list)

