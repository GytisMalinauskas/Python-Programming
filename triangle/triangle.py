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
    

def main():
    test1 = [1,1,1]
    test2 = [3,4,4]
    test3 = [5,4,6]
    print(equilateral([test1]))
    print(equilateral([test2]))
    print(equilateral([test3]))
    print(isosceles([test1]))
    print(isosceles([test2]))
    print(isosceles([test3]))
    print(scalene([test1]))
    print(scalene([test2]))
    print(scalene([test3]))