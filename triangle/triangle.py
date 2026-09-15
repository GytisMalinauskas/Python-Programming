def equilateral(sides):
    """Checks if the triangle is equilateral and returns boolean value"""
    if len(sides) > 3:
        return False
    

def isosceles(sides):
    """Checks if the triangle is isoceles and returns boolean value"""
    if len(sides) > 3:
        return False
    

def scalene(sides):
    """Checks if the triangle is scalene and returns boolean value"""
    if len(sides) > 3:
        return False

def is_triangle(sides):
    """Determines if a shape is a trangle"""
    for side in sides:
        if not side > 0:
            return False
        
def main():
    test1 = [1,1,1]
    test2 = [3,4,4]
    test3 = [5,4,6]
    print(True, equilateral([test1]))
    print(False, equilateral([test2]))
    print(False, equilateral([test3]))
    # print(True, isosceles([test1]))
    # print(True, isosceles([test2]))
    # print(False, isosceles([test3]))
    # print(False, scalene([test1]))
    # print(False, scalene([test2]))
    # print(True, scalene([test3]))