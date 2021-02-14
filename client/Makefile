LIBS+=-pthread
BUILD_DIR := build

include test/test.mk
include trojan/trojan.mk

CFLAGS += -g
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

all: trojan test

trojan: $(OBJS)
	$(CC) $(OBJS) $(LIBS) -o $(BUILD_DIR)/$@.elf

test: $(TEST_OBJS)
	$(CC) $(TEST_OBJS) $(TEST_LIBS) -o $(BUILD_DIR)/$@.elf

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS)  -c $< -o $@

clean:
	rm -rf $(BUILD_DIR)

.PHONY: clean all test trojan
