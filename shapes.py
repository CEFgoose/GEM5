import sys
import os

#---define resource path for compiled build
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#---shapes for editor table & settings previews
CIRCLE=("static/shapes/circle.png")
SQUARE=("static/shapes/square.png")
TRIANGLE =("static/shapes/triangle.png")
PENTAGON=("static/shapes/pentagon.png")
HEXAGON =("static/shapes/hexagon.png")
HEPTAGON=("static/shapes/heptagon.png")
OCTAGON=("static/shapes/octagon.png")
NONAGON =("static/shapes/nonagon.png")
DECAGON=("static/shapes/decagon.png")

#---display shaped dictionary for easy assignment from shape name
allShapes={}
allShapes['circle']=CIRCLE
allShapes['triangle']=TRIANGLE
allShapes['square']=SQUARE
allShapes['pentagon']=PENTAGON
allShapes['hexagon']=HEXAGON
allShapes['heptagon']=HEPTAGON
allShapes['octagon']=OCTAGON
allShapes['nonagon']=NONAGON
allShapes['decagon']=DECAGON



#---sghapes for shape select widget buttons
CIRCLEBUTTON=("static/shapes/circleButton.png")
SQUAREBUTTON=("static/shapes/squareButton.png")
TRIANGLEBUTTON =("static/shapes/triangleButton.png")
PENTAGONBUTTON=("static/shapes/pentagonButton.png")
HEXAGONBUTTON =("static/shapes/hexagonButton.png")
HEPTAGONBUTTON=("static/shapes/heptagonButton.png")
OCTAGONBUTTON=("static/shapes/octagonButton.png")
NONAGONBUTTON =("static/shapes/nonagonButton.png")
DECAGONBUTTON=("static/shapes/decagonButton.png")

#---button shapes dict for easy assignment from shape name
allButtonShapes={}
allButtonShapes['circle']=CIRCLEBUTTON
allButtonShapes['triangle']=TRIANGLEBUTTON
allButtonShapes['square']=SQUAREBUTTON
allButtonShapes['pentagon']=PENTAGONBUTTON
allButtonShapes['hexagon']=HEXAGONBUTTON
allButtonShapes['heptagon']=HEPTAGONBUTTON
allButtonShapes['octagon']=OCTAGONBUTTON
allButtonShapes['nonagon']=NONAGONBUTTON
allButtonShapes['decagon']=DECAGONBUTTON

#---resource paths for images for compiled build

# CIRCLE = resource_path('circle.png')
# SQUARE = resource_path('square.png')
# TRIANGLE = resource_path('triangle.png')
# PENTAGON = resource_path('pentagon.png')
# HEXAGON = resource_path('hexagon.png')
# HEPTAGON = resource_path('heptagon.png')
# OCTAGON = resource_path('octagon.png')
# NONAGON = resource_path('nonagon.png')
# DECAGON = resource_path('decagon.png')
# KAARTICON = resource_path('Kaart.png')
# GEMICON = resource_path('GEM3.png')