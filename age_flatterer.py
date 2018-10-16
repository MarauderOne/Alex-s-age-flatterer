def ageFlatterer(flattererDef):
	print("Welcome to",flattererDef)
	myName = input("What is your name?")
	myAge = int(input("What is your age?"))
	if(myName == "Alex" and myAge <= 34):
		print(myName,"is so young!")
	elif(myName == "Ozge"):
		print(myName,"is so young!")
	else:
		print(myName,"is old.")

ageFlatterer("Alex's Age Flatterer")