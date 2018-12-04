Name: simulamet
Version: 0.0.0
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
# %define _unpackaged_files_terminate_build 0


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

%files
/usr/share/simulamet/*.pdf
/usr/share/simulamet/Desktop-with-Logo/*x*/*/*
/usr/share/simulamet/Desktop-without-Logo/*x*/*/*
/usr/share/simulamet/Splash/*

%doc


%changelog
* Wed Nov 22 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
