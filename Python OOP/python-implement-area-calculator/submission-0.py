import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args: int) -> int:
        if len(args) == 1:
            circle_Area = (args[0] ** 2) * math.pi
            circle_Area_rounded = round(circle_Area, 2)
            return circle_Area_rounded  
        elif len(args) == 2:
            rec_area = args[0] * args[1]
            rec_area_rounded = round(rec_area, 2)
            return rec_area_rounded 
        else:
            print("Values entered not valid")

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
