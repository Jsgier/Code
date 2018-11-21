"""
Engineer: Josh Gier
Date: 11/20/18
Function: This code was written to test the remote control functionality of
an oscilloscope, specifically, the Rigol DS1054Z. It uses the telnetlib library
to send SCPI commands to the ip address defined in the Defines section, which
can be changed to suit a compatible oscilloscope. This code can also be adapted
to control other instruments over ethernet using SCPI.
"""

#-------------------------------------------------------------------------------
#----------------------------- Libraries ---------------------------------------
#-------------------------------------------------------------------------------
import telnetlib
import visa

#-------------------------------------------------------------------------------
#------------------------------- Defines ---------------------------------------
#-------------------------------------------------------------------------------
oscilloscopeIPv6 = "fe80::477:e0e0:bc52:e628%61" #change for different instrument
oscilloscopeIPv4 = "169.254.117."

#-------------------------------------------------------------------------------
#-------------------------------- Main -----------------------------------------
#-------------------------------------------------------------------------------
rm = visa.ResourceManager()
rm.list_resources()

"""
try:
    with telnetlib.Telnet(oscilloscopeIPv4, 23) as oscilloscope:
        oscilloscope.write(":MEASure:ADISplay 1\n")
        oscilloscope.write(":MEASure:ADISPlay?\n")
        print(oscilloscope.read_all())

except ConnectionRefusedError as err:
    print("Target refused connection")
"""
