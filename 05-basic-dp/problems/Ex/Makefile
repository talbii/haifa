PY ?= python3 -B

las-vegas.zip: $(wildcard ./**) tests
	rm -f las-vegas.zip
	zip -r las-vegas.zip . -x *.out -x *.docx -x *.psb -x *.png

accepted.out: submissions/accepted/a.cpp
	g++ submissions/accepted/a.cpp -O2 -o accepted.out

.PHONY: tests
tests: testgen.toml tests.py accepted.out
	$(PY) tests.py
