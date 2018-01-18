Summary: CentOS Virt SIG Xen repo configs
Name: centos-release-xen
Epoch: 10
Version: 8
Release: 4%{?dist}
License: GPL
Group: System Environment/Base
# centos-release-xen-$version.XX.$arch should copy
# CentOS-Xen-$version.repo.$arch to CentOS-Xen-$version.repo.
#
# centos-release-xen should copy one of those $version's to
# CentOS-Xen.repo
Source100: CentOS-Xen-dependencies.repo.x86_64
Source144: CentOS-Xen-44.repo.x86_64
Source146: CentOS-Xen-46.repo.x86_64
Source148: CentOS-Xen-48.repo.x86_64
Source246: CentOS-Xen-46.repo.aarch64
Source300: grub-bootxen.sh
URL: http://wiki.centos.org/QaWiki/Xen4

Provides: centos-release-xen

BuildRoot: %{_tmppath}/centos-release-xen-root

ExclusiveArch: x86_64 aarch64

# This should pull in centos-release-virt-common
Requires: /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Virtualization
Requires: %{_bindir}/grub-bootxen.sh

%description
yum configs and scripts to allow easy installation of Xen on CentOS.

NOTE This package may change major versions of Xen automatically on
yum update.  If this is not the behavior you want, please install the
sub-package specific to the version of xen you want to use and then
remove this package.  (At the moment this is centos-release-xen-44 or
		       centos-release-xen-46).

%package common
Summary: CentOS Virt Sig Xen support files

%description common
This contains the grub-bootxen.sh helper-script which enables the xen
package to add itself to grub automatically.

%if 0%{?centos_ver} <= 6
%package 44
Summary: CentOS Virt Sig Xen repo configs for Xen 4.4
Requires: /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Virtualization
Requires: %{_bindir}/grub-bootxen.sh

%description 44
yum configs and scripts to allow easy installation of Xen 4.4 on CentOS.

Multiple versions of centos-release-xen-NN can be installed at the
same time; by default yum will choose the latest version of xen
available across all repositories.

NOTE This package will not update automatically to newer Xen releases;
\if you don\'t have centos-release-xen installed, you will have to
manually install the newer version of centos-release-xen-NN to get the
newer version.  If this is not the behavior you want, please install
the generic package (centos-release-xen).
%endif


%package 46
Summary: CentOS Virt Sig Xen repo configs for Xen 4.6
Requires: /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Virtualization
Requires: %{_bindir}/grub-bootxen.sh

%description 46
yum configs and scripts to allow easy installation of Xen 4.6 on CentOS.

Multiple versions of centos-release-xen-NN can be installed at the
same time; by default yum will choose the latest version of xen
available across all repositories.

This package will not update automatically to newer Xen releases;
\if you don\'t have centos-release-xen installed, you will have to
manually install the newer version of centos-release-xen-NN to get the
newer version.  If this is not the behavior you want, please install
the generic package (centos-release-xen).

%package 48
Summary: CentOS Virt Sig Xen repo configs for Xen 4.8
Requires: /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Virtualization
Requires: %{_bindir}/grub-bootxen.sh

%description 48
yum configs and scripts to allow easy installation of Xen 4.8 on CentOS.

Multiple versions of centos-release-xen-NN can be installed at the
same time; by default yum will choose the latest version of xen
available across all repositories.

This package will not update automatically to newer Xen releases;
\if you don\'t have centos-release-xen installed, you will have to
manually install the newer version of centos-release-xen-NN to get the
newer version.  If this is not the behavior you want, please install
the generic package (centos-release-xen).


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p -m 755 $RPM_BUILD_ROOT/%{_bindir}

%ifarch x86_64
# Install external dependencies
install -m 644 %{SOURCE100} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen-dependencies.repo

# Install per-release files
%if 0%{?centos_ver} <= 6
install -m 644 %{SOURCE144} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen-44.repo
%endif
install -m 644 %{SOURCE146} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen.repo
install -m 644 %{SOURCE146} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen-46.repo
install -m 644 %{SOURCE148} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen-48.repo

%endif

