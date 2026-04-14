add_executable(${PROJECT_NAME}
    ${SHARED_STARTUP}
    ${SYSTEM_FILE}
    src/blinky.c
)

# Place the ELF into the build directory and create a .bin image after build
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
    SUFFIX ".elf"
)

# Include directories
target_include_directories(${PROJECT_NAME} PUBLIC
    ${SHARED_HEADER}
    ${SHARED_DRIVER}
)