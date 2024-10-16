echo [tool:pytest] > setup.cfg
echo addopts = --cov=api --cov-report=term-missing --cov-report=xml --cov-report=html >> setup.cfg