from prettytable import PrettyTable

print("____________________________________________\n")
print("compito 1\n___________________\n")

## input 
word_list=[]
comma=","
stop_marks=[".","!","?"]
table=PrettyTable()
table.field_names = ["Stats description", "No."]

## acquiring words
while "stop" not in word_list:
    word=input("Please, insert a single word or \", . ! ?\" characters: ")
    word=word.strip()
    #memo: implements checks and controls for admitting only following punctuation ', . ! ?' and [a-z][A-Z] text
    if word!="":
        if word.find(" ")!=-1:
            print(f"error! space detected in {word}. Remind: insert just ONE word")
        else:
            word_list.append(word)
            ## after appending to list, adding the list with capitol letters after stop marks and removing stop word
            if "stop" in word_list[-1] and "stop" not in word_list[0]:
                word_list[0]=word_list[0].capitalize()
                
                for i in range(len(word_list)):
                    if (word_list[i] in stop_marks):                        
                        if word_list[i+1]!="stop":
                            word_list[i+1]=word_list[i+1].capitalize()
                        else:
                            word_list[:i-1]

                word_list_joint=" ".join(word_list)
                index_stop=word_list_joint.find("stop")
                word_list_joint=word_list_joint[:index_stop-1]+" "       

                #loop for paragraph after punctuation
                for c in word_list_joint:
                    
                    if (c in stop_marks):                           
                        c=c.strip()      
                        word_list_joint=word_list_joint.replace(f" {c} ",f"{c}\n")
                                               
                    if (c in comma):
                        c=c.strip()                        
                        word_list_joint=word_list_joint.replace(f" {c} ",f"{c} ")                 
                               
    else:
        print("Empty!")
    
print(f"\nInserts completed!\nYou typed:\n{word_list_joint}")

print("And now, some useful info:")

sum_words=0
for i in range(len(word_list)):
    if not (word_list[i] in stop_marks or word_list[i] in comma):    
        sum_words+=1
        print(word_list)

word_list_joint_dict={}
punctuation_dict={}

word_list_joint=word_list_joint.replace("\n","").replace(" ","")

for c in word_list_joint:
    c=c.lower()    
    if not (word_list[i] in stop_marks or word_list[i] in comma):    

        if c in word_list_joint_dict.keys():
            word_list_joint_dict[c]+=1
        else:
            word_list_joint_dict[c]=1
    else:
        if c in punctuation_dict.keys():
            punctuation_dict[c]+=1
        else:
            punctuation_dict[c]=1

max=0
min=0
pref_char=""
min_char=""

for word,word_count in word_list_joint_dict.items():
    if word_count > max:
        max=word_count
        pref_char=word
    else:
        min=word_count
        min_char=word

# print(f"the preferred character is: {pref_char} with {max} occurrences")
# print(f"the less used character is: {min_char} with {min} occurrences")
# print(f"the total number of typed words is: {sum_words}")

table.add_row(["The total number of words given",sum_words])
table.add_row([f"The most frequent {max} character/s",pref_char])
table.add_row([f"The least frequent {min} character/s",min_char])

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

# print(f"the preferred punctuation sign is: {pref_punct} with {max} occurrences")
# print(f"the less used punctuation sign is: {min_punct} with {min} occurrences")
# print(f"the total number of typed punctuation signs is: {tot_punct}")
# print(f"the total number of phrases is: {phrases}")

# table.add_row([f"the preferred marks {max}",pref_punct])
# table.add_row([f"The least marks {min}",min_punct])
table.add_row(["the total number of typed marks",tot_punct])
table.add_row(["the total number of phrases is",phrases])

print(table)