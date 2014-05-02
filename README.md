WPyStat
=======

Useful , simple stat functions.

## Functions
- **`simpleLinearRegressionForXY(x, y)`**   
Returns an actual formula for simple linear regression. Prints the formula and the correlation of the data (r value)     

SAMPLE USE
=================================
1. Linear regression
```python
        import WStat as stat 
        
        #dummy data
        xVals = [1, 2, 3, 4, 5, 6, 7, 8]
        yVals = [3, 5, 4, 6, 8, 7, 9, 11]
        
        #create function
        function = stat.simpleLinearRegressionForXY(xVals, yVals)
        
        #predict the y value of x = 1.2
        print(function(1.2))
```  
