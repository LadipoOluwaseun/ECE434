///////////////////////////////
// Author: Seun Ladipo
// ECE 434 HW #8
// Dr. Yoder
///////////////////////////////
#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define PRUN 1_1

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
    uint32_t gpio;

    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    gpio = P9_31;   // Select which pin to toggle.

    while (1) {
        __R30 |= gpio;      // Set the GPIO pin to 1
        __delay_cycles(1);
        __R30 &= ~gpio;     // Clearn the GPIO pin
        __delay_cycles(0);
    }
}