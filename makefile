# Load .env file automatically if it exists
-include .env

day-%:
	@if ! echo "$*" | grep -Eq '^[0-9]+$$'; then \
		echo "Error: '$*' is not a number"; exit 1; \
	fi

	@echo "Creating day $* ..."

	@mkdir -p day$* tests/day$*

	@sed "s/{{day}}/$*/g" templates/day.py.tpl > day$*/day$*.py
	@sed "s/{{day}}/$*/g" templates/__init__.py.tpl > day$*/__init__.py
	@sed "s/{{day}}/$*/g" templates/test.py.tpl > tests/day$*/test_day$*.py

	@echo "Done."

fetch-%:
	@if [ -z "$(AOC_SESSION)" ]; then \
		echo "Error: AOC_SESSION not set (check your .env file)"; \
		exit 1; \
	fi
	@if ! echo "$*" | grep -Eq '^[0-9]+$$'; then \
		echo "Error: '$*' is not a number"; exit 1; \
	fi
	@echo "Fetching input for day $* ..."
	@mkdir -p day$*
	@curl --silent \
	      --cookie "session=$(AOC_SESSION)" \
	      "https://adventofcode.com/2025/day/$*/input" \
	      -o day$*/input.txt
	@echo "Saved to day$*/input.txt"

create-%:
	@$(MAKE) day-$*
	@$(MAKE) fetch-$*

.PHONY: day-% fetch-% create-%