Name: simulamet
Version: 1.2.4~rc1.2
Release: 1
Summary: SimulaMet Desktop
Group: Applications/Internet
License: GPL-3.0-or-later
URL: https://www.simulamet.no
Source: https://packages.nntb.no/sources/%{name}-%{version}.tar.xz

# FIXME: S390x does not provide the dependency Gimp 3.x, yet.
#        Once this is fixed, the architecture exclusion can be removed:
ExcludeArch: s390x

AutoReqProv: on
BuildRequires: cmake
BuildRequires: dejavu-fonts-all
BuildRequires: gcc
BuildRequires: ghostscript
BuildRequires: gimp
BuildRequires: google-noto-cjk-fonts
BuildRequires: google-noto-sans-fonts
BuildRequires: google-noto-serif-fonts
BuildRequires: GraphicsMagick
BuildRequires: perl-Image-ExifTool
BuildRequires: urw-base35-fonts
BuildRoot: %{_tmppath}/%{name}-%{version}-build


# This package does not generate debug information (no executables):
%global debug_package %{nil}

# TEST ONLY:
# define _unpackaged_files_terminate_build 0


%description
 This package contains the scripts to configure a SimulaMet desktop.
 See https://www.simulamet.no for details on SimulaMet!

%prep
%setup -q

%build
# NOTE: CMAKE_VERBOSE_MAKEFILE=OFF for reduced log output!
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DFLAT_DIRECTORY_STRUCTURE=0 -DPRINT_A4=1 -DINSTALL_ORIGINALS=0 -DCMAKE_VERBOSE_MAKEFILE=OFF .
%cmake_build

%install
%cmake_install
# ====== Relocate files =====================================================
mkdir -p %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Gressholmen-*.jpeg   %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Lindøya-*.jpeg       %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Oslo-*.jpeg          %{buildroot}/boot/SimulaMet
mkdir -p %{buildroot}/etc/simulamet
mv %{buildroot}/usr/share/simulamet/Splash/simulamet-version   %{buildroot}/etc/simulamet
# ===========================================================================


%package management
Summary: Management tools for the SimulaMet system environment
Group: Applications/Internet
BuildArch: noarch
Requires: acl
Requires: bash
Requires: bash-completion
Requires: bind-utils
Requires: bridge-utils
Requires: bwm-ng
Requires: bzip2
Requires: chrpath
Requires: cloud-utils-growpart
Requires: cmake
Requires: curl
Requires: dnf-automatic
Requires: ethtool
Requires: fail2ban
Requires: gdisk
Requires: git
Requires: gpg
Requires: gpm
Requires: hipercontracer
Requires: htop
Requires: iproute
Requires: iproute-tc
Requires: iptables
Requires: iputils
Requires: joe
Requires: jq
Requires: kernel-modules-extra
Requires: libidn
Requires: make
Requires: man
Requires: netperfmeter
Requires: netplan
Requires: net-tools
Requires: nmap
Requires: openssh-server
Requires: openssl
Requires: parallel
Requires: plocate
Requires: pwgen
Requires: python3
Requires: rsplib-tools
Requires: rsync
Requires: subnetcalc
Requires: sudo
Requires: tar
Requires: tcpdump
Requires: td-system-tools
Requires: td-system-tools-configure-grub
Requires: traceroute
Requires: tree
Requires: tsctp
Requires: unzip
Requires: uuid
Requires: virt-what
Requires: wget
Requires: wireshark-cli
Requires: zip
Recommends: grub2-tools

%description management
This metapackage contains basic software for SimulaMet system management.
The software installed provides a common working environment.
See http://www.simulamet.no for details on SimulaMet!

%files management
/boot/SimulaMet/Oslo-*.jpeg
%{_sysconfdir}/grub.d/??_simulamet_management_theme
%{_sysconfdir}/simulamet/simulamet-version
%{_datadir}/simulamet/grub-defaults
%{_sysconfdir}/system-info.d/20-simulamet
%{_sysconfdir}/system-maintenance.d/20-simulamet

