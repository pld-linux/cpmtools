Summary:	Tools for accessing CP/M file systems
Summary(pl):	Narzêdzia pozwalaj±ce na dostêp do systemów plików CP/M
Name:		cpmtools
Version:	2.5
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.moria.de/~michael/cpmtools/%{name}-%{version}.tar.gz
# Source0-md5:	11fb7c34229e835537f87f170abd6035
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.moria.de/~michael/cpmtools/
BuildRequires:	libdsk-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/misc

%description
This package allows to access CP/M file systems similar to the
well-known mtools package, which accesses MSDOS file systems. It's
used mainly for file exchange with a Z80-PC simulator, but it works on
floppy devices as well.

%description -l pl
Ten pakiet pozwala na dostêp do systemów plików CP/M w sposób podobny
do dobrze znanego pakietu mtools, który pozwala na dostêp do systemów
plików MSDOS. Pakiet ten s³u¿y g³ównie do wymiany plików z symulatorem
Z80-PC, ale dzia³a tak¿e ze stacjami dyskietek.

%prep
%setup -q
%patch -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--with-libdsk

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D cpm.5 $RPM_BUILD_ROOT%{_mandir}/man5/cpm.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/diskdefs
%{_mandir}/man[15]/*
