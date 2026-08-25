from robot_name import Robot
import random

def main():
    # Set a seed
    seed = "Totally random."

    # Initialize RNG using the seed
    random.seed(seed)

    # Call the generator
    robot = Robot()
    name = robot.name

    # Reinitialize RNG using seed
    random.seed(seed)

    # Call the generator again
    robot.reset()
    name2 = robot.name
    
    robot2 = Robot()
    name3 = robot2.name
    
    print(name, name2, name3)
    
if __name__ == "__main__":
    main()