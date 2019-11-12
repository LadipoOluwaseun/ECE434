## Seun Ladipo HW05

This project includes

1. Make Folder
	
	This folder includes three different files used in the makefile creation tutorial. These included the Makefile itself along with the path.make file and the "Hello World" app.c file.

	1. Target: app.o in target as the as an object file is the expected object file
	2. Dependency: app.c nesscary becuase file is being compiled
	3. Command: -c signals compiler complies but does not link

## Notes on installing the Kernel Source
	I was able to get the kernel 5.4 to compile on the bone although my virtual box ended up breaking after shutting down and resrearting my system. I can use windows powershell to acess the bone although I am not sure of the source of this breaking. 

## Cross-Compiling
	I followed the relevant instruction to get cross comple to work and have aquired the desired output.

## Kernel Modules
	Parts
		1. Part one was sucessfully completed by making the board print hello and goodbye.

		2. Part two was completed by having the kernel recieve and readback the string "hello"

		3. I updated the file to use P_14 and P_15 for the led and button respectively.
		Below is the sample ourput from my Beaglebone Kernel
			GPIO_TEST: Interrupt! (button state is 0) 
			GPIO_TEST: Interrupt! (button state is 1) 

## Prof. Yoder's comments

Make looks good.  Looking forward to the other parts.


Late: -1
Grade:  2/10

## Prof. Yoder's new comments
It's done!
Late: -1
Greap 9/10