#ifndef BLINKY_H
#define BLINKY_H

#include "stm32f769xx.h"   // CMSIS core header

typedef struct {
    GPIO_TypeDef *port;
    volatile uint8_t pin;
}gpio_led_t;

// Function prototypes
void blinky_init(gpio_led_t led);
void led_toggle(gpio_led_t led);
void led_on(gpio_led_t led);
void led_off(gpio_led_t led);   

void gpio_enable_clock(GPIO_TypeDef *port);

void delay(volatile uint32_t count);



#endif // BLINKY_H