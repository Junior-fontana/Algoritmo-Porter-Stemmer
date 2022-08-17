#Programa para eliminar as "stop words" do arquivo "tokens.txt" e aplicar o algoritmo de Porter Stemmer, isto é, eliminar as flexões
#das palavras e retornar seu radical (raiz morfológica).
import PyPDF2
import sys
import os
import nltk
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english')) #palavras que devem ser filtradas (removidas).
caracteres_Extras = set(['','[]','.',';','´','`','b',"b",'/','x'])
ps = PorterStemmer()
with open("tokens.txt","rb") as arquivo:
	linha = arquivo.read()
	linha = linha.decode("utf-8")
	linha = linha.lower()                  ##Tudo em caixa baixa. 
	palavras = linha.split()
	tokens = open("tokens_filtrados.txt","w") 
	for e in palavras:
		#print(e) 
		if not e in stop_words and not e in caracteres_Extras and len(e) > 6 and not e.startswith("b"):
			tokens.write("\n "+str(ps.stem(e)))  ##Aplica o algoritmo de Porter Stemmer.
	tokens.close()
	tokens2 = open("tokens_filtrados.txt","r") 
	for e in tokens2.readlines():
		print(e)
	tokens2.close()
