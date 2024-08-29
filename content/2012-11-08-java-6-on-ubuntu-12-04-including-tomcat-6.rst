Java 6 on Ubuntu 12.04 (including Tomcat 6)
###########################################
:date: 2012-11-08 11:47
:author: kura
:category: howto
:category: tutorials
:slug: java-6-on-ubuntu-12-04-including-tomcat-6

.. contents::
    :backlinks: none

If like me you run in to issue when using OpenJDK, my issues come from
it's memory problems when you're allocating and using large amounts of
memory - mostly for Solr where we're concerned but obviously I'd switch
for other high memory usage instances too.

So without further ado, lets get the installation going.

You'll need Debian's "add-apt-repository", on servers this doesn't
usually come by default so we'll need to install it.

.. code-block:: bash

    sudo apt-get install python-software-properties

Next we need to add Java's PPA.

.. code-block:: bash

    sudo add-apt-repository ppa:sun-java-community-team/sun-java6

Once this is done we'll need to update our apt caches and install Java
6.

.. code-block:: bash

    sudo apt-get install sun-java6-jdk

Now that this is installed we should get the Java version, remember it
for future.

.. code-block:: bash

    java -version

You'll get something like this

.. code-block:: bash

    java version "1.6.0_20" OpenJDK Runtime Environment (IcedTea6 1.9.9) (6b20-1.9.9-0ubuntu1~10.04.2)
    OpenJDK 64-Bit Server VM (build 19.0-b09, mixed mode)

Next we update our alternatives to switch OpenJDK with Sun's Java.

.. code-block:: bash

    sudo update-java-alternatives -s java-6-sun

And finally we'll confirm the change is made by comparing the new Java
version against the one from before

.. code-block:: bash

    java -version

You should see something similar to this.

.. code-block:: bash

    java version "1.6.0_21"
    Java(TM) SE Runtime Environment (build 1.6.0_21-b06)
    Java HotSpot(TM) 64-Bit Server VM (build 17.0-b16, mixed mode)

Tomcat 6
--------

To make Tomcat use this version of Java we'll need to change JAVA_HOME.

Open up **/etc/default/tomcat6** for editing, you'll need to open this
using sudo or as root.

Scroll down, you'll see JAVA_HOME is set, it may be commented out so
edit it to look like the line below.

.. code-block:: bash

    JAVA_HOME=/usr/lib/jvm/java-6-sun

And restart Tomcat.

.. code-block:: bash

    sudo /etc/init.d/tomcat6 restart
