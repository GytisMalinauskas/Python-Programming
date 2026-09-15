"""A module for classifying triangles by side length.

Functions:
    is_triangle(sides) -- validates that three sided form a valid triangle
    equilateral(sides) -- all three sides are equal
    isosceles(sides) -- at least two sides are equal
    scalene(sides) -- all three sides are different
"""

def equilateral(sides):
    """Checks if the triangle is equilateral and returns boolean value"""
    if not is_triangle(sides):
        return False
    
    for index in range(len(sides) - 1):
        if not sides[index] == sides[(index + 1) % 3] or not sides[index] == sides[(index + 2) % 3]:
            return False
    return True

def isosceles(sides):
    """Checks if the triangle is isoceles and returns boolean value"""
    if not is_triangle(sides):
        return False

    return not scalene(sides)

def scalene(sides):
    """Checks if the triangle is scalene and returns boolean value"""
    if not is_triangle(sides):
        return False
    for index in range(len(sides) - 1):
        if sides[index] == sides[(index + 1) % 3] or sides[index] == sides[(index + 2) % 3]:
            return False
    return True

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