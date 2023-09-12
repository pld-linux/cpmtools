Summary:	Tools for accessing CP/M file systems
Summary(pl.UTF-8):	Narzędzia pozwalające na dostęp do systemów plików CP/M
Name:		cpmtools
Version:	2.24
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	http://www.moria.de/~michael/cpmtools/files/%{name}-%{version}.tar.gz
# Source0-md5:	0cb3a4c2fa7b2b05d9096d06b4b126b7
Patch0:		%{name}-install.patch
Patch1:		%{name}-link.patch
URL:		http://www.moria.de/~michael/cpmtools/
BuildRequires:	autoconf >= 2.13
BuildRequires:	libdsk-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to access CP/M file systems similar to the
well-known mtools package, which accesses MSDOS file systems. It's
used mainly for file exchange with a Z80-PC simulator, but it works on
floppy devices as well.

%description -l pl.UTF-8
Ten pakiet pozwala na dostęp do systemów plików CP/M w sposób podobny
do dobrze znanego pakietu mtools, który pozwala na dostęp do systemów
plików MSDOS. Pakiet ten służy głównie do wymiany plików z symulatorem
Z80-PC, ale działa także ze stacjami dyskietek.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--datarootdir=%{_datadir}/misc \
	--with-libdsk

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/cpm*
%attr(755,root,root) %{_bindir}/fsck.cpm
%attr(755,root,root) %{_bindir}/fsed.cpm
%attr(755,root,root) %{_bindir}/mkfs.cpm
%{_datadir}/misc/diskdefs
%{_mandir}/man1/cpm*.1*
%{_mandir}/man1/fsck.cpm.1*
%{_mandir}/man1/fsed.cpm.1*
%{_mandir}/man1/mkfs.cpm.1*
%{_mandir}/man5/cpm.5*
%{_mandir}/man5/diskdefs.5*
