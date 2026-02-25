allVowels = "aeiou"
theList = [40,35, 10, 15, 20]
word = "I love python"

def vowelCounter(phrase:str, numOfVowels):
    phrase = phrase.lower()
    if len(phrase) == 0:
        print(numOfVowels)
        return numOfVowels
    if phrase[0] in allVowels:
        numOfVowels += 1
        phrase = phrase[1:]
      #  print(f"curr phrase {phrase} curr vowels {numOfVowels}")
        vowelCounter(phrase,numOfVowels)
    else:
        numOfVowels += 0
        phrase = phrase[1:]
      #  print(f"curr phrase {phrase} curr vowels {numOfVowels}")
        vowelCounter(phrase,numOfVowels)
        
    
    
vowelCounter(word,0)
    
print(list(map(lambda n: n*n,theList)))
