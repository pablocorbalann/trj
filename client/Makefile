LDFLAGS=-pthread
BUILD_DIR := build

include test/test.mk
include trojan/trojan.mk

DEPS := $(OBJS:.o=.d)
CFLAGS = -g
CC = gcc
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
# Add a prefix to INC_DIRS. So moduleA would become -ImoduleA. GCC understands this -I flag
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# The final build step.
trj: $(OBJS)
	$(CC) $(OBJS) -o $(BUILD_DIR)/$@ $(LDFLAGS)

test: $(TEST_OBJS)
	$(CC) $(TEST_OBJS) -o $(BUILD_DIR)/$@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS)  -c $< -o $@

.PHONY: clean all test trj

clean:
	rm -rf $(BUILD_DIR)



# Include the .d makefiles. The - at the front suppresses the errors of missing
# Makefiles. Initially, all the .d files will be missing, and we don't want those
# errors to show up.
-include $(DEPS)
