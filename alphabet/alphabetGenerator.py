import re
# bildar ett alphabet från textfil med alla bokstäver i europa.
word_to_index = {}
index_to_word = {}
with open('bokstaver.txt','r') as f:
    counter = 0
    for i in f.readlines():
        stringen = re.sub(r'[0-9|.|,|:|(|)|\n|\s]','',i)
        s = list(stringen)
        for token in s:
            bokstav =token.lower()
            if word_to_index.get(bokstav) == None:
                word_to_index[bokstav] = counter
                index_to_word[counter] = bokstav
                counter += 1

# lägger till stora bokstäver
counter = len(word_to_index)
for i in range(len(word_to_index)):
    bokstav = index_to_word[i]
    stor_bokstav = bokstav.upper()
    word_to_index[stor_bokstav] = counter
    index_to_word[counter] = stor_bokstav
    counter +=1


with open('alphabet.txt','w') as wf:
    for ordet in word_to_index:
        index = word_to_index[ordet]
        index = str(index)
        line = "{} {}\n".format(index,ordet)
        wf.write(line)
    wf.write("328 '\n")
    wf.write("329 space")
