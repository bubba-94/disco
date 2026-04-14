#include "../include/blinky.h"

void delay(volatile uint32_t count) {
    while (count--) __asm("nop");
}

int main(void) {

    gpio_led_t test1 = {GPIOJ, 13};
    gpio_led_t test2 = {GPIOJ, 5};

    // Delay for clock stabilization
    (void)RCC->AHB1ENR;

    blinky_init(test1);
    blinky_init(test2);

    while (1) {
        led_on(test1);
        led_off(test2);
        delay(3000000);
        
        led_off(test1);
        led_on(test2);
        delay(3000000);
    }
}

void blinky_init(gpio_led_t led) {

    gpio_enable_clock(led.port);

    led.port->MODER &= ~(3U << (led.pin * 2));
    led.port->MODER |=  (1U << (led.pin * 2));
    
}

void led_on(gpio_led_t led) {
    led.port->BSRR = (1U << led.pin);
}

void led_off(gpio_led_t led) {
    led.port->BSRR = (1U << (led.pin + 16));
}

// Clock initialization function for GPIO ports
void gpio_enable_clock(GPIO_TypeDef *port) {
    if      (port == GPIOA) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;
    else if (port == GPIOB) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOBEN;
    else if (port == GPIOC) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOCEN;
    else if (port == GPIOD) RCC->AHB1ENR |= RCC_AHB1ENR_GPIODEN;
    else if (port == GPIOE) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOEEN;
    else if (port == GPIOF) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOFEN;
    else if (port == GPIOG) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOGEN;
    else if (port == GPIOH) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOHEN;
    else if (port == GPIOI) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOIEN;
    else if (port == GPIOJ) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOJEN;
    else if (port == GPIOK) RCC->AHB1ENR |= RCC_AHB1ENR_GPIOKEN;
    
    (void)RCC->AHB1ENR;
}