%post management
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun management
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package development
Summary: Development tools for the SimulaMet system environment
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}
Requires: autoconf
Requires: automake
Requires: bc
Requires: bison
Requires: boost-devel
Requires: bzip2-devel
Requires: c-ares-devel
Requires: clang
Requires: cmake
Requires: dejavu-fonts-all
Requires: extra-cmake-modules
Requires: flex
Requires: g++
Requires: gcc
Requires: gdb
Requires: GeoIP-devel
Requires: ghostscript
Requires: git-lfs
Requires: google-noto-fonts-all
Requires: GraphicsMagick
Requires: libcurl-devel
Requires: libtool
Requires: lksctp-tools-devel
Requires: mock
Requires: open-sans-fonts
Requires: openssl-devel
Requires: pbuilder
Requires: pdf2svg
Requires: perl-Image-ExifTool
Requires: pkg-config
Requires: python3
Requires: python3-netifaces
Requires: python3-pip
Requires: python3-setuptools
Requires: qt6-linguist
Requires: qt6-qtbase-devel
Requires: R-base
Requires: reprepro
Requires: rpm-build
Requires: rsplib-libcpprspserver-devel
Requires: rsplib-librsplib-devel
Requires: shellcheck
Requires: urw-base35-fonts
Requires: xz-devel
Requires: zlib-devel
Recommends: qt6-linguist
Recommends: qt6-qtbase-devel
Recommends: valgrind
Recommends: yamllint


%description development
This metapackage contains basic software for SimulaMet development.
The software installed provides a common working environment.
See https://www.simulamet.no for details on SimulaMet!

%files development
/boot/SimulaMet/Gressholmen-*.jpeg
%{_sysconfdir}/grub.d/??_simulamet_development_theme

%post development
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun development
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package desktop
Summary: Desktop setup for the SimulaMet system environment
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}

%description desktop
This metapackage contains the scripts to configure a SimulaMet desktop.
See https://www.simulamet.no for details on SimulaMet!

%files desktop
/boot/SimulaMet/Lindøya-*.jpeg
%{_sysconfdir}/grub.d/??_simulamet_desktop_theme
%{_datadir}/simulamet/SimulaMet-A4.pdf
%{_datadir}/simulamet/Desktop-with-Logo/*x*/*/*
%{_datadir}/simulamet/Desktop-without-Logo/*x*/*/*
%ghost %{_datadir}/simulamet/Splash

%post desktop
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun desktop
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%changelog
* Mon Sep 29 2025 Thomas Dreibholz <dreibh@simula.no> - 1.2.3-1
- New upstream release.
* Thu Jul 10 2025 Thomas Dreibholz <dreibh@simula.no> - 1.2.2
- New upstream release.
* Wed Jul 09 2025 Thomas Dreibholz <dreibh@simula.no> - 1.2.1
- New upstream release.
* Sat Dec 14 2024 Thomas Dreibholz <dreibh@simula.no> - 1.2.0
- New upstream release.
* Tue Dec 19 2023 Thomas Dreibholz <dreibh@simula.no> - 1.1.14
- New upstream release.
* Tue Dec 12 2023 Thomas Dreibholz <dreibh@simula.no> - 1.1.13
- New upstream release.
* Wed Dec 06 2023 Thomas Dreibholz <dreibh@simula.no> - 1.1.12
- New upstream release.
* Tue Aug 08 2023 Thomas Dreibholz <dreibh@simula.no> - 1.1.11
- New upstream release.
* Wed Feb 08 2023 Thomas Dreibholz <dreibh@simula.no> - 1.1.10
- New upstream release.
* Sun Sep 11 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.9
- New upstream release.
* Tue Feb 15 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.8
- New upstream release.
* Mon Feb 14 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.7
- New upstream release.
* Mon Jun 14 2021 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.6
- New upstream release.
* Tue Dec 15 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.5
- New upstream release.
* Tue Dec 08 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.4
- New upstream release.
* Sun Nov 15 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.3
- New upstream release.
* Tue Oct 27 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.2
- New upstream release.
* Sat Oct 10 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.1
- New upstream release.
* Tue Oct 06 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.0
- New upstream release.
* Tue May 05 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.2
- New upstream release.
* Sat Jan 25 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.1
- New upstream release.
* Sat Jan 25 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- New upstream release.
* Wed Nov 13 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.0
- New upstream release.
* Fri Sep 20 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.1
- New upstream release.
* Thu Aug 22 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.0
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.6.0
- New upstream release.
* Fri Jul 05 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.3
- New upstream release.
* Wed Jul 03 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.2
- New upstream release.
* Mon Jun 17 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.1
- New upstream release.
* Wed Nov 22 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
