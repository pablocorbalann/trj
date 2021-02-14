SRCS += $(shell find . -path "./trojan/*.c")
OBJS := $(SRCS:%.c=$(BUILD_DIR)/%.o)
