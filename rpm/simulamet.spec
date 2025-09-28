Name: simulamet
Version: 1.2.2
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
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-sans-mono-fonts
BuildRequires: dejavu-serif-fonts
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
Requires: bash-completion
Requires: bridge-utils
Requires: btrfs-progs
Requires: bc
Requires: bwm-ng
Requires: colordiff
Requires: cronie
Requires: ethtool
Requires: git
Requires: gpm
Requires: hping3
Requires: htop
Requires: joe
Requires: jq
Requires: libidn
Requires: lksctp-tools
Requires: (mlocate or plocate)
Requires: net-snmp-utils
Requires: net-tools
Requires: netperfmeter
Requires: nmap
Requires: (ntpsec or ntpdate)
Requires: parallel
Requires: pxz
Requires: reprepro
Requires: rsplib-services
Requires: rsplib-tools
Requires: smartmontools
Requires: subnetcalc
Requires: tcpdump
Requires: tftp
Requires: traceroute
Requires: tree
Requires: vconfig
Requires: virt-what
Requires: whois
Recommends: grub2-tools
Recommends: reiserfs-utils
Recommends: ipsec-tools
Recommends: wireshark-cli

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
Requires: banner
Requires: bibtexconv
Requires: bison
Requires: boost-devel
Requires: bzip2-devel
Requires: clang
Requires: cmake
Requires: (createrepo_c or createrepo)
Requires: debhelper
Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts
Requires: dejavu-serif-fonts
Requires: devscripts
Requires: flex
Requires: gcc
Requires: gcc-c++
Requires: gdb
Requires: ghostscript
Requires: gimp
Requires: glib2-devel
Requires: gnupg
Requires: google-noto-cjk-fonts
Requires: google-noto-sans-fonts
Requires: google-noto-serif-fonts
Requires: GraphicsMagick
Requires: libcurl-devel
Requires: libpcap-devel
Requires: libtool
Requires: lksctp-tools-devel
Requires: make
Requires: mock
Requires: openssl-devel
Requires: pbuilder
Requires: perl-Image-ExifTool
Requires: python3
Requires: qtchooser
Requires: qt5-linguist
Requires: qt5-qtbase-devel
Requires: rsplib-librsplib-devel
Requires: quilt
Requires: R-base
Requires: rpm
Requires: rsplib-docs
Requires: texlive-epstopdf-bin
Requires: tidy
Requires: urw-base35-fonts
Requires: valgrind


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
