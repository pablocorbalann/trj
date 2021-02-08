TARGET = client
LIBS = -pthread
CC = gcc
CFLAGS = -g
FILES = client.c trojan/trojan.c trojan/system.c

client: $(FILES)
	gcc -o $(TARGET) $(LIBS) $(FILES) $(CFLAGS)
