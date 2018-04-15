MYSQL_DRIVER?=mysql-connector-python-2.1.7
CONFIG_FILE?=${PWD}/etc/config.ini
LOGS_FILE?=${PWD}/logs/{{ cookiecutter.docker_image }}.log

IMAGE?={{ cookiecutter.docker_image }}
CONTAINER?={{ cookiecutter.docker_container }}

.PHONY: help
help:
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo "    clean-logs"
	@echo "        Remove logs."
	@echo "    clean"
	@echo "        Remove all artifacts."
	@echo "    pretty"
	@echo "        Pretty code."
	@echo "    requirements"
	@echo "        Find and set dependencies version."
	@echo "    wheels"
	@echo "        Cache wheel dependencies."
	@echo "    install"
	@echo "        Install project."
	@echo "    develop"
	@echo "        Install project in develop mode."
	@echo "    uninstall"
	@echo "        Uninstall dependencies."
	@echo "    run"
	@echo "        Run project."
	@echo "    test"
	@echo "        Install project in develop mode and run tests."
	@echo "    package"
	@echo "        Package for distribute."
	@echo "    feature"
	@echo "        Create new feature."
	@echo "    hotfix"
	@echo "        Create new hotfix."
	@echo "    release"
	@echo "        Create new version."
	@echo "    docker-image"
	@echo "        Create docker image."
	@echo "    docker-run"
	@echo "        Remove docker container and create."
	@echo "    docker-logs"
	@echo "        Show docker logs."
	@echo "    docker"
	@echo "        Create docker image and remove and create docker container."

.PHONY: clean-pyc
clean-pyc:
	@find . -name '*.pyc' -exec rm -rf {} +
	@find . -name '__pycache__' -exec rm -rf {} +

.PHONY: clean-build
clean-build:
	@find . -name '.cache' -exec rm -rf {} +
	@find . -name 'dist' -exec rm -rf {} +
	@find . -name 'build' -exec rm -rf {} +
	@find . -name '.isort.cfg' -exec rm -rf {} +
	@find . -name '.coverage' -exec rm -rf {} +
	@find . -name '.eggs' -exec rm -rf {} +
	@find . -name '*.egg-info' -exec rm -rf {} +

.PHONY: clean-logs
clean-logs:
	@find . -name '*.log' -exec rm -rf {} +
	@find . -name '*.log.*' -exec rm -rf {} +

.PHONY: clean
clean: clean-build clean-pyc clean-logs

.PHONY: pretty
pretty:
	@pip install isort > /dev/null
	@echo "[settings]\nnot_skip = __init__.py" > .isort.cfg
	@isort -sl -rc .
	@rm -rf .isort.cfg

.PHONY: requirements
requirements:
	@pip install pip-tools > /dev/null
	@pip-compile requirements.in > /dev/null
	@pip-compile test-requirements.in > /dev/null

.PHONY: wheels
wheels:
	@pip wheel --no-cache-dir -w wheels -r requirements.txt -r test-requirements.txt > /dev/null

.PHONY: install-mysql
install-mysql:
	@wget https://dev.mysql.com/get/Downloads/Connector-Python/${MYSQL_DRIVER}.tar.gz
	tar xzf $(MYSQL_DRIVER).tar.gz
	cd $(MYSQL_DRIVER) && python setup.py install && cd ..
	rm -rf $(MYSQL_DRIVER)

.PHONY: install
install: clean install-mysql
	@pip install --no-cache-dir --use-wheel --no-index --find-links=wheels . > /dev/null

.PHONY: develop
develop: clean install-mysql
	@pip install --no-cache-dir --use-wheel --no-index --find-links=wheels -r test-requirements.txt -e . > /dev/null

.PHONY: uninstall
uninstall:
	@pip uninstall -y -r requirements.txt -r test-requirements.txt > /dev/null

.PHONY: run
run:
	@run -c $(CONFIG_FILE) -l $(LOGS_FILE)

test: develop
	@pytest -vv --flake8 --cov="spsr"

.PHONY: package
package: clean
	@pip wheel -w ./dist --no-cache-dir --use-wheel --no-index --find-links=wheels . > /dev/null

.PHONY: feature
feature:
	@echo "### Save state..."; git stash > /dev/null
	@echo "### Fetch origin..."; git fetch origin > /dev/null
	@read -p "### Create feature: " feature; \
		git checkout -B feature-$$feature origin/develop > /dev/null
	@echo "### Recover state..."; git stash pop > /dev/null; echo

.PHONY: hotfix
hotfix:
	@echo "### Save state..."; git stash > /dev/null
	@echo "### Fetch origin..."; git fetch origin > /dev/null
	@read -p "### Create hotfix: " hotfix; \
		git checkout -B hotfix-$$hotfix origin/master > /dev/null
	@echo "### Recover state..."; git stash pop > /dev/null; echo

.PHONY: release
release:
	@echo "### Save state..."; git stash > /dev/null
	@echo "### Fetch origin..."; git fetch origin > /dev/null
	@echo "### Create release branch..."; git checkout -B release origin/master > /dev/null
	@read -p "### Create version: " version; \
		echo "$$version" > VERSION; \
		git commit -a -m "prepared release version $$version" > /dev/null; \
		git tag -f -a $$version -m "released version $$version" > /dev/null; \
		git push -f origin : $$version > /dev/null
	@echo "### Merge master..."; git checkout master > /dev/null; git merge release > /dev/null
	@echo "### Push master..."; git push origin master > /dev/null
	@echo "### Merge develop..."; git checkout develop > /dev/null; git merge release > /dev/null
	@echo "### Push develop..."; git push origin develop > /dev/null
	@echo "### Remove release branch..."; git branch -D release > /dev/null
	@echo "### Recover state..."; git stash pop > /dev/null; echo

.PHONY: docker-build
docker-build:
	@docker build -t $(IMAGE) --compress --no-cache --rm .

.PHONY: docker-run
docker-run:
	@docker rm -f $(CONTAINER); \
		docker run --name $(CONTAINER) -P -dt $(IMAGE) $(ARGS)

.PHONY: docker-logs
docker-logs:
	@clear
	@docker logs -f $(CONTAINER)

.PHONY: docker
docker: docker-build docker-run docker-logs
	# Write your own command when script finish the task
	# e.g. docker cp $(CONTAINER):/usr/src/app/result.csv .
