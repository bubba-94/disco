# STM32

## Description

This repository contains various STM32 projects (or “sketches”) as part of my learning journey.  
The goal is to document progress over time and provide a quick reference for useful concepts and implementations.

I am using the **STM32F769I-DISCOVERY**, which features a 4-inch LCD screen.  
A key focus will be incorporating the display into projects as early and as often as possible.

## Requirements

Script for installing repo dependencies incoming soon

- **I am using**: 
    - VS Code (Remote WSL)
    - Ubuntu 24.04
    - STM32F769I-DISCOVERY board
    - ST-Link for flashing the device

## Usage

Repositiory can be cloned and each application will have its own ready to run python script for compilation and flashing.

---

## Table of projects

- [Blinky](#blinky) UNDERWAY
- [Inputz](#hello-world) NOT AVIALABLE
- [flaggr](#flaggr) NOT AVAILABLE

---

## Projects

### Inputz

[Source code]()

A minimal starting point to verify the development environment and toolchain.
Should work as a sort of simple keylogger that displays a single character pressed on the connected keyboard. 
Typically includes basic initialization and simple I/O (e.g., serial or LCD).

### Blinky

[Source code](#apps/blinky/)

The classic initial embedded system project.  
Toggle a LED at a fixed interval to perform basic I/O control.

### flaggr

[Source code]()

Make use of the screen on the board and run an SDL2 application showing different flags from configuration files.