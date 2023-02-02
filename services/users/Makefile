down_containers:
	docker compose down

build_containers: down_containers
	cp -r ./../../shared/dist .
	docker compose build
	rm -rf ./dist

up_containers: build_containers
	docker compose up -d
