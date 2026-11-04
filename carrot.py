item = Entities.Carrot

# task of planting carrot
def cplant():
	charvest()
	
	if get_ground_type() !=Grounds.Soil:
		till()

	plant(item)

def charvest():
	if get_entity_type()==item:
		if can_harvest():
			harvest()
	else:
		harvest()