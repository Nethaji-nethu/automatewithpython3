from random import randrange

MAX_GUESSES = 10
RANDOM_NUM_LENGTH = 3


def get_random():
	random_num = ''
	for _ in range(RANDOM_NUM_LENGTH):
		random_num += str(randrange(0,10))
	return random_num

def guess(random_num):
	print('[*] Let\'s see if you can guess it.')
	guess_count = 0
	while guess_count < 10:
		guessed_input = input('GUESS {}>> '.format(guess_count+1))
		guess_count += 1
		result = ''
		if len(guessed_input) != 3 or not guessed_input.isnumeric():
			print('[*] Only provide a {} digit integer'.format(RANDOM_NUM_LENGTH))
			print('[*] You have lost a chance. Chances left = {}'.format(MAX_GUESSES - guess_count))
			continue

		for index,digit in enumerate(guessed_input):
			if guessed_input[index] == random_num[index]:
				result += ' Fermi '
			elif guessed_input[index] in random_num:
				result += ' Pico '
			else:
				result += ' Bagels '
		print('[*] Result = {}'.format(result))
		if result == ' Fermi  Fermi  Fermi ':
			print('[*] Hurray !! You won :) \\:/\\:/\\:/\\:/')
			break
	if  guess_count >= 10 or result != ' Fermi  Fermi  Fermi ':
		print('[*] OOPS !! You ran out of chances. Secret number was {}. Better luck Next time :( '.format(random_num))
		return

print(f'[*] A random number of length {RANDOM_NUM_LENGTH} is generated.')
while True:
	random_num = get_random()
	guess(random_num)
	print('\n\n' + '*'*50)
	response = input('[*] Wanna play again ?? [y/Y] :').lower()
	if response == 'y' or response == 'yes':
		continue
	else:
		break