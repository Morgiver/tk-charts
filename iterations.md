## Iteration 0 :
All objectives for this iteration 0 are fulfilled, the package can now be integrated in a Tkinter app and show an empty chart with its X and Y scaler. 
The chart can be resized with the Tk Window.

### Objectives
1. Define function to draw line, rectangle and other object taking account the reversing of Y axis.
2. Define Position class which will handle the X and Y position value
3. Define an Entity base class, providing the structure of a basic entity (canvas, draw function, position, update function, etc.)
4. Define Panel base class, providing the structure of a basic panel where to draw. It will act like a new context in the Canvas. A Panel will be an Entity.
5. Define and build a X scale view panel, which will handle the X axis control/view
6. Define and build a Y scale view panel, which will handle the Y axis control/view
7. Define and build a Data view panel
8. Define a Viewport class which will control and organise X scale view, Y scale view and Data view panel. This is the chart view.
9. Define and build the TkCharts Frame