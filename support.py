

def support():
    print("Welcome to the automated technical support system.")
    entry=input("Please describe your problem:\n")
    
    dictionary={'crashed':'Are the drivers up to date?','blue': 'Ah, the blue screen of death. And then what happened?','hacked':'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows':'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?','spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}
    
    while entry != 'quit':
        if entry in dictionary:
            print(dictionary[entry])
        else:
            print("Curious, tell me more.")
        entry=input("")
        
        
if __name__=='__main__':
    support()
    
    
    
