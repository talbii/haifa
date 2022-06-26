PY ?= python3

.PHONY: tests
tests: testgen.toml tests.py accepted.out
	$(PY) tests.py

dna-sequencing.zip: $(wildcard ./**) tests
	rm -f dna-sequencing.zip
	zip -r dna-sequencing.zip . -x *.out -x *.docx
