DOCKER_COMPOSE = docker-compose

# Targets
.PHONY: build up down restart logs clean

build:
	$(DOCKER_COMPOSE) up --build -d

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

restart: down up

logs:
	$(DOCKER_COMPOSE) logs -f web

clean:
	$(DOCKER_COMPOSE) down -v --remove-orphans
