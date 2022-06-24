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

gui:
	export BROWSER=$(BROWSER) && \
	export FILTER=$(FILTER) && \
	docker-compose -f docker/hub.yaml up -d && \
	docker-compose -f docker/$(BROWSER).yaml up -d && \
	docker-compose -f docker/test.yaml up --build && \
	docker-compose -f docker/test.yaml stop && \
	docker-compose -f docker/hub.yaml stop && \
	docker-compose -f docker/$(BROWSER).yaml down && \
	docker rm -f $$(docker ps -a -q) && \
	docker rmi docker_automation:latest

api:
	export FILTER=$(FILTER) && \
	docker-compose -f docker/test.yaml up --build
	docker-compose -f docker/test.yaml down

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