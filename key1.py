from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import time

class Voter:
  def __init__(self,voterid,name,encrypted,vote):
    self.voterid = voterid
    self.name = name
    self.encrypted=encrypted
    self.vote=vote

v=[]
def create_voter():
  print("Voter Key Generation\n");
  n=input("Enter ur VoterID : ");
  a=input("Enter ur Name : ");
  #The message to be encrypted
  message = b'Votingsystem'
  #Generating private key (RsaKey object) of key length of 1024 bits
  private_key = RSA.generate(int(n))

  #Generating the public key (RsaKey object) from the private key
  public_key = private_key.publickey()
  
  #Converting the RsaKey objects to string 
  private_pem = private_key.export_key().decode()
  public_pem = public_key.export_key().decode()
  print("Public Key :")
  print(public_pem);
  
  private='private_'+n+'.pem';
  public='public_'+n+'.pem';
  
  #Writing down the private and public keys to 'pem' files
  with open(private, 'w') as pr:
    pr.write(private_pem)
  with open(public, 'w') as pu:
    pu.write(public_pem)
    
  pu_key = RSA.import_key(open(public, 'r').read())

  #Instantiating PKCS1_OAEP object with the public key for encryption
  cipher = PKCS1_OAEP.new(key=pu_key)
  #Encrypting the message with the PKCS1_OAEP object
  cipher_text = cipher.encrypt(message)

  v.append(Voter(n,a,cipher_text,0))
  print("Private key file generated successfully\n");

opt='y'
while(opt=='y'):
  create_voter()
  opt=input("Create another voter(y/n)");
  

print("\nUpdating record....");
time.sleep(2);
print("Proceeding to Verfication...");
time.sleep(2);
message = b'Votingsystem'


    
