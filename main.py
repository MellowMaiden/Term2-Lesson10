#Term2-Lesson10: Making Plots Python
#Example 1:
#First we wil import the needed library
#And we will call is "p" for short
import matplotlib.pyplot as p
#Now we will create two points (0,50) and (6,250)
xvalue = ([0,6])
yvalue = ([50,250])
#Now let us plot to the graph
p.plot(xvalue,yvalue)
#Now finally show the graph to the user


#Example 2
#First let us put some time series data into a variable
values=[3,8,1,10,5,2,7,11,20,7,1,1,5,2]
#make the plot
p.plot(values,marker="o")#ADD a marker dot
#show the plot


#Example 3
v=([0,4.2,6.32,6.936])
t=([0,69,69,0])

#Add in a title and  x y label
p.title("Velocity versus Time graph.")
p.xlabel("Time /s")
p.ylabel("Velocity/ m s-1")
#Let' change the style of the line drawn
#Let's make the line , dotted , red and thicker.
p.plot(v,t,linestyle="dotted", color="red", linewidth="2")
#I would alse like to add in a grid . And make the axis clearer
p.grid()#draws the boxes
p.axhline()#draw a horizontal x axis line
p.axvline()#draw a vertical y axis line
p.show()