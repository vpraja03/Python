class Triangle:
    def triangle():
        # Area of Triangle
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        area = (height * breadth) / 2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", area)

        # Perimeter of Triangle
        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth = float(input("Breadth: "))
        perimeter = height1 + height2 + breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", perimeter)