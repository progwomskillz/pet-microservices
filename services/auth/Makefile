ENV=local
-include ./secrets/$(ENV)/.env

LOCAL_SECRETS_PATH=./secrets/$(ENV)
REMOTE_SECRETS_PATH=s3://$(S3_SECRETS_BUCKET)/$(APP_NAME)/$(ENV)

ifeq ($(ENV), prod)
	DOMAIN=$(BASE_DOMAIN)
else
	DOMAIN=$(ENV).$(BASE_DOMAIN)
endif

push_secrets:
	aws s3 sync $(LOCAL_SECRETS_PATH) $(REMOTE_SECRETS_PATH)

pull_secrets:
	mkdir -p $(LOCAL_SECRETS_PATH)
	aws s3 sync $(REMOTE_SECRETS_PATH) $(LOCAL_SECRETS_PATH)

use_secrets: pull_secrets
	cp $(LOCAL_SECRETS_PATH)/.env ./.

down_containers:
	docker compose down

build_containers: use_secrets down_containers
	cp -r ./../../shared/dist .
	docker compose build
	rm -rf ./dist

up_containers: build_containers
	docker compose up -d

unit_tests: up_containers
	docker exec -it app pytest --cov-report term-missing --cov=. -s ./tests/unit

integration_tests: up_containers
	docker exec -it app pytest --cov-report term-missing --cov=. -s ./tests/integration

tests: up_containers
	docker exec -it app pytest --cov-report term-missing --cov=. -s ./tests
