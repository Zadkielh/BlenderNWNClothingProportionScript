import bpy
import mathutils

# Python Auto Proportion Script for NWN Clothing - Made by Zadi.

# Get currently selected objects in scene
selectedObjects = bpy.context.selected_objects
print(selectedObjects)

# Proportion Constants X, Y, Z

# Male
Proportions = {}
Proportions['m'] = {}
Proportions['m']['chest'] = {
    'o' : [1.50, 1.50, 1.30], # Half Orc
    'g' : [0.85, 0.86, 0.81], # Gnome
    'e' : [0.80, 0.80, 0.89], # Elf
    'd' : [1.08, 1.05, 0.89], # Dwarf
    'a' : [0.60, 0.70, 0.70] # Halfling
}
Proportions['m']['belt'] = {
    'o' : [1.38, 1.38, 1.15],
    'g' : [0.80, 0.81, 0.84],
    'e' : [0.84, 0.88, 0.92], # Note: Elf Male belts don't seem to match the other races belts in base game, so these numbers are closest
    'd' : [1.00, 1.10, 0.90],
    'a' : [0.72, 0.72, 0.72]
}
Proportions['m']['bicepl'] = {
    'o' : [1.45, 1.50, 1.30],
    'g' : [0.65, 0.60, 0.80],
    'e' : [0.70, 0.78, 0.88],
    'd' : [1.14, 1.20, 0.89],
    'a' : [0.70, 0.70, 0.69]
}
Proportions['m']['bicepr'] = {
    'o' : [1.45, 1.50, 1.30],
    'g' : [0.65, 0.60, 0.80],
    'e' : [0.70, 0.78, 0.88],
    'd' : [1.14, 1.20, 0.89],
    'a' : [0.70, 0.70, 0.69]
}
Proportions['m']['neck'] = {
    'o' : [1.35, 1.35, 1.40],
    'g' : [0.72, 0.81, 0.95],
    'e' : [0.79, 0.82, 0.97],
    'd' : [1.10, 1.10, 0.95],
    'a' : [0.70, 0.70, 0.75]
}
Proportions['m']['pelvis'] = {
    'o' : [1.44, 1.25, 1.15],
    'g' : [0.70, 0.77, 0.67],
    'e' : [0.84, 0.83, 0.77],
    'd' : [1.04, 1.00, 0.76],
    'a' : [0.73, 0.70, 0.65]
}
Proportions['m']['shol'] = {
    'o' : [1.50, 1.50, 1.30],
    'g' : [0.75, 0.80, 0.93],
    'e' : [0.79, 0.82, 0.97],
    'd' : [1.10, 1.20, 1.00],
    'a' : [0.80, 0.80, 0.80]
}
Proportions['m']['shor'] = {
    'o' : [1.50, 1.50, 1.30],
    'g' : [0.75, 0.80, 0.93],
    'e' : [0.79, 0.82, 0.97],
    'd' : [1.10, 1.20, 1.00],
    'a' : [0.80, 0.80, 0.80]
}
Proportions['m']['forel'] = {
    'o' : [1.45, 1.60, 1.36],
    'g' : [1.00, 1.03, 0.81],
    'e' : [0.70, 0.78, 0.88],
    'd' : [1.15, 1.30, 0.93],
    'a' : [0.70, 0.70, 0.65]
}
Proportions['m']['forer'] = {
    'o' : [1.45, 1.60, 1.36],
    'g' : [1.00, 1.03, 0.81],
    'e' : [0.70, 0.78, 0.88],
    'd' : [1.15, 1.30, 0.93],
    'a' : [0.70, 0.70, 0.65]
}
Proportions['m']['handl'] = {
    'o' : [1.40, 1.40, 1.20],
    'g' : [0.88, 0.85, 0.80],
    'e' : [0.76, 0.76, 0.80],
    'd' : [1.25, 1.25, 1.00],
    'a' : [0.80, 0.76, 0.80]
}
Proportions['m']['handr'] = {
    'o' : [1.40, 1.40, 1.20],
    'g' : [0.88, 0.85, 0.80],
    'e' : [0.76, 0.76, 0.80],
    'd' : [1.25, 1.25, 1.00],
    'a' : [0.80, 0.76, 0.80]
}
Proportions['m']['legl'] = {
    'o' : [1.30, 1.20, 1.00],
    'g' : [0.52, 0.52, 0.61],
    'e' : [0.70, 0.80, 0.90],
    'd' : [1.01, 1.10, 0.66],
    'a' : [0.70, 0.70, 0.66]
}
Proportions['m']['legr'] = {
    'o' : [1.30, 1.20, 1.00],
    'g' : [0.52, 0.52, 0.61],
    'e' : [0.70, 0.80, 0.90],
    'd' : [1.01, 1.10, 0.66],
    'a' : [0.70, 0.70, 0.66]
}
Proportions['m']['shinl'] = {
    'o' : [1.48, 1.20, 1.00],
    'g' : [0.88, 0.85, 0.61],
    'e' : [0.70, 0.83, 0.90],
    'd' : [1.10, 1.00, 0.66],
    'a' : [0.60, 0.63, 0.58]
}
Proportions['m']['shinr'] = {
    'o' : [1.48, 1.20, 1.00],
    'g' : [0.88, 0.85, 0.61],
    'e' : [0.70, 0.83, 0.90],
    'd' : [1.10, 1.00, 0.66],
    'a' : [0.60, 0.63, 0.58]
}
Proportions['m']['footl'] = {
    'o' : [1.40, 1.20, 1.00],
    'g' : [0.82, 0.70, 0.60],
    'e' : [0.70, 0.83, 0.90],
    'd' : [1.10, 0.95, 0.65],
    'a' : [0.85, 0.85, 0.90]
}
Proportions['m']['footr'] = {
    'o' : [1.40, 1.20, 1.00],
    'g' : [0.82, 0.70, 0.60],
    'e' : [0.70, 0.83, 0.90],
    'd' : [1.10, 0.95, 0.65],
    'a' : [0.85, 0.85, 0.90]
}
Proportions['m']['cloak'] = {
    'o' : [1.40, 1.20, 1.00],
    'g' : [0.82, 0.70, 0.60],
    'e' : [0.70, 0.83, 0.90],
    'd' : [1.10, 0.95, 0.65],
    'a' : [0.85, 0.85, 0.90]
}


