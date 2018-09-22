def weight_on_planets():
	weight_on_earth = float(input("What do you weigh on earth? "))
	weight_on_mars = (weight_on_earth * 0.38)
	weight_on_jupiter = (weight_on_earth * 2.34)
	print("\nOn Mars you would weigh", weight_on_mars, "pounds." "\nOn Jupiter you would weigh", weight_on_jupiter, "pounds.")   
   
   
if __name__ == '__main__':
   weight_on_planets()
