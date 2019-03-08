Name: simulamet
Version: 0.5.0
Release: 1
Summary: SimulaMet Desktop
Group: Applications/Internet
License: GPLv3
URL: https://www.simulamet.no
Source: https://packages.nntb.no/sources/%{name}-%{version}.tar.gz

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
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DFLAT_DIRECTORY_STRUCTURE=0 -DPRINT_A4=1 -DINSTALL_ORIGINALS=0 .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# ====== Relocate files =====================================================
mkdir -p %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Gressholmen-1024x768.jpeg   %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Lindøya-1024x768.jpeg       %{buildroot}/boot/SimulaMet
mv %{buildroot}/usr/share/simulamet/Splash/Oslo-1024x768.jpeg          %{buildroot}/boot/SimulaMet
mkdir -p %{buildroot}/etc/simulamet
mv %{buildroot}/usr/share/simulamet/Splash/simulamet-version   %{buildroot}/etc/simulamet
# ===========================================================================


%package management
Summary: SimulaMet Management
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
Requires: ipsec-tools
Requires: joe
Requires: jq
Requires: libidn
Requires: lksctp-tools
Requires: mlocate
Requires: net-snmp-utils
Requires: net-tools
Requires: nmap
Requires: ntpdate
Requires: pxz
Requires: reiserfs-utils
Requires: reprepro
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
Recommends: netperfmeter
Recommends: rsplib-docs
Recommends: rsplib-services
Recommends: rsplib-tools
Recommends: wireshark-cli

%description management
This metapackage contains basic software for SimulaMet system management.
The software installed provides a common working environment.
See http://www.simulamet.no for details on SimulaMet!

%files management
/boot/SimulaMet/Oslo-1024x768.jpeg
%{_sysconfdir}/grub.d/??_simulamet_management_theme
%{_sysconfdir}/simulamet/simulamet-version
%{_datadir}/simulamet/grub-defaults

%post management
echo "Updating /etc/default/grub with NorNet settings:"
echo "-----"
cat /usr/share/simulamet/grub-defaults | \
   ( if grep "biosdevname=0" >/dev/null 2>&1 /proc/cmdline ; then sed "s/^GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"biosdevname=0 /g" ; else cat ; fi ) | \
   ( if grep "net.ifnames=0" >/dev/null 2>&1 /proc/cmdline ; then sed "s/^GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"net.ifnames=0 /g" ; else cat ; fi ) | tee /etc/default/grub.new && \
mv /etc/default/grub.new /etc/default/grub
echo "-----"
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun management
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package development
Summary: SimulaMet Development
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}
Requires: autoconf
Requires: automake
Requires: banner
Requires: bison
Requires: boost-devel
Requires: bzip2-devel
Requires: clang
Requires: cmake
Requires: createrepo
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
Requires: gnuplot
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
Requires: pkg-config
Requires: python3
Requires: qt5-qtbase-devel
Requires: quilt
Requires: R-base
Requires: rpm
Requires: texlive-epstopdf-bin
Requires: urw-base35-fonts
Requires: valgrind
Recommends: rsplib-devel


%description development
This meta-package contains basic software for SimulaMet development.
The software installed provides a common working environment.
See https://www.simulamet.no for details on SimulaMet!

%files development
/boot/SimulaMet/Gressholmen-1024x768.jpeg
%{_sysconfdir}/grub.d/??_simulamet_development_theme

%post development
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun development
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package desktop
Summary: SimulaMet Desktop
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-management = %{version}-%{release}

%description desktop
This meta-package contains the scripts to configure a SimulaMet desktop.
See https://www.simulamet.no for details on SimulaMet!

%files desktop
/boot/SimulaMet/Lindøya-1024x768.jpeg
%{_sysconfdir}/grub.d/??_simulamet_desktop_theme
%{_datadir}/simulamet/SimulaMet-A4.pdf
%{_datadir}/simulamet/Desktop-with-Logo/*x*/*/*
%{_datadir}/simulamet/Desktop-without-Logo/*x*/*/*
%ghost /usr/share/simulamet/Splash

%post desktop
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun desktop
rm -f /etc/grub.d/??_simulamet_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%changelog
* Wed Nov 22 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
