SRCS += $(shell find ./src -maxdepth 1 -name *.c)
SRC_DIRS += ./src

LIBS+=-pthread
