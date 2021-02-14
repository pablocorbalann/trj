# Find all the C files we want to compile
TEST_SRCS += $(shell find . -path "./test/*.c")

TEST_OBJS := $(TEST_SRCS:%.c=$(BUILD_DIR)/%.o)