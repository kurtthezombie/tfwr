import carrot
import traverse

def task():
	if can_harvest():
		harvest()
		
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

		# Reset
		for i in range(3):
			move(West)

if __name__ == "__main__":
	main()