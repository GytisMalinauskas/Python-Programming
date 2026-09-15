def equilateral(sides):
    """Checks if the triangle is equilateral and returns boolean value"""
    if not is_triangle(sides):
        return False
    
    for index in range(len(sides) - 1):
        if not sides[index] == sides[(index + 1) % 3] or not sides[index] == sides[(index + 1) % 3]:
            return False
    return True

def isosceles(sides):
    """Checks if the triangle is isoceles and returns boolean value"""
    if not is_triangle(sides):
        return False
    

def scalene(sides):
    """Checks if the triangle is scalene and returns boolean value"""
    if not is_triangle(sides):
        return False

def is_triangle(sides):
    """Determines if a shape is a trangle"""
    if not len(sides) == 3:
        return False
    for index in range(len(sides)):
        if not sides[index] > 0:
            return False
        if not sides[index] <= sides[(index + 1) % 3] + sides[(index + 2) % 3]:
            return False
    return True

def main():
    test1 = [1,1,1]
    test2 = [3,4,4]
    test3 = [5,4,6]
    test4 = [0,1,2]
    test5 = [1,1,1,1]
    test6 = [1,10,1]
    print(True, is_triangle(test1))
    print(True, is_triangle(test2))
    print(True, is_triangle(test3))
    print(False, is_triangle(test4))
    print(False, is_triangle(test5))
    print(False, is_triangle(test6))
    # print(True, equilateral(test1))
    # print(False, equilateral(test2))
    # print(False, equilateral(test3))
    # print(True, isosceles(test1))
    # print(True, isosceles(test2))
    # print(False, isosceles(test3))
    # print(False, scalene(test1))
    # print(False, scalene(test2))
    # print(True, scalene(test3))

if __name__ == "__main__":
    main()