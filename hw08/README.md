## Seun Ladipo hw08 ECE 434

##Files

1. hello.c

2. pwm.c

3. pwm4.c

3. LEDBlink.png
	
	Scope capture of the led blinking.

4. PWMGenerator.png

	Scope capture of the PWMsignal at 50MHz.


##Answers to Questions

2.6 Blinking an LED

	The fastest I could get P9_31 pin to toggle is arounf 80ns. There is a bit of jitter and it is not as stable at slower speeds. This can be observed in the LEDBlink.png file.

2. PWM Generator

	The pin toggled at aroun 50MHz is stable. The standard deviatoin is around 380kHz whis isnt that bad when the signal is toggling this fast. This can be observes in the PWMGenerator.png file.

3. Controlling PWM Frequency

	The fastest I could get this to toggle is around a pierod of 80ns. There is much more jitter in this signal. 

4. Reading an Input at Regular Intervals

	I from what I measured there is a delay of around 40 ns from an input to an output signal.

## Prof. Yoder's comments

Over all looks good.
You shouldn't have jitter when using the R30 for output.

Late: -1
Grade:  9/10
