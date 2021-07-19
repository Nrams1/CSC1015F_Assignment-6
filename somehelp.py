import random

def main():
    print('Welcome to the automated technical support system.')
    answer=input('Please describe your problem:\n')

        
    responses=["Have you tried it on a different operating system?","Did you reboot it?","What colour is it?","You should consider installing anti-virus software.","Contact Telkom.","I should get that looked at if I were you."]
 
    while True:
        choose=random.randint(0,len(responses)-1)
        print (responses[choose])
        answer=input("")
        if answer == "quit":
            break

    
if __name__=='__main__':
    main()
    
    
    
    
    