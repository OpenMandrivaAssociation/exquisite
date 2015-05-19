Summary:	This is a psplash replacement that is very simple and uses EFL
Name:		exquisite
Version:	1.0.0
Release:	3
Group:		Graphical desktop/Enlightenment
License:	BSD
URL:		http://enlightenment.org/
Source0: 	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-con)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(eio)

%description
This is a psplash replacement that is very simple and uses EFL (Evas, Edje,
Ecore etc.) for display - thus having immensely powerful theme abilities
without needing any platform-specific compiled themes or modules. It is
compatible with psplash with the same message commands (and more). The
difference is that it requires libraries like evas, edje, ecore, eet and
embryo. These also have loadable modules of their own - thus this is not
perfect for systems that can not have these libraries available and working at
boot, but if you can, it is a lot more capable than other splash engines,
while still running in the framebuffer.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/exquisite/*

