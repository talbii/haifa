PY ?= python3 -B

parties.zip: $(wildcard ./**) tests
	rm -f parties.zip
	zip -r parties.zip . -x *.out

accepted.out: submissions/accepted/a.cpp
	g++ submissions/accepted/a.cpp -O2 -o accepted.out

.PHONY: tests
tests: testgen.toml tests.py accepted.out
	$(PY) tests.py
