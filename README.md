# Salt Project Native Minions for AIX salt-native-minion-aix

## Overview

Salt Native Minion for AIX was originally developed on GitLab
Here are the instructions for GitLab, but in final releases, the Salt Native
Minion for AIX was built using a bash script on AIX machines.

The AIX native minions are based on 64-bit Python 3.9, Tiamat and subsequently PyInstaller v5.5

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/saltstack/open/salt-native-minion-aix.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/saltstack/open/salt-native-minion-aix/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

## Name

Salt support for AIX v7.1 and v7.2

## Description

This project allows you to build support for Salt on AIX v7.1 and v7.2

Provided is a .gitlab-ci.yml file to utilise GitLab CI/CD or alternatively can use the test_bld_xxxx Bash scripts

The CI/CD file and Bash scripts generate a AIX bff package which can be installed and removed with AIX tools.

Documation on Salt 3005.1 for AIX can be found here:

    https://docs.saltproject.io/salt/install-guide/en/latest/topics/install-by-operating-system/aix.html


## Installation

### Before installing the AIX native minion:

Ensure that you have sufficient privileges to install packages on the AIX UNIX system.
Check that your AIX UNIX system is supported. See AIX for more information.
Ensure that ports 4505 and 4506 are open on the applicable AIX UNIX systems.
Salt uses ports 4505 and 4506 for outbound communication from the master to the minions. The AIX native minion uses a direct connection to the AIX UNIX system and uses the network interfaces for communication. For that reason, ports 4505 and 4506 need to be open on the appropriate network interfaces.

#### Install Salt on AIX

The AIX native minion package installs:

*   salt-minion service
*   salt-call service

Note: The salt-ssh and salt-proxy services are not installed with this package.

#### Salt minion package installation

#### To install the package on AIX:

Ensure that you have sufficient privileges to install packages on the AIX system.
Download, verify, and transfer the AIX installation files (prior to community-support this was repo.saltproject.io). The AIX native minion package is a tarball containing an installation and removal script and an AIX bff package.  Run the following commands to extract the installation file into a directory, example used is for the current stable release 3005.1:

.. code-block:: bash

    gzip --decompress salt_3005.1-1.tar.gz
    tar -xvf salt_3005.1-1.tar
    cd salt_3005.1

Note: This directory name may change slightly depending on the latest version of Salt.

Run the following command to install the package:

.. code-block:: bash

    ./install_salt.sh

You’ll see a message that indicates the installation is running. You can see a more detailed output if you install the package in verbose mode.

#### Configure and test the AIX native minion

To configure the AIX native minion to connect with its Salt master:

Edit the /etc/salt/minion file to update the minion configuration with your environment’s specific details, such as the master’s IP address, the minion ID, etc. For example, to set the minion name:

id: your-aix-minion-name

Edit the file to indicate the IP address of the master that is managing this minion. For example:

master: 192.0.2.1

Start the AIX native minion with the following command:

.. code-block:: bash

    startsrc -s salt-minion

To check that the AIX native minion is installed correctly and is running, use the following command:

.. code-block:: bash

    lssrc -g salt

If the AIX native minion is installed and running, the output will be similar to the following:

.. code-block::

    Subsystem         Group            PID          Status
    salt-minion       salt             20110110     active

Note: If the output reads salt-inoperative, that means the minion has not yet been started.

An alternative method to restart the minion is to use the command /etc/rc.d/init.d/salt-minion start but this method is not preferred.

Once the AIX native minion has been started and is running, you can use the command salt-key to verify the master has received a request for the minion key.

On the master, accept the minion’s key with the following command, replacing the placeholder test with the correct minion name:

.. code-block:: bash

    salt-key -y -a your-aix-minion-name

After waiting a small period of time, verify the connectivity between the master and the AIX native minion using simple commands. For example, try running the following commands:

.. code-block:: bash

    salt your-minion-name test.versions
    salt your-minion-name grains.items
    salt your-minion-name cmd.run ‘ls -alrt /’
    salt-call --local test.versions

You can now use the AIX native minion. See Usage below for more information.

#### Salt minion package removal

To uninstall the Salt minion salt package on AIX, run the following command:

.. code-block:: bash

    ./install_salt.sh -u

Alternatively, to remove any trace of salt on the system , run the following command:

.. code-block:: bash

    ./install_salt.sh -u -f

Warning: If install_salt.sh fails to uninstall Salt and you intend to install a new version, you must uninstall using an alternate method. Otherwise the previous package may remain in the cache.

The install script install_salt.sh as a number of self-explanatory options, which can be accessed using the -h option: ./install_salt.sh -h

## Usage

### Using the AIX native minion

You can access the Salt command line interface on the AIX native minion using wrapper scripts. These wrapper scripts execute with environmental variable overrides for library and Python paths. The wrapper scripts are located in the /usr/bin folder, which is typically included in the environmental variable PATH.

Note: The AIX native minion 3005.1 currently has scripts for:

.. code-block:: bash

    salt-minion
    salt-call

Salt command line functionality is available through the use of these scripts.
If srcmster is active, you can use AIX System Resource Controller commands to start, stop, and list the salt-minion daemon with startsrc, stopsrc and lssrc.

##### To start the minion:

.. code-block:: bash

    startsrc -s salt-minion

##### To stop the minion:

.. code-block:: bash

    stopsrc -s salt-minion

##### To check if the minion is running:

.. code-block:: bash

    lssrc -g salt

If the AIX native minion is installed and running, the output will be similar to the following:

.. code-block::

    Subsystem         Group            PID          Status
    salt-minion       salt             20110110     active

Note: If the output reads salt-inoperative, that means the minion has not yet been started.

You can also start the minion as a daemon using the following command:

.. code-block:: bash

    [/usr/bin/]salt-minion -d

## Support

Support can be found in various Salt communities, such as, Slack: https://saltstackcommunity.slack.com

## Contributing

Salt support on AIX is a community-run project and is open to all contributions.
The salt-native-minion-for-aix project team welcomes contributions from the
community. Before you start working with salt-native-minion-for-aix, please
read our [Developer Certificate of Origin](https://cla.vmware.com/dco).
All contributions to this repository must be signed as described on that page.
Your signature certifies that you wrote the patch or have the right to pass it
on as an open-source patch. For more detailed information,
refer to [CONTRIBUTING.md](CONTRIBUTING.md).

The regular Open Source methods of contributing to a project apply:

*   Fork the project
*   Make your modifications to your fork
*   Provide tests for your modifications
*   Submit Merge/Pull Request to the project
*   Adjust modifications as per Reviewers of Merge/Pull Request

## Authors and acknowledgment

The initial work in porting Salt for the AIX platform was done by David Murphy damurphy@vmware.com

## License

Apache License 2.0

## Project status

The Salt native minion for AIX and above is now a community project.  In the past, VMware through Salt Project supported and developed Salt for AIX, but VMware has now turned over on-going development to the community.

The project is currently seeking volunteers to step in as a maintainer or owner, to allow the project to keep going.

AIX 7.3 has been found to have issues with its rpm tool find-provides, also AIX 7.3 has issues with pipes and this is affecting find-provides (used in rpmbuild). Hence no support currently for AIX v7.3.

