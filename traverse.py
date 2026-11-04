def move_act(direction, act):
	for i in range(get_world_size() - 1):
		move(direction)
		act()
		