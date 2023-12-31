def Transcription(textfile,section_divider = None): #using either File.open(src, "a") or open (src, "a")

    def __init__(self, textfile):

        self.body = ""

        if section_divider == None:

            self.sections = textfile.readlines()

        else:

            self.sections = textfile.readlines().split(section_divider)

        self.paragraphs = textfile.readlines().split('\n')

        self.sentences = textfile.readlines().split(". ")

        #clean paragraphs up later, meaning remove the entries of the list
        #that generate empty values based on your paragraph split() criteria

    def section_count(self):

        return len(self.sections)

    def paragraph_count(self):

        return len(self.paragraphs)

#prolly should check if this works so far

testtext = open('blahblah.txt', 'a')
testtext.write("Mic check. Mic check. Testing")
testtext.close()

newtext = open("blahblah.txt")
whatever = newtext.read()
print(whatever[:2])

#transcript = Transcription(testtext)

#print(transcript.section_count())

#what im gaining from all of this trial and error, is that reading files (through readlines() & read()
#does not simply just give you all of the text of a file. Am I doing something wrong when Im writing?