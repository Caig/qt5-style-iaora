Name:		qt5-style-iaora
Summary:	Mandriva's IaOra widget style ported to Qt5
Version:	0.3.5.1
Release:	1
License:	GPLv3+
Group:		System/Libraries
Url:		https://store.kde.org/p/1183616/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
The old Mandriva's IaOra widget style ported to Qt5.
It includes the original color schemes too.

%files
%{_qt5_plugindir}/styles/libiaora-qt.so
/etc/iaoracolors
%{_datadir}/color-schemes/IaOra*.colors

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
