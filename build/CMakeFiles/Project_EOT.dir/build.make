# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.24

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.24.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.24.1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Volumes/Vault/Work/github/0001-Project_EOT

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Volumes/Vault/Work/github/0001-Project_EOT/build

# Include any dependencies generated for this target.
include CMakeFiles/Project_EOT.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Project_EOT.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Project_EOT.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Project_EOT.dir/flags.make

CMakeFiles/Project_EOT.dir/src/main.cpp.o: CMakeFiles/Project_EOT.dir/flags.make
CMakeFiles/Project_EOT.dir/src/main.cpp.o: /Volumes/Vault/Work/github/0001-Project_EOT/src/main.cpp
CMakeFiles/Project_EOT.dir/src/main.cpp.o: CMakeFiles/Project_EOT.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Project_EOT.dir/src/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Project_EOT.dir/src/main.cpp.o -MF CMakeFiles/Project_EOT.dir/src/main.cpp.o.d -o CMakeFiles/Project_EOT.dir/src/main.cpp.o -c /Volumes/Vault/Work/github/0001-Project_EOT/src/main.cpp

CMakeFiles/Project_EOT.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Project_EOT.dir/src/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Volumes/Vault/Work/github/0001-Project_EOT/src/main.cpp > CMakeFiles/Project_EOT.dir/src/main.cpp.i

CMakeFiles/Project_EOT.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Project_EOT.dir/src/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Volumes/Vault/Work/github/0001-Project_EOT/src/main.cpp -o CMakeFiles/Project_EOT.dir/src/main.cpp.s

CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o: CMakeFiles/Project_EOT.dir/flags.make
CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o: /Volumes/Vault/Work/github/0001-Project_EOT/lib/create_arrs/create_arrs.cpp
CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o: CMakeFiles/Project_EOT.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o -MF CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o.d -o CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o -c /Volumes/Vault/Work/github/0001-Project_EOT/lib/create_arrs/create_arrs.cpp

CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Volumes/Vault/Work/github/0001-Project_EOT/lib/create_arrs/create_arrs.cpp > CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.i

CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Volumes/Vault/Work/github/0001-Project_EOT/lib/create_arrs/create_arrs.cpp -o CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.s

CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o: CMakeFiles/Project_EOT.dir/flags.make
CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o: /Volumes/Vault/Work/github/0001-Project_EOT/lib/sorts/sorts.cpp
CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o: CMakeFiles/Project_EOT.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o -MF CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o.d -o CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o -c /Volumes/Vault/Work/github/0001-Project_EOT/lib/sorts/sorts.cpp

CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Volumes/Vault/Work/github/0001-Project_EOT/lib/sorts/sorts.cpp > CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.i

CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Volumes/Vault/Work/github/0001-Project_EOT/lib/sorts/sorts.cpp -o CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.s

CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o: CMakeFiles/Project_EOT.dir/flags.make
CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o: /Volumes/Vault/Work/github/0001-Project_EOT/lib/Steps/steps.cpp
CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o: CMakeFiles/Project_EOT.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o -MF CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o.d -o CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o -c /Volumes/Vault/Work/github/0001-Project_EOT/lib/Steps/steps.cpp

CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Volumes/Vault/Work/github/0001-Project_EOT/lib/Steps/steps.cpp > CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.i

CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Volumes/Vault/Work/github/0001-Project_EOT/lib/Steps/steps.cpp -o CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.s

# Object files for target Project_EOT
Project_EOT_OBJECTS = \
"CMakeFiles/Project_EOT.dir/src/main.cpp.o" \
"CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o" \
"CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o" \
"CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o"

# External object files for target Project_EOT
Project_EOT_EXTERNAL_OBJECTS =

Project_EOT: CMakeFiles/Project_EOT.dir/src/main.cpp.o
Project_EOT: CMakeFiles/Project_EOT.dir/lib/create_arrs/create_arrs.cpp.o
Project_EOT: CMakeFiles/Project_EOT.dir/lib/sorts/sorts.cpp.o
Project_EOT: CMakeFiles/Project_EOT.dir/lib/Steps/steps.cpp.o
Project_EOT: CMakeFiles/Project_EOT.dir/build.make
Project_EOT: CMakeFiles/Project_EOT.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX executable Project_EOT"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Project_EOT.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Project_EOT.dir/build: Project_EOT
.PHONY : CMakeFiles/Project_EOT.dir/build

CMakeFiles/Project_EOT.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Project_EOT.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Project_EOT.dir/clean

CMakeFiles/Project_EOT.dir/depend:
	cd /Volumes/Vault/Work/github/0001-Project_EOT/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Volumes/Vault/Work/github/0001-Project_EOT /Volumes/Vault/Work/github/0001-Project_EOT /Volumes/Vault/Work/github/0001-Project_EOT/build /Volumes/Vault/Work/github/0001-Project_EOT/build /Volumes/Vault/Work/github/0001-Project_EOT/build/CMakeFiles/Project_EOT.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Project_EOT.dir/depend