# Female
Proportions['f'] = {}
Proportions['f']['chest'] = {
    'o' : [1.65, 1.48, 1.39], # Half Orc 1.65 1.48 1.39
    'g' : [0.83, 0.84, 0.83], # Gnome 0.83 0.84 0.84
    'e' : [0.82, 0.82, 0.90], # Elf 0.82 0.82 0.90
    'd' : [1.25, 1.20, 0.99], # Dwarf 1.25 1.20 0.99
    'a' : [0.64, 0.70, 0.70] # Halfling 0.64 0.70 0.70
}
Proportions['f']['belt'] = {
    'o' : [1.45, 1.38, 1.15],
    'g' : [0.73, 0.74, 0.84],
    'e' : [0.70, 0.78, 0.87],
    'd' : [1.30, 1.30, 0.88],
    'a' : [0.64, 0.70, 0.70]
}
Proportions['f']['bicepl'] = {
    'o' : [1.68, 1.68, 1.12],
    'g' : [0.80, 0.81, 0.84],
    'e' : [0.90, 0.90, 0.92],
    'd' : [1.30, 1.14, 0.94],
    'a' : [0.70, 0.70, 0.65]
}
Proportions['f']['neck'] = {
    'o' : [1.67, 1.42, 1.38],
    'g' : [0.85, 0.8, 0.75],
    'e' : [0.80, 0.80, 0.95],
    'd' : [1.10, 1.04, 0.98],
    'a' : [0.70, 0.70, 0.82]
}
Proportions['f']['pelvis'] = {
    'o' : [1.46, 1.43, 1.08],
    'g' : [0.79, 0.79, 0.77],
    'e' : [0.77, 0.75, 0.77],
    'd' : [1.16, 1.10, 0.74],
    'a' : [0.64, 0.72, 0.60]
}
Proportions['f']['shol'] = {
    'o' : [1.67, 1.68, 1.38],
    'g' : [0.80, 0.87, 0.93],
    'e' : [0.80, 0.85, 1.00],
    'd' : [1.25, 1.30, 1.10],
    'a' : [0.75, 0.75, 0.75]
}
Proportions['f']['shor'] = {
    'o' : [1.67, 1.68, 1.38],
    'g' : [0.80, 0.87, 0.93],
    'e' : [0.80, 0.85, 1.00],
    'd' : [1.25, 1.30, 1.10],
    'a' : [0.75, 0.75, 0.75]
}
Proportions['f']['forel'] = {
    'o' : [1.69, 1.69, 1.45],
    'g' : [1.07, 1.22, 0.84],
    'e' : [0.70, 0.78, 0.87],
    'd' : [1.31, 1.41, 1.02],
    'a' : [0.70, 0.70, 0.66]
}
Proportions['f']['forer'] = {
    'o' : [1.69, 1.69, 1.45],
    'g' : [1.07, 1.22, 0.84],
    'e' : [0.70, 0.78, 0.87],
    'd' : [1.31, 1.41, 1.02],
    'a' : [0.70, 0.70, 0.66]
}
Proportions['f']['handl'] = {
    'o' : [1.80, 1.80, 1.50],
    'g' : [1.15, 1.10, 0.97],
    'e' : [0.80, 0.80, 0.85],
    'd' : [1.44, 1.44, 1.10],
    'a' : [0.87, 0.80, 0.85]
}
Proportions['f']['handr'] = {
    'o' : [1.80, 1.80, 1.50],
    'g' : [1.15, 1.10, 0.97],
    'e' : [0.80, 0.80, 0.85],
    'd' : [1.44, 1.44, 1.10],
    'a' : [0.87, 0.80, 0.85]
}
Proportions['f']['legl'] = {
    'o' : [1.45, 1.46, 1.02],
    'g' : [0.54, 0.56, 0.64],
    'e' : [0.77, 0.74, 0.92],
    'd' : [1.10, 1.09, 0.65],
    'a' : [0.60, 0.65, 0.66]
}
Proportions['f']['legr'] = {
    'o' : [1.45, 1.46, 1.02],
    'g' : [0.54, 0.56, 0.64],
    'e' : [0.77, 0.74, 0.92],
    'd' : [1.10, 1.09, 0.65],
    'a' : [0.60, 0.65, 0.66]
}
Proportions['f']['shinl'] = {
    'o' : [1.48, 1.47, 1.02],
    'g' : [0.85, 0.89, 0.64],
    'e' : [0.77, 0.76, 0.92],
    'd' : [1.11, 1.10, 0.67],
    'a' : [0.68, 0.65, 0.57]
}
Proportions['f']['shinr'] = {
    'o' : [1.48, 1.47, 1.02],
    'g' : [0.85, 0.89, 0.64],
    'e' : [0.77, 0.76, 0.92],
    'd' : [1.11, 1.10, 0.67],
    'a' : [0.68, 0.65, 0.57]
}
Proportions['f']['footl'] = {
    'o' : [1.45, 1.43, 1.02],
    'g' : [0.88, 0.75, 0.65],
    'e' : [0.80, 0.80, 0.91],
    'd' : [1.09, 0.99, 0.66],
    'a' : [0.85, 0.85, 0.82]
}

