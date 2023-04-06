# set environment variables
set -a
source .env
set +a

# run test
pytest -rA ./test
