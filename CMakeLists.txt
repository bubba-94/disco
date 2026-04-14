cmake_minimum_required(VERSION 3.13)
if(NOT DEFINED APP_NAME)
set(APP_NAME blinky)
endif()

project(${APP_NAME} C CXX ASM)

set(SHARED_LINKER "${CMAKE_SOURCE_DIR}/linker/stm32f769.ld")
set(SHARED_STARTUP "${CMAKE_SOURCE_DIR}/startup/startup_stm32f769xx.s")
set(DRIVER_FILE "${DRIVER_PATH}/core_cm7.h")
set(SYSTEM_FILE "${HEADER_PATH}/system_stm32f7xx.c")


set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} \
-T${SHARED_LINKER} \
-Wl,-Map=${CMAKE_BINARY_DIR}/${APP_NAME}.map \
-Wl,--gc-sections \
-lc -lm -lnosys -lgcc")

add_subdirectory(apps/${APP_NAME})