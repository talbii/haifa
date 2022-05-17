ARCHIVE_FILES = domjudge-problem.ini problem.yaml problem.pdf submissions output_validators data
PY = python3

.PHONY: build
build: $(wildcard ./**)
	rm -f ramon.zip
	$(PY) tests.py
	zip -r ramon.zip $(ARCHIVE_FILES)
