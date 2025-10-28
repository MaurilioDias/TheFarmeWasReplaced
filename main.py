import Plantar

cont = 0 # Variável para controla da quantidade de Colunas

while True:
	for i in range(get_world_size()):#Laço que faz o drone percorrer cada casa
		# As condições IF controla o que será plantado em cada linha
		if cont >= 0 and cont <= 1:
			Plantar.girassol()
		
		if cont >= 2 and cont <=7:
			if get_pos_x() % 2 == 0:
				if get_pos_y()%2 == 0:
					Plantar.arvore()
				else:
					Plantar.kactus()
			else:
				if get_pos_y()%2 != 0:
					Plantar.arvore()
				else:
					Plantar.kactus()

		if cont >= 8 and cont <= 20:
			Plantar.cenoura()
		if cont >= 21 and cont <= 31:
			Plantar.capim()

		if i < 31:#Decide se o drona se move para frente ou para a esquerda
			move(North)
		else:
			move(East)
	
	cont +=1
	
	if cont > 31:
		cont = 0
