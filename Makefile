build:
	docker-compose build
up:
	docker-compose up -d
log:
	docker-compose logs -f fast-api
down:
	docker-compose down
stop:
	docker-compose stop
restart:
	docker-compose restart
