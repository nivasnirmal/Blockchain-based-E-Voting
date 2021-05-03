from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
from key1 import v,message
import time
#from blockchain_1 import blockchain
valid=1;
f=1;
value=1;
ver=0;
val=0;
def vote_casting(val):
    print("\nBallot");
    print("\nCandidates:\n1-ADMK\n2-DMK\n3-BJP")
    v[val].vote=input("Choose your Candidate(1-3) : ");
    print(v[val].voterid)
    print(v[val].name)
    print(v[val].vote)

def verification():
    print("\n\nVerification\n");
    c=int(0);
    global valid
    global f
    global value
    global ver
    global val
    f=1;
    valid=1
    ver=0
    while(valid):
        voterid=input("Enter ur Voter ID : ");
        c=int(0);
        for obj in v:
            if(obj.voterid==voterid):
                valid=0
                val=int(c);
            c+=1
        if(int(v[val].vote)>0):
            print("Vote already passed!!\n");
            f=0
            
    if(f):
        try:
            pk=input("Enter the private key file name : ");
            
            #Importing keys from files, converting it into the RsaKey object   
            pr_key = RSA.import_key(open(pk, 'r').read())
    
            #Instantiating PKCS1_OAEP object with the private key for decryption
            decrypt = PKCS1_OAEP.new(key=pr_key)

            print("Verifying key.....\n");
            time.sleep(2);
                
            #Decrypting the message with the PKCS1_OAEP object
            decrypted_message = decrypt.decrypt(v[val].encrypted)
            if(message==decrypted_message):
                value=0;
        except:
            ver=1;

while(value):
    verification()
    if(value==0):
        print("Key Validated")
        print("Procceding to Vote....");
        time.sleep(2);
        vote_casting(val)
        opt=input("Another person to Vote(y/n)")
        if(opt=='y'): value=1;
        else: value=0;
    elif(ver):
        print("\nWrong Key!!! Try Again!!\n")
    elif(f==0):
        opt=input("Another person to Vote(y/n)")
        if(opt=='y'): value=1;
        else: value=0;
        
#print(v[0].vote+'\n'+v[1].vote)

val=0


