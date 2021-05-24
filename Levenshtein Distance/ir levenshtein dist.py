import numpy as np

class Vocabulary:
    pass

    def __init__(self, name):
        self.name = name
        self.vocab_list=[]
        self.num_words = 0


    def add_word(self, word):
        if word not in self.vocab_list:
            # First entry of word into vocabulary
            self.vocab_list.append(word)
            self.num_words += 1


    def add_sentence(self, sentence):
        for word in sentence.split(' '):
            self.add_word(word)


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])


voc = Vocabulary('test')
print(voc)
corpus = ["Here is an overview of the main differences between British and American spellings:",
          "armour armoury behaviour candour clamour colour demeanour endeavour favourite flavour glamour harbour honour humour labour neighbour odour rancour rigour rumour saviour savour savoury splendour valour vapour vigour",
          "armor armory behavior candor clamor color demeanor endeavor favorite flavor glamor harbor honor humor labor neighbor odor rancor rigor rumor savior savor savory splendor valor vapor vigor",
          " amphitheatre calibre centimetre centre fibre kilometre litre louvre lustre manoeuvre meagre metre millimetre sabre sceptre sombre spectre theatre",
          " amphitheater caliber centimeter center fiber kilometer liter louver luster maneuver meager meter millimeter saber scepter somber specter theater"]
for sent in corpus:
  voc.add_sentence(sent)

print(voc.vocab_list,"\nNo of words:",voc.num_words)

seq2=input("enter the word to compare")
display=[]
for seq1 in voc.vocab_list:
    distance=levenshtein(seq1,seq2)
    if distance<=2:
        display.append(seq1)
        #print(seq1)
print(display)      
    

