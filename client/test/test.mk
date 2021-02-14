# Find all the C files we want to compile
TEST_SRCS += $(shell find . -path "./test/*.c")

TEST_OBJS := $(TEST_SRCS:%.c=$(BUILD_DIR)/%.o)

PKGCONFIG = $(shell which pkg-config)
CFLAGS = $(shell $(PKGCONFIG) --cflags gtk+-2.0)
TEST_LDFLAGS = $(shell $(PKGCONFIG) --libs gtk+-2.0)
