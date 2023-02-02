down_containers:
	docker compose down

build_containers: down_containers
	docker compose build

up_containers: build_containers
	docker compose up -d

setup_tests: up_containers
	docker exec -it shared pip install -r tests_requirements.txt --no-cache-dir

unit_tests: setup_tests
	docker exec -it shared pytest -s --cov-report term-missing --cov=. ./tests/unit/

integration_tests: setup_tests
	docker exec -it shared pytest -s --cov-report term-missing --cov=. ./tests/integration/

tests: setup_tests
	docker exec -it shared pytest -s --cov-report term-missing --cov=. ./tests

build: up_containers
	docker exec -it shared python setup.py
