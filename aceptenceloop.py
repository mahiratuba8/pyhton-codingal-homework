#fom to filll in to get acepted to a unversity, if they have mark under 50 then they are not granted entrance and over 50 or equl to then granted entance.
name=str(input("Enter you full name: "))
score=int(input("Enter you high school scores out of 100: "))
if score<50:
    print(f"Unfortunutly {name}, you are not granted entrance.")
elif 50<=score:
    print(f"Congratualation {name}, you have been accepted!")