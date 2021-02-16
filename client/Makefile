# This file is part of trj: github.com/pblcc/trj
#
# It's the makefile of the client, that contains all the commands related 
# to compiling the client itself, that has been built using the C programming language.
#
# For information about how does this file works you should read this comment by 
# @mpzaborski (thanks for your amazing contribution)
#
# 		https://github.com/pblcc/trj/issues/4#issuecomment-778865518
#
# You can find more relevant information about how to use this makefile in the README.md
# file of the project.
#
# Basic commands:
# 	make all
# 	make test
# 	make trojan
#
# !!
# Please do not touch this file if you don't now what you are doing, 
# the makefile can ruin all the client...

BUILD_DIR := build

include test/test.mk
include src/build.mk
include src/trojan/build.mk

INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))
CFLAGS += $(INC_FLAGS) -MMD -MP -g
LIBS+=-pthread
OBJS := $(SRCS:%.c=$(BUILD_DIR)/%.o)

all: client test

client: $(OBJS)
	$(CC) $(OBJS) $(LIBS) -o $(BUILD_DIR)/$@.elf

test: $(TEST_OBJS)
	$(CC) $(TEST_OBJS) $(TEST_LIBS) -o $(BUILD_DIR)/$@.elf

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS)  -c $< -o $@

clean:
	rm -rf $(BUILD_DIR)

.PHONY: clean all test client
