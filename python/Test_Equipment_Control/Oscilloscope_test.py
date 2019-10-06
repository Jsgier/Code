"""
Engineer: Josh Gier
Date: 11/20/18
Function: This code was written to test the remote control functionality of
an oscilloscope, specifically, the Rigol DS1054Z. It uses the PyVisa library
to send SCPI commands to the ip address defined in the Defines section, which
can be changed to suit a compatible oscilloscope. This code can also be adapted
to control other instruments over ethernet using SCPI.
Resources:
RigolDS1054Z Programming Guide-
http://int.rigol.com/File/TechDoc/20151218/MSO1000Z&DS1000Z_ProgrammingGuide_EN.pdf
This is how a SCIPI command looks in PyVisa-
oscilloscope.query('Command')
"""

#-------------------------------------------------------------------------------
#----------------------------- Libraries ---------------------------------------
#-------------------------------------------------------------------------------
import visa

#-------------------------------------------------------------------------------
#------------------------------- Defines ---------------------------------------
#-------------------------------------------------------------------------------
oscilloscopeAddress = "TCPIP0::169.254.117.76::INSTR"

#-------------------------------------------------------------------------------
#------------------------------- Functions  ------------------------------------
#-------------------------------------------------------------------------------

#@FunctionName: oscope_change_time
#@InputParameters: newTime[ms]{0.000005 to 50000}
#@OutputParameters: none
#@FunctionDescription: Function Checks to see if oscilloscope was successfully
#attached, and if so, changes the time / div to that set in variable newTime,
#expressed in milliseconds.
def oscope_change_time(newTime = 100):
    print(oscilloscope.query('TIMebase:MODE?')) #Display current mode.


#-------------------------------------------------------------------------------
#-------------------------------- Main -----------------------------------------
#-------------------------------------------------------------------------------
rm = visa.ResourceManager()
try:
    oscilloscope = rm.get_instrument(oscilloscopeAddress)
except:
    print("Oscilloscope is not connected or refused connection.")
