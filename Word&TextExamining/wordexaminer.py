def WordToExamine(word): 
	def __init__():
		this.word = word

	
	def show(): #returns the word initialized

		return this.word 

	def firstletters(arg = None): #you might as well write this to accept both no arguments
		
		if arg == None:
	
			return this.word[0]

		else:
			numb = arg-1

			return this.word[numb:]
 

	def lastletters(arg = None):
		
		if arg == None:

			length = len(this.word)-1
		
			return this.word[length]

		else:
			
			length = arg - 1
			

			return this.word[:length]






			
		