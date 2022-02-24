# Copyright (C) 2021, Achiefs.

Summary:     FIM software provides a easy way to watch your files.
Name:        fim
Version:     %{_version}
Release:     1
License:     GPL
Group:       System Environment/Daemons
Source0:     %{name}-%{version}.tar.gz
URL:         https://github.com/Achiefs/fim
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Vendor:      Achiefs <support@achiefs.com>
Packager:    Jose Fernandez <support@achiefs.com>
AutoReqProv: no
ExclusiveOS: linux

%description
FIM helps you to monitor your files of any unwanted action.

%prep
%setup -q
curl https://sh.rustup.rs -sSf | sh -s -- -y

%build
source $HOME/.cargo/env
cargo build --release

%install
mkdir -p -m 640 ${RPM_BUILD_ROOT}%{_configdir}
mkdir -p -m 640 ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p -m 640 ${RPM_BUILD_ROOT}/lib/systemd/system
mkdir -p -m 640 ${RPM_BUILD_ROOT}/usr/share/man/man1

install -m 0750 target/release/fim ${RPM_BUILD_ROOT}%{_bindir}/
install -m 0640 config/linux/config.yml ${RPM_BUILD_ROOT}%{_configdir}/
install -m 0644 pkg/fim.service ${RPM_BUILD_ROOT}/lib/systemd/system/
install -m 0644 pkg/fim.1 ${RPM_BUILD_ROOT}/usr/share/man/man1/

%pre
%post
%preun
%postun

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%attr(750, root, root) %{_bindir}/fim
%dir %attr(750, root, root) %{_configdir}
%attr(640, root, root) %config(noreplace) %{_configdir}/config.yml
%attr(644, root, root) /lib/systemd/system/fim.service
%attr(644, root, root) /usr/share/man/man1/fim.1.gz



%changelog
* Tue Jan 18 2022 support <support@achiefs.com> - 0.2.1
- More info: https://github.com/Achiefs/fim/releases/tag/v0.2.1

* Tue Oct 05 2021 support <support@achiefs.com> - 0.2.0
- More info: https://github.com/Achiefs/fim/releases/tag/v0.2.0
