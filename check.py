#open the txt file
story = open("story.txt", 'r').read()
print story

#tokenize the file

tokenized_story = story.split(" ")

no_punctuation_tokens = [] #remove all possible punctuation symbol
for token in tokenized_story:
    
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace("'", "")
    token = token.replace(";", "") 
    token = token.replace("\n", "")
    no_punctuation_tokens.append(token)

lowercase_token = [] #convert all word in lower case   
for lowercase in no_punctuation_tokens:
	lowercase = lowercase.lower()
	lowercase_token.append(lowercase)

print (lowercase_token)	


