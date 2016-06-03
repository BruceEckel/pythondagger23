.PHONY: clean dist html test

APP = pythondagger
DEVDIR = $(APP)-code

clean:
	cd bench && $(MAKE) -i clean
	cd doc && $(MAKE) -i clean
	cd test && $(MAKE) -i clean
	find . \( -name "*~" -o -name "*.pyc" \) -exec rm "{}" \;

dist:
  ifndef VER
		@echo "Error: VER is not defined. Try: make dist VER=1.0.0"
  else
		cd ..; rm -fr $(APP)-$(VER); mkdir $(APP)-$(VER); rsync --cvs-exclude -a $(DEVDIR)/ $(APP)-$(VER); tar zcvf $(APP)-$(VER).tar.gz $(APP)-$(VER); rm -fr $(APP)-$(VER);
  endif

html:
	cd doc && $(MAKE) html

pypi:
	python setup.py register sdist bdist_wininst upload
	-rm -fr MANIFEST build dist

pypidocs:
	cd doc/_build/html; zip -r /tmp/docs.zip *

test:
	cd test && $(MAKE) test
