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

lowercase_tokens = [] #convert all word in lower case   
for lowercase in no_punctuation_tokens:
	lowercase = lowercase.lower()
	lowercase_tokens.append(lowercase)

print (lowercase_tokens)

#function to remove punctuation
no_punctuation_tokens = []

def remove_punctuation(token):
  
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace("'", "")
    token = token.replace(";", "") 
    token = token.replace("\n", "")
    return token.lower()
for token in tokenized_story:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token)	
    




