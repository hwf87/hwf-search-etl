# set environment variables
set -a
source .env
set +a

# run test
pytest -rA ./test --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html
