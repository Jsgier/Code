"""
Engineer: Josh Gier
Date: 11/22/18
Function: This code was written to create new python programs, with the correct
template format.  It separates the code into blocks including library, defines,
and main, as well as timestamping at time of creation.
"""

#-------------------------------------------------------------------------------
#----------------------------- Libraries ---------------------------------------
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#------------------------------- Defines ---------------------------------------
#-------------------------------------------------------------------------------
defaultFile = "Script_" #Filename can be changed to suit desired default

#Following Section -template that will be written to new python script
defaultText = []
defaultTest.append("/"""/)

#-------------------------------------------------------------------------------
#------------------------------- Functions  ------------------------------------
#-------------------------------------------------------------------------------

#@FunctonName:
#@FunctionDescription:
#@InputParameters:
#@OutputParameters:
def


#-------------------------------------------------------------------------------
#-------------------------------- Main -----------------------------------------
#-------------------------------------------------------------------------------
fileCreationFlag = 0
i = 0
while fileCreationFlag == 0:

    try: # attempt to create new file with default name
        filename = defaultFile + str(i) + ".py"
        f = open(filename, "x")
        fileCreationFlag = 1
        f.close()
    except FileExistsError: #if file already exists, increment name suffix
        i +=1

f = open(filename, "w")
# Here is what is written to the new python script by default.
f.write("blah")
f.close()
print("New File "+filename +" Created")
