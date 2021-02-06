TARGET = client
LIBS = -pthread
CC = gcc
CFLAGS = -g

$(TARGET): client.c trojan/ 
	$(CC) -o $(TARGET) $(LIBS) trojan/ trojan/trojan.c client.c

#  TARGET = client
# LIBS = -pthread
# CC = gcc
# CFLAGS = -g 
#
# .PHONY: default all clean
#
# default: $(TARGET)
# all: default
#
# OBJECTS = $(patsubst %.c, %.o, $(wildcard *.c))
# HEADERS = $(wildcard *.h)
#
# %.o: %.c $(HEADERS)
# 	$(CC) $(CFLAGS) -c $< -o $@ -I trojan/
#
# .PRECIOUS: $(TARGET) $(OBJECTS)
#
# $(TARGET): $(OBJECTS)
# 	$(CC) $(OBJECTS) -Wall $(LIBS) -o $@
#
# clean:
# 	-rm -rf *.o
