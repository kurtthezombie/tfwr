import plants
import traverse

world_size = get_world_size() - 1
directions = [North, South]

def task():
	plants.pumpkin()
		
def next_column():
	move(East)
	task()

def main():
	while True:
		task()

		for i in range(get_world_size()):
			direction = directions[i%2]
			
			traverse.traverse(direction, task)
			
			if i < world_size:
				move(East)
				task()

		# Reset
		for i in range(world_size):
			move(West)
			if can_harvest():
				harvest()

if __name__ == "__main__":
	main()