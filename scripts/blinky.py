#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from colorama import Fore, Style

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = "blinky"

PRINT_PREFIX = Fore.GREEN + Style.BRIGHT + f"[>>>{APP_NAME}.py<<<] " + Style.RESET_ALL

BUILD_DIR = os.path.join(ROOT, "build", APP_NAME)
OUTPUT_DIR = os.path.join(ROOT, "build", "bin", APP_NAME)

SDK_BASE = os.path.expanduser("~/moody")
CMSIS_PATH = os.path.join(SDK_BASE, "drivers", "CMSIS_6_STM32")


# Include and driver paths for CMake
TOOLCHAIN_PATH = os.path.join(SDK_BASE, "configs", "cmake", "toolchain-arm-none-eabi.cmake")
DRIVER_PATH = os.path.join(CMSIS_PATH, "Core", "Include")
HEADER_PATH = os.path.join(CMSIS_PATH, "STM32F769XX")

BUILD_TYPE = "Debug"

# Pass variables to CMake
FLAGS = [
    f"-DAPP_NAME={APP_NAME}",
    f"-DCMAKE_TOOLCHAIN_FILE={TOOLCHAIN_PATH}",
    f"-DDRIVER_PATH={DRIVER_PATH}",
    f"-DHEADER_PATH={HEADER_PATH}",
    f"-DCMAKE_BUILD_TYPE={BUILD_TYPE}",
    f"-DOUTPUT_DIR={OUTPUT_DIR}",
]

def run(cmd):
    print(f"{PRINT_PREFIX} {' '.join(cmd)}\n")
    subprocess.run(cmd, check=True)

def clean():
    print(f"Cleaning build cache in {BUILD_DIR}")
    if os.path.isdir(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR, exist_ok=True)

def print_config():
    print(PRINT_PREFIX, f"    Build type: {BUILD_TYPE}")
    print(PRINT_PREFIX, f"      App Name: {APP_NAME}")
    print(PRINT_PREFIX, f"           SDK: {SDK_BASE}")
    print(PRINT_PREFIX, f"     Toolchain: {TOOLCHAIN_PATH}")
    print(PRINT_PREFIX, f"        Driver: {DRIVER_PATH}")
    print(PRINT_PREFIX, f" Driver header: {HEADER_PATH}")
    print(PRINT_PREFIX, f"          Root: {ROOT}")
    print(PRINT_PREFIX, f"     Build dir: {BUILD_DIR}")
    print(PRINT_PREFIX, f"    Output dir: {OUTPUT_DIR}")
    print(Style.RESET_ALL)

def moody_print(cmd, ):
    print(PRINT_PREFIX, f"{cmd}", Style.RESET_ALL)

def build():
    print_config()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Configure
    run(["cmake", "-S", ROOT, "-B", BUILD_DIR] + FLAGS)

    # Build
    run(["cmake", "--build", BUILD_DIR])

def copy_and_flash():
    elf_name = f"{APP_NAME}.elf"
    output_name = f"{APP_NAME}.bin"

    built_elf = os.path.join(BUILD_DIR, elf_name)
    built_output = os.path.join(OUTPUT_DIR, output_name)

    moody_print(f"Creating an objcopy of {elf_name} as {output_name}")
    run(["arm-none-eabi-objcopy", "-O", "binary", built_elf, built_output])

    if not os.path.isfile(built_output):
        raise FileNotFoundError(moody_print(f"Output file not found: {built_output}"))
    
    moody_print(f"Flashing {output_name} to device")
    run(["st-flash", "write", built_output, "0x08000000"])

if __name__ == "__main__":
    try:
        clean()
        build()
        copy_and_flash()
    except subprocess.CalledProcessError as e:
        moody_print(f"Build failed: {e}\n")
        sys.exit(1)