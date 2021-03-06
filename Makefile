.PHONY: clean tests cov docs release-tag

VERSION = $(shell python -c "print(__import__('rpi_displays').__version__)")

clean:
	rm -fr docs/_build build/ dist/
	make -C docs clean

tests:
	py.test --cov

cov: tests
	coverage html
	@echo open htmlcov/index.html

apidoc:
	make -C docs apidoc

docs:
	make -C docs html
	@echo open docs/_build/html/index.html

release-tag:
	@echo About to release ${VERSION}; read
	@echo [ENTER] to continue; read
	git tag -a "v${VERSION}" -m "Version v${VERSION}" && git push --follow-tags
