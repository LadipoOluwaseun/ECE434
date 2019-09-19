Seun Ladipo 
ECE 434 Embedded Linux HW2
Dr. Yoder

Shell Script
1.	The maximum voltage is around 3.348 V and the minimum voltage is 0 V
2.	The mean period is around 237.5 ms
3.	It is about 237 - 100 = 137 ms off of the expected value	
4.	The pierod is not very accurate as the beagleboard is not intended for this use along with the program being run through software providing overhead
5.	After Running Htop I can see I am using about 6 % of my CPU. There is a very high variation
6.	See Table
7.	The pierod is actually quite stable as standard deviation is 1.8 ms
8.	The standard deviation while running vi is about 10 ms
9.	This makes it a bit more shorter but not by much
10.	This also makes the pierod a but shorter
11.	The shortest pierod I could achieve was 25 ms

Python
1.	The minimum and maximum voltage is around 0 and 3.3 volts respetively
2.	The pierod is 200 ms
3.	This is about half as fast as the expected although is is faster than the shell script
4.	Python has less software overhead than the shell scrpit
5.	This is using around 2% of the CPU
6.	See Table
7.	The pierod is actually quite stable while very fast
8.	This does make the pierod a bit more unstable	
9.	There was no overhead in the original file so this did not impact the pierod
10.	N/A
11. The  shortest period I could achieve was .360 ms

C
1.	The minimum and maximum voltage is around 0 and 3.3 volts respetively
2.	The pierod is 400 micro seconds 
3.	This is much faster than 100 ms 400 times faster than the expected value
4.	C runs on a lower level and thus is much faster
5.	This is using about 10% of the CPU
6.	See Table
7.	The pierod is actually quite stable while very fast
8.	This does make the pierod a bit more unstable	
9.	Removing the unnesscary components did ot effect the pierod
10.	N/A
11.	The shortest pierod I could achieve was .400 ms

Table

Shell Scrpit
Input Speed (ms)	100		50		10		5		1		0.5	
CPU Usage %			17		26		67		81		99		100
Actual Speed (ms)	237		136		56		46		37		36

Python
Input Speed (ms)	100		50		10		5		1		0.5
CPU Usage %			2		3		3		15		24		35		
Actual Speed (ms)	200		100		21		11		.5		.47

C program
Input Speed (ms)	100		50		10		5		1		0.5
CPU Usage %			52		60		61		69		73		N/A
Actual Speed (ms)	0.49	0.38	.31		.28		.27		N/A

## Prof. Yoder's comments

Your numbers look good.

Please name the directory 'hw02'.  Name the readme 'README.md'.
Please resubmit

Grade:  5/10