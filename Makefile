env:
	python -m venv .venv

install:
	pip install -r requirements.txt

check:
	flake8 main/ tests/

tag_api:
	behave -k -t $(T) ./tests/api

tag_gui:
	behave -k -t $(T) ./tests/gui

wip:
	behave -w -k

allure-report:
	behave -f allure -o reports ./features

html-report:
	behave -f html -o report/reports.html @rerun_failing.features

rerun:
	behave @rerun_failing.features

allure:
	allure serve reports