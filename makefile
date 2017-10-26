all: main.cpp
	g++ -Wall -o Gene-run Gene-run.cpp
clean:
	rm -f Gene-run