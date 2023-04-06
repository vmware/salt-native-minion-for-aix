# Copyright 2019-2022 VMware, Inc.
# SPDX-License-Identifier: Apache-2

# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global srcname salt


Name:       %{srcname}
Version:    %{_salt_ver}
Release:    %{_salt_release}
Group:      System Environment/Daemons
Summary:    Self contained Salt Minion binary
License:    ASL 2.0

Source0: run
Source1: minion
Source2: salt-common.logrotate
Source3: salt-call
Source4: salt-minion
Source5: salt-minion_rc_script
Source6: salt-minion_src

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Self contained Python 3.9 Salt Minion 64-bit binary for AIX

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%install
rm -fR %{buildroot}

mkdir -p %{buildroot}/opt/saltstack/salt
cp -R %{SOURCE0} %{buildroot}/opt/saltstack/salt

# Add some directories
install -d -m 0755 %{buildroot}%{_var}/log/salt
touch %{buildroot}%{_var}/log/salt/minion
install -d -m 0755 %{buildroot}%{_var}/cache/salt
install -d -m 0755 %{buildroot}%{_sysconfdir}/salt
install -d -m 0755 %{buildroot}%{_sysconfdir}/salt/minion.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/salt/pki
install -d -m 0700 %{buildroot}%{_sysconfdir}/salt/pki/minion
install -d -m 0755 %{buildroot}%{_bindir}

# Add the config files
install -D -p -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/salt/minion

# Logrotate
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/salt

# Add helper scripts
install -D -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/salt-call
install -D -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/salt-minion
install -D -m 0755 %{SOURCE5} %{buildroot}%{_initddir}/salt-minion
install -D -m 0755 %{SOURCE6} %{buildroot}%{_initddir}/salt-minion_src


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_var}/cache/salt
%{_var}/log/salt
%{_bindir}/salt-call
%{_bindir}/salt-minion
/opt/saltstack/salt/run
%config(noreplace) %{_sysconfdir}/salt/
%config(noreplace) %{_sysconfdir}/salt/minion
%config(noreplace) %{_sysconfdir}/salt/minion.d
%config(noreplace) %{_sysconfdir}/salt/pki/minion
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
%config(noreplace) %{_initddir}/salt-minion
%config(noreplace) %{_initddir}/salt-minion_src


%changelog
* %{_salt_date} SaltProject Packaging Team <saltproject-packaging@vmware.com> - %{_salt_ver}-%{_salt_release}
- Initial rpm for delivering Python 3 tiamat-based Salt Minion binary

* Thu Oct 15 2020 SaltProject Packaging Team <saltproject-packaging@vmware.com> - 3001.1-1
- Initial rpm for delivering Python 3 tiamat-based Salt Minion binary
