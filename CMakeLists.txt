cmake_minimum_required(VERSION 3.0)
project(Project_EOT)

#Bring the headers, such as Student.h into the project
include_directories(lib/create_arrs lib/sorts libs/Steps)

#Can manually add the sources using the set command as follows:
set(SOURCES src/main.cpp lib/create_arrs/create_arrs.cpp lib/sorts/sorts.cpp lib/Steps/steps.cpp)

add_executable(Project_EOT ${SOURCES})
