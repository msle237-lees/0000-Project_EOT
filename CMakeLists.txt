cmake_minimum_required(VERSION 2.8.9)
project(Project_EOT)

set(CMAKE_C_COMPILER "clang++")
set(CMAKE_CXX_COMPILER "/usr/bin/clang++")

#Bring the headers, such as Student.h into the project
include_directories(lib/create_arrs lib/sorts libs/Steps)

#Can manually add the sources using the set command as follows:
set(SOURCES src/main.cpp lib/create_arrs/create_arrs.cpp lib/sorts/sorts.cpp lib/Steps/steps.cpp)

#However, the file(GLOB...) allows for wildcard additions:
#file(GLOB SOURCES "src/*.cpp")

add_executable(Project_EOT ${SOURCES})
