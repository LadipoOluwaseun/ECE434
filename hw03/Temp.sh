#!/bin/bash
config-pin P9_24 i2c
config-pin P9_26 i2c

# Author: Seun Ladipo
# ECE 434 HW #3
# Dr. Yoder

# takes the average of two temp sensors on the i2c bus
while [ "1" = "1" ]; do
		#temp sensor 1 on bus 2
        TEMP=`i2cget -y 2 0x48`
        TEMPF=$(((($TEMP *9)/5)+32))

        #temp sensor 2 on bus 2 
        TEMP2=`i2cget -y 2 0x49`
        TEMPF2=$(((($TEMP2 *9)/5)+32)) 
        
        #temp average for 1 and 2
        TEMPAVG=$((($TEMPF +$TEMPF2)/2))
        echo -ne "${TEMPAVG}"
        
        #sleep for a second
        sleep 1.0
        echo -ne "\\r"
        
done