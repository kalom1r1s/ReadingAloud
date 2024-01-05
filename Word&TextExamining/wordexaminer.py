class WordExaminer: 
	def __init__(self, word):
		self.word = word
		self.len = len(word)

	
	def show(self): #returns the word initialized

		return self.word 

	def firstletters(self, arg = None): #you might as well write this to accept both no arguments
		
		if arg == None:
	
			return self.word[0]

		else:

			return self.word[:arg]
 

	def lastletters(self, arg = None):
		
		if arg == None:
		
			return self.word[self.len-1]

		else:
			
			length = arg - 1
			

			return self.word[self.len-arg:self.len]

#w1 = "testexaminer"
#w2 = "yabbadabbadoo"
#w3 = "singleline"

#test1 = WordExaminer(w1)
#test2 = WordExaminer(w2)
#test3 = WordExaminer(w3)



			
		