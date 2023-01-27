from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys, glob
import subprocess

file_in = open("encrypted_data.bin","rb")
private_key = RSA.import_key(open("private.pem").read())
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
skey = cipher_rsa.decrypt(enc_data)
file_in.close()
print(skey)
	
for item in glob.glob("*.txt"):

	data_in = open(item, 'rb')
	data = data_in.read()
	data_in.close()
	try:
	  iv = b64decode("xdpms+Mvqvw9tMFOZv+UQQ==")
	  ct = data
	  cipher =AES.new(skey, AES.MODE_CBC, iv)
	  pt = unpad(cipher.decrypt(ct), AES.block_size)
	  print("The message was: ", pt)
	  fo = open(item,'wb')
	  fo.write(pt)
	  fo.close()
	except ValueError:
	  print("Incorrect decryption")
	except KeyError:
	  print("Incorrect Key")	
