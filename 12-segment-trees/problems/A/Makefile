PY ?= python3 -B

accepted.out: submissions/accepted/a.cpp
	g++ submissions/accepted/a.cpp -O2 -o accepted.out

.PHONY: tests
tests: testgen.toml tests.py accepted.out
	$(PY) tests.py

tabor.zip: $(wildcard ./**) tests
	rm -f tabor.zip
	zip -r tabor.zip . -x *.out
