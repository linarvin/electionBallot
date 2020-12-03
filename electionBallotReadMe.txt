
ReadMe File:
By Arvin Lin, Lauryn Rivers

Welcome to our Electronic Ballot System. 

In this system, you as the user can input your Full name, 9 Digit ID Number, and the candidate of your choice. There would be a real-time time stamp when you start the ballot and end. This way we would know if the file is tampered with after decryption. 

This project uses both python code and a terminal with openssl commands to run. Mac users can use their terminal to run all code.

Included Files:

electionBallot.py
electionBallotReadMe.txt

Output Files:

voteCount_PlainText.txt - created after running electionBallot.py
voteCount_Encrypted.aes-128-cbc.txt - created after running encryption line (step 3)
voteCount_Decrypted.txt - created after running decryption line (step 5)

User Instructions:

1. Run the electionBallot.py file using the following command:
	python electionBallot.py 

2. Input your First Name, Last Name, 9 Digit ID Number (Does not have to be real), and the candidate of your choice. The output file will be voteCount_PlainText.txt                which holds the votes.

3. Run the line in the terminal: 

             openssl aes-128-cbc -salt -in voteCount_PlainText.txt -out voteCount_Encrypted.aes-128-cbc.txt 
            
   to encrypt the voteCount_PlainText.txt with aes-128-cbc. The code may ask for a password. The user will pick a password, but make sure to remember it                            (it will be used later).

4. Click on voteCount_Encrypted.aes-128-cbc.txt to check if the voteCount_PlainText.txt is encrypted (and it should be). 
5. Run the line in the terminal:

	openssl aes-128-cbc -d -salt -in voteCount_Encrypted.aes-128-cbc.txt -out voteCount_Decrypted.txt -k [password]

   replacing “[password]” with the password you used to encrypt the file

6. After decrypting, voteCount_PlainText.txt and voteCount_Decrypted.txt should hold the same information.

7. For extra security, the user may use a hash to confirm if a text file has been edited.
   To find the hash value use this terminal line: 

	openssl dgst -sha256 voteCount_PlainText.txt
	openssl dgst -sha256 voteCount_Decrypted.txt

   These lines should return the same hash value. If someone tampers with either text file, then the hashes will no longer match and the user will know 
   if someone has interfered with the results.

