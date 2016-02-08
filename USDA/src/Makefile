# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# Hydrobase
# Makefile: Contains the instructions to generate the executable for testing DataMapper


CC = gcc
CXX = g++
EXEC = data_mapper


all : $(EXEC)
# Compilation flags:
# -O3   turns on optimization
# -g    enables debugging support
# -Wall turns on all compiler warnings
CXXFLAGS = -O3 -g -std=c++11 -Wall 

# Linking flags: Link to the static and run-time libraries
LFLAGS = -lm

# Object files: List of object files needed to build the program.
OBJECTS = DataMapper.o


# Linking rule:
$(EXEC): $(OBJECTS)
	$(CXX) -c $(CXXFLAGS) main.cpp
	$(CXX) $^ $(LFLAGS) -o $@ 


# Clean-up rule:
clean:
	rm -f $(EXEC) *.o *~ \#*


