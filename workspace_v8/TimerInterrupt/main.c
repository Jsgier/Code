#include "msp.h"


/**
 * @ProjectName: TimerInterrupt
 * @FileName: Main.c
 * @FileDescription: This is a small program used to configure and test
 * timer interrupts in the msp432p401r microcontroller. TimerA is set and
 * used to drive an interrupt, which should toggle an LED.  Likewise, TimerB
 * will drive another LED, to explore different LED frequencies.
 * @Engineer: Josh Gierd
 * @Start Date" 12/15/18
 *
 * main.c
 */
void main(void)
{
    //Setup
	WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;		     // stop watchdog timer

	//enable Timer A interrupt, set to count up, use SMCLK, and prescale by 8
	TIMER_A0->CTL = TIMER_A_CTL_IE | TIMER_A_CTL_MC_1 | TIMER_A_CTL_TASSEL_2 \
	        | TIMER_A_CTL_ID_3;




	while(1)                                             // infinite loop
}
