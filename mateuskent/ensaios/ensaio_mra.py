>>> import turtle
>>> c = turtle.Turtle()
>>> for t in range(20):
	y = 10/2*t**2
	c.setpos(0,y)

	
>>> c.home()
>>> c.clear()
>>> for t in range(20):
	y = t**2
	c.setpos(0,y)

	
>>> for t in range(20):
	y = -t**2
	c.setpos(0,y)

	
>>> c.home()
>>> c.left(90)
>>> c.clear()
>>> c.up()
>>> c.forward(200)
>>> c.forward(200)
>>> c.speed('fastest')
>>> for t in range(20):
	y = -3*t**2
	c.setpos(0,y)

	
>>> c.setpos(0,400)
>>> for t in range(20):
	y = -2*t**2
	c.setpos(0,y)

	
>>> c.setpos(0,400)
>>> for t in range(10):
	y = -2*t**2
	c.setpos(0,y)

	
>>> c.setpos(0,400)
>>> for t in range(15):
	y = -2*t**2
	c.setpos(0,y)

	
>>> c.position()
(0.00,-392.00)
>>> x0,y0 = c.position()
>>> x0
0
>>> y0
-392
>>> 
