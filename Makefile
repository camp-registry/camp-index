# camp local preview
#
# The browse site and the repository tree are served from one persistent
# nginx container (docker-compose.yml) at http://localhost:8471.
#
#   make up       start/refresh the preview container
#   make dist     regenerate dist/ (site + Composer metadata) from the index
#   make down     stop the container
#   make logs     tail nginx logs
#
# Two base URLs on purpose: the browse site is viewed from your browser
# (localhost), while the tool_camp Moodle client fetches from inside its
# container (host.docker.internal). Both resolve to the same nginx.

CAMP        ?= tools/.venv/bin/camp
SITE_URL    ?= http://localhost:8471
CLIENT_URL  ?= http://host.docker.internal:8471
LISTINGS    ?=

.PHONY: up down dist logs restart

dist: ## Regenerate the served site + Composer metadata from the index
	$(CAMP) site index $(SITE_URL) dist/site $(if $(LISTINGS),--listings $(LISTINGS),)
	$(CAMP) composer index $(CLIENT_URL) dist/packages.json

up: ## Start (or recreate) the persistent preview container
	docker compose up -d
	@echo "CAMP web up at $(SITE_URL)  (repo metadata at $(SITE_URL)/packages.json)"

down: ## Stop the preview container
	docker compose down

restart: ## Restart the preview container
	docker compose restart

logs: ## Tail nginx access/error logs
	docker compose logs -f
