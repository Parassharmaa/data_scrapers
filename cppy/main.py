from sys import argv  #to get filename by passing argument

"""
function 1: Reads the file, splits the data into list format,
			matches the data with countries and return the list if matched countries

function 2: Takes list of counteries with population and return 
			country with maximum population

"""

def get_counteries(l, file):
	"""
function 1: Reads the file, splits the data into list format,
			matches the data with countries and return the list if matched countries
	"""
	f = open(file, "r") #opens file in read mode
	d = f.read().split('\n') #split the file data from '\n' in to list
	d = [i.split(';') for i in d] #spliting country name and population
	a = [i for i in d if i[0][0].lower()==l.lower()] #matching country name with the letter
	return a

def get_population(c):
	p = max([int(i[1].replace(",","")) for i in c]) #getting max population from counteries list
	a = [i for i in c if int(i[1].replace(",", ""))==p] #matching max population and storing pair in list
	return a[0][0], a[0][1] #returning country and max population

if __name__ == "__main__":

	#handling exception if no file argument
	try:
		f = argv[1]
	except:
		print("No files argument was passed")
		exit()

	while(True):
		l = str(input("Please enter a letter:"))

		#cheking length and type of input
		if len(l)>1 or not l.isalpha(): 
			print("\n**Enter an alphabet only**\n") 
		#handling exception if any
		try:
			counteries = get_counteries(l, f)
			if counteries:
				print("="*30)
				print("\nCounteries with letter '%s' are:" %l)
				for i in counteries:
					print(">>%s" %i[0])
				print("\nTotal Counteries: %s \n" %len(counteries))
				print("%s has maximum population of %s\n" %get_population(counteries))
		except Exception as e:
			print(str(e))
			exit(0) #exit loop if exception found