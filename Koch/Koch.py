import adsk.core, adsk.fusion, adsk.cam, traceback, math
from .simplelogo import SimpleLogo

app = adsk.core.Application.get()
if app:
    ui = app.userInterface
    product = app.activeProduct
design = adsk.fusion.Design.cast(product)
rootComp = design.rootComponent
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane

def koch(logo, depth, size):
    if (depth == 0):
        logo.forward(size)
        return
    koch(logo, depth - 1, size / 3)
    logo.left(60)
    koch(logo, depth - 1, size / 3)
    logo.right(120)
    koch(logo, depth - 1, size / 3)
    logo.left(60)
    koch(logo, depth - 1, size / 3)

def run(context):
    try:
        s = 7
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        arcs = sketch.sketchCurves.sketchArcs
        logo = SimpleLogo()
        logo.lines = lines
        logo.arcs = arcs
        logo.x = s / 2
        logo.y = -s / 6 * math.sqrt(3)
        for i in range(0, 3):
            koch(logo, 3, s)
            logo.right(120)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
