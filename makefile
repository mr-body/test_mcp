NAME=mcp

all:
	python3 servidor.py

install:
	pip3 install -r requirements.txt

requirements:
	pip3 freeze > requirements.txt

clean:
	rm -f *.pyc
	rm -rf __pycache__

fclean: clean
	rm -f requirements.txt

.PHONY: all clean