# Robes are fun!

Proportions['f']['robe'] = {}
Proportions['f']['robe']['Arm_L'] = {
    'o' : [1.7, 1.40, 1.30],
    'g' : [1.26, 1.43, 1.30],
    'e' : [0.84, 0.81, 0.90],
    'd' : [1.28, 1.20, 0.92],
    'a' : [0.98, 1.08, 0.96]
}
Proportions['f']['robe']['Arm_R'] = {
    'o' : [1.7, 1.40, 1.30],
    'g' : [1.26, 1.43, 1.30],
    'e' : [0.84, 0.81, 0.90],
    'd' : [1.28, 1.20, 1.00],
    'a' : [0.98, 1.08, 0.96]
}
Proportions['f']['robe']['Skirt_B'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.99, 1.16, 0.95]
}
Proportions['f']['robe']['skirt_FL'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.63, 0.70, 0.61]
}
Proportions['f']['robe']['skirt_FR'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.63, 0.70, 0.61]
}
Proportions['f']['robe']['torso_g'] = {
    'o' : [1.50, 1.50, 1.30],
    'g' : [1.30, 1.24, 1.29],
    'e' : [0.81, 0.82, 0.90],
    'd' : [1.27, 1.20, 0.98],
    'a' : [0.98, 1.10, 1.08]
}
Proportions['f']['robe']['Coat_top'] = {
    'o' : [1.01, 0.95, 1.00],
    'g' : [1.00, 1.13, 1.02],
    'e' : [1.01, 0.99, 0.99],
    'd' : [0.99, 0.96, 1.02],
    'a' : [1.04, 1.00, 1.00],
}
Proportions['f']['robe']['lbicep_g'] = {
    'o' : [1.21, 1.21, 0.86],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.83, 0.83, 0.95],
    'd' : [1.05, 0.96, 0.86],
    'a' : [1.10, 1.00, 0.93]
}
Proportions['f']['robe']['rbicep_g'] = {
    'o' : [1.21, 1.21, 0.86],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.83, 0.83, 0.95],
    'd' : [1.05, 0.96, 0.86],
    'a' : [1.10, 1.00, 0.93]
}
Proportions['f']['robe']['lforearm_g'] = {
    'o' : [1.00, 1.00, 1.20],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00],
}
Proportions['f']['robe']['rforearm_g'] = {
    'o' : [1.00, 1.00, 1.20],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00],
}
Proportions['f']['robe']['coat_BL1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['f']['robe']['coat_BR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['f']['robe']['coat_BR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['f']['robe']['coat_FL1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['f']['robe']['coat_FR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['f']['robe']['coat_BL1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_BL2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_BR1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_BR2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_FL1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_FL2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_FR1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_FR2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['rootdummy'] = {
    'o' : [1.09, 1.00, 1.07],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['f']['robe']['coat_root'] = {
    'o' : [1.18, 1.18, 0.93],
    'g' : [1.21, 1.28, 0.96],
    'e' : [0.82, 0.86, 1.00],
    'd' : [1.13, 1.09, 1.00],
    'a' : [1.05, 1.34, 1.56]
}
Proportions['f']['robe']['root'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [0.645, 0.645, 0.645],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [0.64, 0.64, 0.64]
}


Proportions['m']['robe'] = {}
Proportions['m']['robe']['Arm_L'] = {
    'o' : [1.7, 1.40, 1.30],
    'g' : [1.26, 1.43, 1.30],
    'e' : [0.84, 0.81, 0.90],
    'd' : [1.28, 1.20, 1.00],
    'a' : [0.98, 1.08, 0.96]
}
Proportions['m']['robe']['Arm_R'] = {
    'o' : [1.7, 1.40, 1.30],
    'g' : [1.26, 1.43, 1.30],
    'e' : [0.84, 0.81, 0.90],
    'd' : [1.28, 1.20, 1.00],
    'a' : [0.98, 1.08, 0.96]
}
Proportions['m']['robe']['skirt_B'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.99, 1.16, 0.95]
}
Proportions['m']['robe']['skirt_FL'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.63, 0.70, 0.61]
}
Proportions['m']['robe']['skirt_FR'] = {
    'o' : [1.50, 1.50, 1.04],
    'g' : [1.30, 1.40, 0.98],
    'e' : [0.82, 0.82, 0.89],
    'd' : [1.24, 1.21, 0.66],
    'a' : [0.63, 0.70, 0.61]
}
Proportions['m']['robe']['torso_g'] = {
    'o' : [1.50, 1.50, 1.30],
    'g' : [1.30, 1.24, 1.29],
    'e' : [0.81, 0.82, 0.90],
    'd' : [1.27, 1.20, 0.98],
    'a' : [0.98, 1.10, 1.08]
}
Proportions['m']['robe']['coat_top'] = {
    'o' : [1.01, 0.95, 1.00],
    'g' : [1.00, 1.13, 1.02],
    'e' : [1.01, 0.99, 0.99],
    'd' : [0.99, 0.96, 1.02],
    'a' : [1.04, 1.00, 1.00],
}
Proportions['m']['robe']['lbicep_g'] = {
    'o' : [1.21, 1.21, 0.86],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.83, 0.83, 0.95],
    'd' : [1.05, 0.96, 0.86],
    'a' : [1.10, 1.00, 0.93]
}
Proportions['m']['robe']['rbicep_g'] = {
    'o' : [1.21, 1.21, 0.86],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.83, 0.83, 0.95],
    'd' : [1.05, 0.96, 0.86],
    'a' : [1.10, 1.00, 0.93]
}
Proportions['m']['robe']['lforearm_g'] = {
    'o' : [1.00, 1.00, 1.20],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00],
}
Proportions['m']['robe']['rforearm_g'] = {
    'o' : [1.00, 1.00, 1.20],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00],
}
Proportions['m']['robe']['coat_BL1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['m']['robe']['coat_BR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['m']['robe']['coat_BR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['m']['robe']['coat_FL1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['m']['robe']['coat_FR1'] = {
    'o' : [1.65, 1.45, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [0.82, 0.82, 0.90],
    'd' : [1.28, 1.23, 0.63],
    'a' : [0.65, 0.70, 0.61]
}
Proportions['m']['robe']['coat_BL1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_BL2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_BR1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_BR2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_FL1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_FL2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_FR1a'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_FR2'] = {
    'o' : [1.00, 1.00, 1.00],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['rootdummy'] = {
    'o' : [1.09, 1.00, 1.07],
    'g' : [1.00, 1.00, 1.00],
    'e' : [1.00, 1.00, 1.00],
    'd' : [1.00, 1.00, 1.00],
    'a' : [1.00, 1.00, 1.00]
}
Proportions['m']['robe']['coat_root'] = {
    'o' : [1.18, 1.18, 0.93],
    'g' : [1.21, 1.28, 0.96],
    'e' : [0.82, 0.86, 1.00],
    'd' : [1.13, 1.09, 1.00],
    'a' : [1.05, 1.34, 1.56]
}
Proportions['m']['robe']['root'] = {
    'o' : [0.88, 1.04, 0.98],
    'g' : [0.645, 0.645, 0.645],
    'e' : [1.00, 1.00, 1.00],
    'd' : [0.80, 0.96, 0.96],
    'a' : [0.64, 0.64, 0.64]
}

races = ['o', 'g', 'e', 'd', 'a']
    
def CreateNewScaledObjects(piece, name, slot):
    newName = list(name)
    
    for i in range(len(races)):
            newName[2] = races[i]
            newObject = piece.copy()
            bpy.context.collection.objects.link(newObject)
            newObject.name = "".join(newName)
            newScale = (Proportions[name[1:2]][slot][races[i]][0], Proportions[name[1:2]][slot][races[i]][1], Proportions[name[1:2]][slot][races[i]][2])
            newObject.scale = newScale
            
    
def GetChildren(piece, dict):
    for ob in bpy.data.objects: 
        if ob.parent == piece: 
            dict[ob] = {}
            GetChildren(ob, dict[ob])
            
def DuplicateRobe(piece, d, race, col, gender):
    for k in d:
        newRobePart = k.copy()
        
        if newRobePart.data:
            newRobePart.data = k.data.copy()
        
        if newRobePart.animation_data:
            newRobePart.animation_data.action = k.animation_data.action.copy()
            
        newRobePart.name = k.name + "_" + str(race)
        
        bpy.context.collection.objects.link(newRobePart)
        
        print(piece.name[1:2], k.name, race)
        
        newScale = (Proportions[gender]['robe'][k.name][race][0], Proportions[gender]['robe'][k.name][race][1], Proportions[gender]['robe'][k.name][race][2])
        newRobePart.scale = newScale
            
        #newRobePart.select_set(True)
        #bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        newRobePart.parent = piece       
        
        bpy.context.collection.objects.unlink(newRobePart)
        bpy.data.collections[col].objects.link(newRobePart)
         
        if not (len(d[k]) == 0):
            DuplicateRobe(newRobePart, d[k], race, col, gender)
        

def CreateNewScaledRobes(piece, name, slot):
    children = {}
    GetChildren(piece, children)
    print("New Round:")
    
    races = ['o', 'g', 'e', 'd', 'a']
    
    for i in range(len(races)):
        
        newRobe = piece.copy()
        newName = list(name)
        newName[2] = races[i]
        newRobe.name = "".join(newName)
        
        #col = bpy.data.collections.new("".join(newName))
        col = bpy.context.blend_data.collections.new(name="".join(newName))
        bpy.context.collection.children.link(col)
        bpy.data.collections[col.name].objects.link(newRobe)
        
        DuplicateRobe(newRobe, children, races[i], col.name, piece.name[1:2])
        
        newScale = (Proportions[piece.name[1:2]]['robe']['root'][races[i]][0], Proportions[piece.name[1:2]]['robe']['root'][races[i]][1], Proportions[piece.name[1:2]]['robe']['root'][races[i]][2])
        newRobe.scale = newScale
    
                    

for i in range(len(selectedObjects)):
    name = selectedObjects[i].name
    
    temp = name[5:]
    
    slot = []
    
    for n in range(len(temp)):
        if (temp[n].isnumeric()):
            break
        else:
            slot.append(temp[n])
            
    slot = "".join(slot)
    
    if (slot == "robe"):
        CreateNewScaledRobes(selectedObjects[i], name, slot)
    else:
        CreateNewScaledObjects(selectedObjects[i], name, slot)