PY=python
PELICAN=pelican
PELICANOPTS=--fatal=errors

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_TARGET_DIR=/var/www/kura.io

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

html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete
	find . -type f -iname "*.pyc" -delete
	find . -type d -iname "__pycache__" -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

start-dev:
	pelican --autoreload --listen content/ &

stop-dev:
	for pid in `ps aux | grep pelican | grep -v grep | awk '{print$$2}'`; do \
		kill $$pid ; \
	done
	@echo 'Stopped Pelican.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS) --debug

install:
	pip install -r requirements.txt
	sudo mkdir -p /usr/share/fonts/truetype/kura.io/
	sudo cp eevee/static/fonts/*.ttf /usr/share/fonts/truetype/kura.io/
	sudo fc-cache -v

test: clean rsync

rsync:
	rm -rf $(OUTPUTDIR)/*
	$(MAKE) publish
	rm -rf output/theme/fonts/roboto*
	rm -rf $(OUTPUTDIR)/curriculum-vitae/ && cp -R cv $(OUTPUTDIR)/curriculum-vitae/
	echo "kura.gg" > $(OUTPUTDIR)/CNAME
	# bash scripts/headerid.sh $(OUTPUTDIR)/
	bash scripts/pngquant.sh $(OUTPUTDIR)/
	bash screenshot/screenshot.sh $(OUTPUTDIR)/
	# bash scripts/compress.sh $(OUTPUTDIR)/
	bash scripts/perms.sh $(OUTPUTDIR)/
	bash scripts/md5.sh $(OUTPUTDIR)/
	# rm -rf $(OUTPUTDIR)/*

.PHONY: html help clean regenerate start stop publish rsync
