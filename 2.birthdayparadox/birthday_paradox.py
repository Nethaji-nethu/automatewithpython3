from datetime import timedelta, datetime, date
from random import randint,randrange

def get_bdays(no_of_bdays):
	init_date = date(2023,1,1)
	bdays = []
	for _ in range(no_of_bdays):
		bday = init_date + timedelta(days=randint(0,365))
		bdays.append(bday)
	#print(' '.join([str(bday) for bday in bdays]))
	return bdays

def check_paradox(bdays):
	if len(bdays) == len(set(bdays)):
		return
	for index,bday in enumerate(bdays):
		if bday in bdays[index+1:]:
			return bday

no_bdays_wanted = int(input('enter no_of_bdays you want to generate (1-100) : '))

probability = 0
match_found = 0
for _ in range(100000):
	bdays = get_bdays(no_bdays_wanted)
	is_paradox = check_paradox(bdays)
	if _ % 10000 == 0:
		print('Completed {} iterations.'.format(_))
	if is_paradox == None:
		#print('[{}] No Bday\'s were found redundant \n'.format(_))
		pass
	else:
		#print('[{}] {} found redundant \n'.format(_,is_paradox))
		match_found += 1
print('Completed {} iterations'.format(100000))
print('Total matches found = {}'.format(match_found))
print('Probability = {}'.format(match_found/100000))