#Stella Ferraz
#This function is made to run in command prompt in Python 3.10.5
#This is a hanging man game.
#To play follow input prompts




from random import choice

#word list
words = ['LUMBERJACK', 'TRAMPOLINE', 'ALCHEMIST', 'DYSTOPIAN', 'HELIPORT', 'LOVESICK', 'JINX', 'UNCOPYRIGHTABLE', 'NO', 'DUCK',]


def GameHangingMan ():
	print ("Welcome to your worst decision: to play this game")
	while True:							#loop to play the game
		count_right_guesses = 0
		count_wrong_guesses = 0
		total_guesses = 0
		wrong_guess = []
		right_guess = []
		randomword = choice(words)
		word_as_list = []
		
		

		print ("Your word has", len(randomword), "letters.")

		while True:						#loop to guess in the same word
				

			guess = input("Guess a letter:")		#input to guess
			total_guesses +=1


			if guess.upper() in right_guess or guess.upper() in wrong_guess:	#check if guess is right or wrong or if has been tried
				print ('You already have tried this letter.')					#message
				total_guesses -=1								#correct number of guesses
			elif guess.upper() in randomword:
				right_guess += guess.upper()							#add guess letter to right list 
				right_guess.sort()								#sort list (this is imcomplete, I was planning to use a custom sort order comparing to the variable randomword)
				answer = print ('Correct guess:', guess.upper())				#mesage of correct guess
				print (right_guess)								#display list of right guesses
				count_right_guesses += 1							#add to right guesses count
				print ('')
				print ("You have made", total_guesses, " total guesses.")			#message of guesses count
				print ("Correct:", count_right_guesses)
				print ("Incorrect:", count_wrong_guesses)
				print ('')
				
			elif guess.upper() not in randomword:
				wrong_guess += guess								#add letter to wrong guesses list 
				wrong_guess.sort()								#sort worng guesses list
				count_wrong_guesses += 1							#add to count of wrong guesses
				print ('The letter', guess, 'is incorrect. You have guessed:', wrong_guess)	#message of incorrect guess
				print ('')
				print ("You have made", total_guesses, " total guesses.")			#message of guesses count
				print ("Correct:", count_right_guesses)
				print ("Incorrect:", count_wrong_guesses)
				print ('')
		
			if len(right_guess) < len(randomword):					#check if answer is complete
				continue
			elif len(right_guess) == len(randomword): 
				print ('You have guessed the word', randomword, 'right! It took you', total_guesses, 'guesses. GG!')	#message of guessing the word right
				break
	
		play_again = input('Do you want to play again? Answer "YES" or "NO": ')			#input to play again or not
		if play_again.upper() == 'YES':
			print ("I don't know why you keep doing this.")
			continue
		elif play_again.upper() == 'NO':
			break
		else:
			print ("I don't understand you, so I don't want to play anymore.")
			break
			

	print ('Thanks for playing, I know you have suffered.')
	print ('Game ended...')


GameHangingMan ()				#calling funtion in command prompt