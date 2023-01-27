
# Hybrid Encryption. 
## Encrypt and Decrypt your txt files


Jafaran Khan


[Compile Instructions]

-	Firstly ensure that there are at least three .txt files with some messages in your source directory. These would be the files which we are going to Encrypt.

To open and execute "Encryption.py" in the Linux terminal, navigate to the source directory where the file is stored using the "cd" command, and then use the command "python3 Encryption.py" to run the script.

Example:

[cd /path/to/source/directory
python3 Encryption.py]

To open and execute "Decryption.py" in the Linux terminal, use the same process as above, but replace "Encryption.py" with "Decryption.py"

Example:

[cd /path/to/source/directory
python3 Decryption.py]

-------------------------------------------------------------

## Understanding hybrid encryption where we encrypt multiple files.

-	Basically hybrid encryption revolves with the usage of both symmetric and asymmetric encryption.
-	Symmetric key revolves around encrypting data using a single secret key
-	While asymmetric encryption uses a pair of public and private keys. In our case, we will be using the RSA encryption method to provide us with the public and private keys.
-	We will be following the procedure where symmetric key is generated and used to encrypt the data. This symmetric key is then encrypted using an asymmetric encryption algorithm(RSA encryption) and the recipient's public key.
-	Finally, the recipient can use their private key to decrypt the symmetric key and then use the symmetric key to decrypt the data.

## Advantage of Hybrid Encryption

-	It combines the speed and efficiency of symmetric encryption with the security of asymmetric encryption.
-	As symmetric encryption tends to be faster than asymmetric encryption. Thus data can be encrypted faster.
-	While the smaller symmetric key can be encrypted with slower assymetric encryption.
-	Therefore, this provides us with  faster encryption and decryption of the data, while still providing a high level of security.

## Expected Outcomes

-	Firstly ensure that there are at least three .txt files with some messages in your source directory. These would be the files which we are going to Encrypt.

- We will firstly proceed to the source directory in the terminal through using the cd command.
## Encryption

- After that we will proceed to python3 Encryption.py to encrypt the Three .txt files
- After encryption, we will have two pairs of RSA public and private keys and a encrypted_data.bin which would be our encrypted symmetric key. This files will be inside our source folder.
- As we have done the encryption process ,we will have the following txt in ciphertext format.
- Next, we will proceed with the decryption process as shown below. After decrypting, we will have it in text format.

## Decryption

- Next, we will proceed with the decryption process as shown below. After decrypting, we will have it in text format.
- We can now proceed to the txt file to see the decrypted message.
- We should now have the text in a decrypted format.





