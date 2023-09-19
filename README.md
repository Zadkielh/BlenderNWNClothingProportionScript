# BlenderNWNClothingProportionScript
A Proportion script for Neverwinter Nights, quickly adjusting a human clothing piece to all the different races and phenotypes
A blender alternative to NWNArmory.

## **Important!**
1. Robes and Cloaks are mostly experimental, expect manual adjustments.
2. All models have to follow base game naming conventions.
3. ONLY Human sized models will give the correct output as base models. This means using a dwarf chest as the base will not generate human models, nor will it give correct proportions for the rest of the races.

4. To get all 24 variants, you need female and male variants, as well as their respective pheno0 and pheno2 variants.
I.E pmh0+pfh0+pmh2+pfh2
This is because base game has differing female and male pieces under the same type. If you don't want specific female/male/pheno0/pheno2 models, then just scale your base model to fit female/male/pheno0/pheno2 and then run the script.

## ANIMATIONS:
To get animations on your robes, apply the animation set to the base model first, the animation data will be copied over to the variants.

## How to use (NON ROBES):
1. Load the script into the text editor in blender, or use the blend file, which has it pre-loaded.
2. Take your chosen mesh/meshes and select it/them, and run the script.
3. Double Check the outputted meshes, sizing might not be 100% accurate.
4. Adjust manually as needed, export.

## How to use (ROBES):
1. Load the script into the text editor in blender, or use the blend file, which has it pre-loaded.
2. Import your robe, and select the parent object (top-most in the hierarchy). Run script on the root object. (If you want to do multiple, select only the root) If you are using a custom model, you might not have the root parent object, in which case, copy one from a base robe model and set it as the root parent.
4. Double check output meshes, sizing is experimental and is not 100% accurate. Some races will need slight location transformation to be 1:1 aswell.
5. Adjust as needed, export.
