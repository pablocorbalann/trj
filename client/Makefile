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
