def techsupport():
    print("Welcome to the automated technical support system.")
    entry=input("Please describe your problem:\n")
    e = entry.split()

    dictionary={'crashed':'Are the drivers up to date?','blue': 'Ah, the blue screen of death. And then what happened?','hacked':'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows':'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?','spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}

    while entry !="quit":
        hasKey= False
        for  word in e:
            if word in dictionary:
                hasKey=True
                if hasKey==True:
                    print(dictionary[word])
    
                    entry=input("")
                    e=entry.split()
                    break

        if hasKey==False:
            print("Curious, tell me more.")
            entry=input("")
            e= entry.split()
            
if __name__=='__main__':
    techsupport()
    