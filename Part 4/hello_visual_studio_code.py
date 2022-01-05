# Write your solution here

mes=input("Editor:")
f=False

while f==False:
    if "visual studio code"==mes.lower():
        print("an excellent choice!")
        f=True
        
    elif mes.lower()=="notepad" or "word"==mes.lower():
        print("awful")
        mes=input("Editor:")
        
    else:
        print("not good")
        mes=input("Editor:")

        
    