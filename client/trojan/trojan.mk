# Find all the C files we want to compile
SRCS += $(shell find . -path "./trojan/*.c")

OBJS := $(SRCS:%.c=$(BUILD_DIR)/%.o)