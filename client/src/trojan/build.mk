# This file is part of trj: github.com/pblcc/trj
#
# It's the makefile for compiling the trojan code of the application.
#
# For running this specific process, try: make trojan.
SRCS += $(shell find ./src/trojan -maxdepth 1 -name *.c)
SRC_DIRS += ./src/trojan
