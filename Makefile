TESTARGS := ${testargs}

all: mypy test

mypy:
	mypy algoneer_datasets/

test:
	py.test algoneer_datasets ${TESTARGS}

update:
	pip3 install pur
	pur -r requirements.txt
	pur -r requirements-test.txt
	pur -r requirements-optional.txt

release:
	python3 setup.py sdist
	twine upload dist/* -u ${TWINE_USER} -p ${TWINE_PASSWORD}
