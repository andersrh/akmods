Name:           ublue-os-akmods-addons
Version:        0.3
Release:        1%{?dist}
Summary:        Signing key and repos for ublue os akmods

License:        MIT
URL:            https://github.com/ublue-os/akmods

BuildArch:      noarch
Supplements:    mokutil policycoreutils

Source0:        public_key.der
Source1:        _copr_ublue-os-akmods.repo
Source2:        negativo17-fedora-steam.repo

%description
Adds the signing key for importing with mokutil to enable secure boot for kernel modules and repo files required to install akmod dependencies.

%prep
%setup -q -c -T


%build
# Have different name for *.der in case kmodgenca is needed for creating more keys
install -Dm0644 %{SOURCE0} %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/pki/akmods/certs/akmods-ublue.der
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/_copr_ublue-os-akmods.repo
install -Dm0644 %{SOURCE2} %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo

sed -i 's@enabled=1@enabled=0@g' %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo

install -Dm0644 %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/pki/akmods/certs/akmods-ublue.der            %{buildroot}%{_sysconfdir}/pki/akmods/certs/akmods-ublue.der
install -Dm0644 %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/_copr_ublue-os-akmods.repo    %{buildroot}%{_sysconfdir}/yum.repos.d/_copr_ublue-os-akmods.repo
install -Dm0644 %{buildroot}%{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo     %{buildroot}%{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo

%files
%attr(0644,root,root) %{_datadir}/ublue-os/%{_sysconfdir}/pki/akmods/certs/akmods-ublue.der
%attr(0644,root,root) %{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/_copr_ublue-os-akmods.repo
%attr(0644,root,root) %{_datadir}/ublue-os/%{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo
%attr(0644,root,root) %{_sysconfdir}/pki/akmods/certs/akmods-ublue.der
%attr(0644,root,root) %{_sysconfdir}/yum.repos.d/_copr_ublue-os-akmods.repo
%attr(0644,root,root) %{_sysconfdir}/yum.repos.d/negativo17-fedora-steam.repo

%changelog
* Mon Jul 17 2023 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.3
- Add ublue-os/akmods copr repo for modules not available upstream/elsewhere

* Tue May 30 2023 Benjamin Sherman <benjamin@holyarmy.org> - 0.2
- Add negativo17 fedora-steam repo to enable xbox controllers

* Fri May 18 2023 David Hoell - 0.1
- Add key for enrolling ublue kernel modules for secure boot
