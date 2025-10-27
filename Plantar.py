def arvore():
	if get_ground_type() == Grounds.Grassland:
		harvest()
		till()
		plant(Entities.Tree)
	else:
		harvest()
		plant(Entities.Tree)
		

def cenoura():
	if get_ground_type() == Grounds.Grassland:
		harvest()
		till()
		plant(Entities.Carrot)
	else:
		harvest()
		plant(Entities.Carrot)


def girassol():
	if get_ground_type() == Grounds.Grassland:
		harvest()
		till()
		plant(Entities.Sunflower)
	else:
		harvest()
		plant(Entities.Sunflower)
	if get_water() < 0.3:
			use_item(Items.Water)


def abobora():
	if get_ground_type() == Grounds.Grassland:
		harvest()
		till()
		plant(Entities.Pumpkin)
	else:
		harvest()
		plant(Entities.Pumpkin)
	if get_water() < 0.3:
		use_item(Items.Water)
	
	
def kactus():
	if get_ground_type() == Grounds.Grassland:
		harvest()
		till()
		plant(Entities.Cactus)
	else:
		harvest()
		plant(Entities.Cactus)
	use_item(Items.Water)


def capim():
	harvest()
