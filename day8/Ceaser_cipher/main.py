import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc_text=[]
dcy_text=[]


def encrypt(message,shift):
  ind = 0
  for i in range(len(message)):
    ind = (alphabet.index(message[i]))
    enc_text.append(alphabet[(ind+shift)%26])
    ind = 0
  encr = ''.join(enc_text)
  print(f"Here is the encoded result : {encr} ")
  return

def decrypt(shift):
  ind = 0
  for i in range(len(enc_text)):
    ind = (alphabet.index(enc_text[i]))
    dcy_text.append(alphabet[(ind-shift)%26])
    ind = 0
  dcr = ''.join(dcy_text)
  print(f"Here is the encoded result : {dcr} ")
  return
   

cont ='yes'
print(art.logo)
while cont == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    encrypt(text,shift)
  elif direction == "decode" :
    decrypt(shift)
  else:
    print("\n Invalid input !!")
  
  cont=input("\nType 'yes' if you want ot go again .Otherwise type 'no' \n").lower()
  if cont == 'no':
    print("Thanks for using Ceaser Cipher..\nbYe !!")
