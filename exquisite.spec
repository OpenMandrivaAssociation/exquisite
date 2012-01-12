#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/exquisite exquisite; \
#cd exquisite; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "exquisite" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf exquisite-$PKG_VERSION.tar.xz exquisite/ --exclude .svn --exclude .*ignore

%define svnrev	60246

Summary:	This is a psplash replacement that is very simple and uses EFL
Name:		exquisite
Version:	0.0.2
Release:	0.%{svnrev}.1
License:	BSD
URL:		http://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz
Group:		Graphical desktop/Enlightenment 

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)

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
%setup -qn %{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x

%make

%install
rm -fr %{buildroot}
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/exquisite/*


