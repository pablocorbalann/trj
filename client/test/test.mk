TEST_SRCS += $(shell find . -path "./test/*.c")
TEST_OBJS := $(TEST_SRCS:%.c=$(BUILD_DIR)/%.o)

PKGCONFIG = $(shell which pkg-config)
CFLAGS += $(shell $(PKGCONFIG) --cflags gtk+-2.0)
TEST_LIBS := $(shell $(PKGCONFIG) --libs gtk+-2.0)
