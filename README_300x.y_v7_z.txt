=================================
Salt Packages for AIX 7.z
=================================

Version: salt.30.0.x.y.bff (300x.y)
Date: 202?-??-??

To Install:
-----------
Salt is installed mainly into the /opt/salt directory, and a minimum of
2GBytes of disk space is required to install. Wrapper scripts for the
command-line interfaces are installed in the /usr/bin directory
(see the "Usage on AIX" section below).
Further documentation can be viewed at
https://saltstack.gitlab.io/open/docs/salt-install-guide/topics/install/native/index.html
Note: updates are handled by the install script.

1. Browse to https://repo.saltproject.io/salt/py3/aix and download the *.gz installation
file for your OS version.

2. Run the following commands to extract the installation file into a directory:

gzip --decompress salt_3005x.y-1.tar.gz
tar -xvf salt_3005x.y-1.tar
cd salt_3005x.y

3. Run the following command to install:

./install_salt.sh

To Uninstall:
-------------
1. Run the following command:

./install_salt.sh -u

2. To completely remove any trace of salt on the system , run command:

./install_salt.sh -u -f

Note: If install_salt.sh fails to uninstall Salt and you intend to install a new
version, you must uninstall using an alternate method. Otherwise the previous
package may remain in the cache.


The install script install_salt.sh as a number of self-explanatory options,
which can be examined using the -h option:

    ./install_salt.sh -h


Usage on AIX
------------
Wrapper scripts are provided to access the Salt command-line interfaces. These
wrapper scripts execute with environmental variable overrides for library and
python paths. These wrapper scripts are provided in /usr/bin, which is typically
included in the environmental variable PATH.

The following wrapper scripts are available:

  salt-ssh
  salt-proxy
  salt-minion


Note: with this release only salt-minion functionality is provided

Salt command line functionality is available through the use of
these wrapper scripts. For example, to start the salt-minion as a daemon:

[/usr/bin/]salt-minion -d


Additionally the use of AIX System Resource Controller commands can now
be used to start, stop and list the following salt daemons with
startsrc, stopsrc and lssrc, if srcmstr is active:

  salt-minion

For example:
  startsrc -s salt-minion
  stopsrc -s salt-minion

  lssrc -g salt

