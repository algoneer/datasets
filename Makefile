TESTARGS := ${testargs}

all: mypy test

mypy:
	mypy algoneer_datasets/

test:
	py.test algoneer_datasets ${TESTARGS}
