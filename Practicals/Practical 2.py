file = "file.txt"

with open(file, "r") as f:
    vowels, consonants, uppercase, lowercase = 0,0,0,0
    
    v = "aeiou"
    c = "bcdfghjklmnpqrstvwxyz"
    data = f.read()
    
    for ch in data:
        if ch.isupper():
            uppercase += 1
        
        if ch.islower():
            lowercase += 1
        
        if ch.lower() in v:
            vowels += 1
          
        if ch.lower() in c:
            consonants += 1
    
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Uppercase:", uppercase)
    print("Lowercase:", lowercase)