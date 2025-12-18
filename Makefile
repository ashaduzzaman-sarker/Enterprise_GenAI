.PHONY: install dev test lint format clean docker-up docker-down

install:
	poetry install

dev:
	poetry run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

test:
	poetry run pytest -v --cov=. --cov-report=html

lint:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run black .
	poetry run isort .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down -v