%ifarch aarch64
install -m 644 %{SOURCE246} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen.repo
install -m 644 %{SOURCE246} $RPM_BUILD_ROOT/etc/yum.repos.d/CentOS-Xen-46.repo
%endif
install -m 744 %{SOURCE300} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/CentOS-Xen.repo

%files common
%{_bindir}/grub-bootxen.sh

%ifarch x86_64
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/CentOS-Xen-dependencies.repo
%endif

%if 0%{?centos_ver} <= 6
%files 44
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/CentOS-Xen-44.repo
%endif

%files 46
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/CentOS-Xen-46.repo

%files 48
%defattr(-,root,root)
%config(noreplace) /etc/yum.repos.d/CentOS-Xen-48.repo

%changelog
* Thu Jan 18 2018 George Dunlap <george.dunlap@citrix.com> - 8-4.centos
- Add 'dependencies' repo, to selectively enable packages from epel

* Mon Nov 21 2016 George Dunlap <george.dunlap@citrix.com> - 8-3.centos
- Add repository for 4.8.  Leave default at 4.6 for now.

* Tue Mar 22 2016 George Dunlap <george.dunlap@citrix.com> - 8-2.centos
- Point centos-release-xen to Xen 4.6 for CentOS 6

* Mon Feb 15 2016 George Dunlap <george.dunlap@citrix.com> - 8-1.centos
- Break out version-specific packages for those who don\'t want to update
  automatically.

* Wed Jan 20 2016 George Dunlap <george.dunlap@citrix.com> - 7-12.centos
- Fix bug \in grub-bootxen.sh that caused no initrd line to be installed
  when installing or upgrading a kernel when xen was already installed

* Wed Nov 11 2015 George Dunlap <george.dunlap@citrix.com> - 7-11.centos
- buildlogs (centos-virt-xen-testing) packages are not signed

* Tue Nov  3 2015 George Dunlap <george.dunlap@citrix.com> - 7-10.centos
- Removed CBS repositories
- Moved C6 repos to Virt SIG layout
- Include all files so we can build the same srpm on any arch

* Wed Sep 16 2015 George Dunlap <george.dunlap@citrix.com> - 7-9.centos
- Add dependency on Virt SIG gpg key
- Shifted /etc/sysconfig/xen-kernel to xen package

* Tue Sep 15 2015 George Dunlap <george.dunlap@citrix.com> - 7-8.centos
- Configure for aarch64 systems

* Tue Sep 08 2015 George Dunlap <george.dunlap@citrix.com> - 7-7.centos
- Change virt6 repos to new format (virt6-xen-{44,46}-{testing,candidate})

* Tue Sep 01 2015 George Dunlap <george.dunlap@citrix.com> - 7-6.centos
- Add virt7-xen-46-* repos for 4.6 testing

* Thu Jul 30 2015 George Dunlap <george.dunlap@eu.citrix.com> - 7-5.centos
- Fix grub-bootxen.sh script

* Wed Jun 24 2015 George Dunlap <george.dunlap@eu.citrix.com> - 7-4.centos
- Update GPG key name
- Fix link following bug \in grub-bootxen

* Wed Jun 17 2015 George Dunlap <george.dunlap@eu.citrix.com> - 7-3.centos
- Update core C7 repos

* Tue May 26 2015 George Dunlap <george.dunlap@eu.citrix.com> - 7-2.el6.centos
- Use plain files rather than a tarball for easier source tracking
- Add Virt SIG repos (disabled by default)

* Mon Oct 20 2014 Johnny Hughes <johnny@centos.org> - 6-4.el6.centos
- shifted /etc/sysconfig/xen-kernel to centos-xen-release

* Thu Oct  9 2014 Johnny Hughes <johnny@centos.org> - 6-3.el6.centos
- Modified grub-bootxen.sh to allow for automatic grub updates for kernel install

* Wed Jun 19 2013 Karanbir Singh <kbsingh@centos.org> - 6-2.el6.centos
- Update to release

* Thu Jan 31 2013 Karanbir Singh <kbsingh@centos.org> - 6-0.el6.centos
- Build for CentOS Xen Beta release

