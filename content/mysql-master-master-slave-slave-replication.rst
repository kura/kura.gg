MySQL Master-Master-Slave-Slave Replication
###########################################
:date: 2010-09-04 18:14
:author: kura
:category: tutorials
:tags: mysql, replication
:slug: mysql-master-master-slave-slave-replication

.. contents::

Quick introduction
------------------

My employers presented me with a challenge this week. The task was not
difficult in the end but to me it was an untried concept involving
MySQL.

I have never been a fan of MySQL and generally turn my nose at the
thought of using it, let alone replicating it etc.

The task in question? Master -> Master -> Slave -> Slave replication.

From this point forward I will expect you to have MySQL installed and
set-up as normal.

-  Master 1 will be known as Master 1 and Slave 2 with IP 10.1.1.1
-  Master 2 will be known as Master 2 and Slave 1 with IP 10.1.1.2
-  Slave 1 will be known as Slave 3 with IP 10.1.1.3
-  and Slave 2 will be known as Slave 4 with IP 10.1.1.4

Master 1
--------

Modify your MySQL config file, usually named my.cnf or mysql.cnf

Add the following lines to [mysqld]

.. code:: ini

    [mysqld]
    server-id=1
    auto_increment_offset=1
    auto_increment_increment=2

    log-bin
    binlog-ignore-db=mysql
    binlog-ignore-db=test
    log-slave-updates

Save and close.

You should note that I have included *auto_increment_offset*and
*auto_increment_increment*. auto_increment_offset is the same as
server-id in my case, it does as the name suggests - offsets the auto
increment value. auto_increment_increment should be set to the number
of servers you have as masters, in this example we have 2.

Open up a MySQL prompt and run the following query

.. code:: mysql

    GRANT REPLICATION SLAVE ON *.* TO 'replication'@'10.1.1.2' IDENTIFIED BY 'password';

Now restart MySQL.

Master 2 (Slave 1)
------------------

Modify your MySQL config file.

Add the following in [mysqld]

.. code:: ini

    [mysqld]
    server-id=2
    auto_increment_offset=2
    auto_increment_increment=2

    log-bin
    binlog-ignore-db=mysql
    binlog-ignore-db=test
    log-slave-updates

    master-host = 10.1.1.1
    master-user = replication
    master-password = password
    master-port = 3306

Save and restart MySQL.

Now open a MySQL prompt and run the following queries

.. code:: mysql

    START SLAVE;
    SHOW SLAVE STATUS\G;

Slave_IO_Running and Slave_SQL_Running must be set to **Yes**.

Master 1 (Slave 2)
------------------

Open a MySQL prompt and run the following query

.. code:: mysql

    SHOW MASTER STATUS;

You should see a master record has been created.

Now we need to configure Master 1 to run as Slave 2.

Modify MySQL config and add the following lines to [mysqld]

.. code:: ini

    [mysqld]
    master-host = 10.1.1.2
    master-user = replication
    master-password = password
    master-port = 3306

Save and restart MySQL.

Master 2
--------

Open a MySQL prompt and run the following query

.. code:: mysql

    GRANT REPLICATION SLAVE ON *.* TO 'replication'@'10.1.1.1' IDENTIFIED BY 'password';

Master 1
--------

Open a MySQL prompt and run the following queries

.. code:: mysql

    START SLAVE;
    SHOW SLAVE STATUS\G;

Slave_IO_Running and Slave_SQL_Running must be set to **Yes**.

Slave 3 and Slave 4
-------------------

Now that you have Master - Master replication set up it's time to attach
the slaves.

I am going to do the following

-  make Slave 3 slave of Master 1
-  and Slave 4 a slave of Master 2.

Master 1
--------

Open a MySQL prompt and run the following query

.. code:: mysql

    GRANT REPLICATION SLAVE ON *.* TO 'replication'@'10.1.1.3' IDENTIFIED BY 'password';

Master 2
--------

Open a MySQL prompt and run the following query

.. code:: mysql

    GRANT REPLICATION SLAVE ON *.* TO 'replication'@'10.1.1.4' IDENTIFIED BY 'password';

Slave 3
-------

Open your MySQL config file, under [mysqld] put the following

.. code:: ini

    [mysqld]
    server-id=3

    master-host = 10.1.1.1
    master-user = replication
    master-password = password
    master-port = 3306

Save and restart MySQL.

Open a MySQL prompt and run the following queries

.. code:: mysql

    START SLAVE;
    SHOW SLAVE STATUS\G;

Slave_IO_Running and Slave_SQL_Running must be set to **Yes**.

Slave 4
-------

Open your MySQL config file, under [mysqld] put the following

.. code:: ini

    [mysql]
    server-id=4

    master-host = 10.1.1.2
    master-user = replication
    master-password = password
    master-port = 3306

Save and restart MySQL.

Open a MySQL prompt and run the following queries

.. code:: mysql

    START SLAVE;
    SHOW SLAVE STATUS\G;

Slave_IO_Running and Slave_SQL_Running must be set to **Yes**.
