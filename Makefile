PY=python
PELICAN=pelican
PELICANOPTS=

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
	@echo '   make startserver    start/restart develop_server.sh'
	@echo '   make stopserver     stop local server'
	@echo '   make rsync          upload the web site via rsync+ssh '
	@echo ''

html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

startserver:
	$(BASEDIR)/develop_server.sh start

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	kill `ps aux | grep pelican.server | grep -v grep | awk '{print $2}'`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

rsync: publish
	rsync -e "ssh" -P -avhp --delete $(OUTPUTDIR)/ ego.kura.io:$(SSH_TARGET_DIR) --cvs-exclude
	rm -rf $(OUTPUTDIR)/*

.PHONY: html help clean regenerate startserver stopserver publish rsync
