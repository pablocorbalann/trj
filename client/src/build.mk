# This file is part of the trj project: github.com/pblcc/trj
#
# It's the makefile created for building the trojan code and all the source 
# without any kind of problem using a system of depth.
#
# For more information check out the Makefile of the client or the README.md 
# of this trj version.
#
# Please do not touch this file unless you know what you're doing

SRCS += $(shell find ./src -maxdepth 1 -name *.c)
SRC_DIRS += ./src

LIBS += -pthread
