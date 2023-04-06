set -a
source .env
set +a

pytest -rA ./test
