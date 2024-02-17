# Tkinter Charts
This package will provide a Frame containing a Canvas capable to draw simple charts.

The motivation behind this little project is to be able to use an easy and light way to draw charts in Tkinter, rather than use heavy package like matplotlib (which is a great package).

## Actual State : Iteration 0 (see [historic for past iterations](https://github.com/Morgiver/tk-charts/blob/main/iterations.md))

1. ~Define function to draw line, rectangle and other object taking account the reversing of Y axis.~
2. ~Define Position class which will handle the X and Y position value~
3. ~Define an Entity base class, providing the structure of a basic entity (canvas, draw function, position, update function, etc.)~
4. ~Define Panel base class, providing the structure of a basic panel where to draw. It will act like a new context in the Canvas. A Panel will be an Entity.~
5. ~Define and build a X scale view panel, which will handle the X axis control/view~
6. ~Define and build a Y scale view panel, which will handle the Y axis control/view~
7. ~Define and build a Data view panel~
8. ~Define a Viewport class which will control and organise X scale view, Y scale view and Data view panel. This is the chart view.~
9. ~Define and build the TkCharts Frame~

## Example image
![Example Image](images/example.png)