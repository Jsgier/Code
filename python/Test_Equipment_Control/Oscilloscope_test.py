"""
Engineer: Josh Gier
Date: 11/20/18
Function: This code was written to test the remote control functionality of
an oscilloscope, specifically, the Rigol DS1054Z. It uses the telnetlib library
to send SCPI commands to the ip address defined in the Defines section, which
can be changed to suit a compatible oscilloscope. This code can also be adapted
to control other instruments over ethernet using SCPI.

Read the RigolDS1054Z Programming Guide Here:
http://int.rigol.com/File/TechDoc/20151218/MSO1000Z&DS1000Z_ProgrammingGuide_EN.pdf

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
#-------------------------------- Main -----------------------------------------
#-------------------------------------------------------------------------------
rm = visa.ResourceManager()
try:
    oscilloscope = rm.get_instrument(oscilloscopeAddress)
except:
    print("Oscilloscope is not connected or refused connection.")
