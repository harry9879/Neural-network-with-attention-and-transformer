letter='''dear <|NAME|>
I am happy to tell you that you are selected 
<|DATE|>
'''
a=input('Enter your name \n')
b=input('Enter your date \n')
letter= letter.replace('<|NAME|>',a)
letter= letter.replace('<|DATE|>',b)
print(letter)
