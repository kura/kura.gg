PY=python
PELICAN=pelican
PELICANOPTS=--fatal=errors

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_TARGET_DIR=/var/www/kura.gg

RANDOM_STRING:=$(shell echo $RANDOM | md5sum | head -c 12)

help:
	@echo 'Makefile for a pelican Web site'
	@echo ''
	@echo 'Usage:'
	@echo '   make html           (re)generate the web site'
	@echo '   make clean          remove the generated files'
	@echo '   make regenerate     regenerate files upon modification'
	@echo '   make publish        generate using production settings'
	@echo '   make start          start/restart develop_server.sh'
	@echo '   make stop           stop local server'
	@echo '   make rsync          upload the web site via rsync+ssh '
	@echo ''

.PHONY: html
html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

.PHONY: clean
clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete
	find . -type f -iname "*.pyc" -delete
	find . -type d -iname "__pycache__" -delete

.PHONY: regenerate
regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

.PHONY: dev-start
dev-start:
	pelican -rlD content/ &

.PHONY: dev-stop
dev-stop:
	for pid in `ps aux | grep pelican | grep -v grep | awk '{print$$2}'`; do \
		kill $$pid ; \
	done
	@echo 'Stopped Pelican.'

.PHONY: publish
publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

.PHONY: install
install:
	pip3 install -U -r requirements.txt
	sudo mkdir -p /usr/share/fonts/truetype/kura.gg/
	sudo cp eevee/static/fonts/*.ttf /usr/share/fonts/truetype/kura.gg/
	sudo fc-cache -v

.PHONY: test
test: clean rsync

.PHONY: cname
cname:
	echo "kura.gg" > $(OUTPUTDIR)/CNAME

.PHONY: remove_crud
remove_crud:
	bash scripts/remove_crud.sh $(OUTPUTDIR)/

.PHONY: pngquant
pngquant:
	bash scripts/pngquant.sh $(OUTPUTDIR)/

.PHONY: screenshot
screenshot:
	bash screenshot/screenshot.sh $(OUTPUTDIR)/

.PHONY: crawl
crawl:
	bash scripts/crawl.sh $(OUTPUTDIR)/

.PHONY: perms
perms:
	bash scripts/perms.sh $(OUTPUTDIR)/

.PHONY: hash
hash:
	bash scripts/md5.sh $(OUTPUTDIR)/
	bash scripts/sha1.sh $(OUTPUTDIR)/

.PHONY: touch
touch:
	python3 touch.py $(INPUTDIR)/ $(OUTPUTDIR)/

.PHONY: update_cv
update_cv:
	scripts/update_cv.sh

.PHONY: strip
strip:
	grep -rl "kura \[atpersand\]" output | xargs sed -i 's/kura \[atpersand\]/${RANDOM_STRING} \[atpersand\]/g'

.PHONY: rsync
rsync:
	rm -rf $(OUTPUTDIR)/*
	$(MAKE) publish
	rm -rf output/theme/fonts/roboto*
	rm -rf $(OUTPUTDIR)/curriculum-vitae/ && cp -R cv $(OUTPUTDIR)/curriculum-vitae/
	echo "kura.gg" > $(OUTPUTDIR)/CNAME
	# bash scripts/headerid.sh $(OUTPUTDIR)/
	bash scripts/remove_crud.sh $(OUTPUTDIR)/
	bash scripts/pngquant.sh $(OUTPUTDIR)/
	bash screenshot/screenshot.sh $(OUTPUTDIR)/
	# bash scripts/compress.sh $(OUTPUTDIR)/
	bash scripts/perms.sh $(OUTPUTDIR)/
	bash scripts/md5.sh $(OUTPUTDIR)/
	bash scripts/sha1.sh $(OUTPUTDIR)/
	python3 touch.py $(INPUTDIR)/ $(OUTPUTDIR)/
	# rm -rf $(OUTPUTDIR)/*

