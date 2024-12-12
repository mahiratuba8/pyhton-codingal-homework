class ID:
    def __init__(self, name, ethnicity,living, career):
        self.name=name
        self.ethnicity=ethnicity
        self.living=living
        self.career=career


Savanah=ID("Savanah","Chineese","New York","Plastic surgeon")
print("Your friends name is",Savanah.name,"she is ", Savanah.ethnicity, "she lives in",Savanah.living, "and wroks as a ",Savanah.career )
Ben=ID("Ben","German","Germany", "lawyer")
print("Your friends name is",Ben.name,"she is ", Ben.ethnicity)

    