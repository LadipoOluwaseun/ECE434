///////////////////////////////
// Author: Seun Ladipo
// ECE 434 HW #8
// Dr. Yoder
///////////////////////////////
#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

#define GPIO1 0x4804C000
#define GPIO3 0x481AE000

#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define USR0 (1<<21)
#define USR1 (1<<22)
#define USR2 (1<<23)
#define USR3 (1<<24)
#define p9_37 (1<<19)
unsigned int volatile * const GPIO1_CLEAR = (unsigned int *) (GPIO1 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO1_SET   = (unsigned int *) (GPIO1 + GPIO_SETDATAOUT);

//GPIO 3
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO1_SET   = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int R30;
volatile register unsigned int R31;

void main(void) {
    int i;

    / Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    for(i=0; i<5; i++) {
        *GPIO3_SET = p9_37;      // The the USR3 LED on
        delay_cycles(100000000);
            //500000000/5);    // Wait 1/2 second

        *GPIO1_CLEAR = p9_37;
         delay_cycles(100000000);
             //500000000/5);
    }
    __halt();
}