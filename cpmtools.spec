Summary:	-
Summary(pl):	-
Name:		cpmtools
Version:	2.1
Release:	1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.moria.de/~michael/cpmtools/%{name}-%{version}.tar.gz
# Source0-md5:	43bbca6c5728e2aff298079cb0c00146
URL:		http://www.moria.de/~michael/cpmtools/
BuildRequires:	libdsk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
