# plants.py

def pumpkin():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
	plant(Entities.Pumpkin)

def tree():
	if can_harvest():
		harvest()

	plant(Entities.Tree)

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