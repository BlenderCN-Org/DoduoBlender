import bge, bpy

cont = bge.logic.getCurrentController()

spinRight = cont.actuators["spinRight"]
spinLeft = cont.actuators["spinLeft"]

pressJ = cont.sensors["J"]
pressH = cont.sensors["H"]

head = cont.owner
zRot = head.worldOrientation.to_euler()[2]

if pressJ.positive and zRot > -1:
    print("Presionado J")
    cont.activate(spinLeft)

cont.deactivate(spinLeft)
    
if pressH.positive and zRot < 0.44:
    print("Presionado H")
    cont.activate(spinRight)
    
cont.deactivate(spinRight)