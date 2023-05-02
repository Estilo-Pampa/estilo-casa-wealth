CC=g++
CFLAGS=-Wall -g

all: myprogram

myprogram: main.cpp foo.cpp bar.cpp
    $(CC) $(CFLAGS) -o $@ $^

clean:
    rm -f myprogram
  
