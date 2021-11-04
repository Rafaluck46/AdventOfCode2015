
cartesian_x = 0
cartesian_y = 0

class SantaDirection:
    x: str
    y: str
    index: int

    def __init__(self, x: str, y:str, index: int):
        self.x = x
        self.y = y
        self.index = index

houses_index: list[SantaDirection] = []
houses_index.append(SantaDirection(0,0,0))

def check_santa_position() -> None:  
    global cartesian_x
    global cartesian_y
    global houses_index

    santa_direction = SantaDirection(cartesian_x, cartesian_y, 0)

    house_already_visited = list(filter(lambda l: l.x == santa_direction.x and l.y == santa_direction.y, houses_index)) 
   
    if(len(house_already_visited) == 0):
        houses_index.append(santa_direction)

def move_santa(direction: str) -> None:
    
    global cartesian_x
    global cartesian_y

    if direction == ">":
        cartesian_x += 1
    elif direction == "<":
        cartesian_x += -1
    elif direction == "^":
        cartesian_y += 1
    elif direction == "v": 
        cartesian_y += -1

def open_santa_file() -> None: 
    with open("/home/rafaluck46/Fun/AdventOfCode/day3/input_santa.txt")  as f: 
        for line in f:
            for index in line: 
                move_santa(index)
                check_santa_position()

if __name__ == '__main__':
    open_santa_file()   
    print(len(houses_index))

