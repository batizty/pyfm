.PHONY: all test check

all: test check


test:
	echo "Unit Tests Running"
	bash dev/python_unit_test.sh

check:
	echo "Python Checker"
	bash dev/python_check_style.sh

clean:
	echo "Clean is empty now"