SSH Tunnelling
##############
:date: 2011-02-14 20:37
:author: kura
:category: tutorials
:tags: ssh, tunnel
:slug: ssh-tunnelling

Quite a simple one:

    ssh -f USER@INTERMEDIATE\_DEVICE -L
    LOCAL\_PORT:DESTINATION\_DEVICE:DESTINATION\_PORT -N

**-f** tells ssh to go to background
**-L** binds a local port to a remote device and port
**-N** tells ssh not to execute any commands

So use this to tunnel from local port 8000 in to a remote machine on
port 22 you'd use

    ssh -f user@server.test.com -L 8000:server.destination.com:22 -N

Once the tunnel is open you can use the following to ssh or scp data
around

    ssh localhost -p 8000
    scp -P 8000 /path/to/local/file user@localhost:~
    scp -P 8000 user@localhost:/path/to/remote/file .

I use ssh tunnels all the time to remote access and use one of our Solr
servers that is blocked behind a firewall.
