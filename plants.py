# plants.py

def carrot():
	if get_entity_type() == Entities.Carrot:
		if can_harvest():
			harvest()
	else:
		harvest()

	if get_ground_type() != Grounds.Soil:
		till()

	plant(Entities.Carrot)

def bush():
	if can_harvest():
		harvest()

	plant(Entities.Bush)

def grass():
	if get_entity_type() == Entities.Grass:
		if can_harvest():
			harvest()