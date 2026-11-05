import plants
import bush
import traverse

world_size = get_world_size() - 1

def task():
      ## plants.[grass,bush,carrot] are functions that will plant the respective entity
	plants.grass()
		
def next_column():
	move(East)
	task()

def main():
	while True:
		task()

		traverse.move_act(North, task)

		next_column()

		traverse.move_act(South, task)

		next_column()

		traverse.move_act(North, task)
		
		next_column()
		
		traverse.move_act(South, task)
		
		next_column()

		traverse.move_act(North, task)
		
		next_column()
		
		traverse.move_act(South, task)

		# Reset
		for i in range(world_size):
			move(West)
			if can_harvest():
				harvest()

if __name__ == "__main__":
	main()