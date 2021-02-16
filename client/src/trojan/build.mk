# This file is part of trj: github.com/pblcc/trj
#
# It's the makefile for compiling the trojan code of the application, using the 
# command:
# 		make client
#
# For more information you should check the Makefile of the client or the README.md
# file of this version of trj.
#
# Please do not touch this file unless you know what you're doing!

SRCS += $(shell find ./src/trojan -maxdepth 1 -name *.c)
SRC_DIRS += ./src/trojan
