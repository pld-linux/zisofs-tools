Summary:	Utilities to create compressed CD-ROM filesystems
Summary(pl.UTF-8):	Narzędzia do tworzenia skompresowanych systemów plików na CD-ROM
Name:		zisofs-tools
Version:	1.0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/fs/zisofs/%{name}-%{version}.tar.gz
# Source0-md5:	0a31fc4ff1abcc42fcd20ec674d94466
URL:		http://www.kernel.org/pub/linux/utils/fs/zisofs/
BuildRequires:	autoconf
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools that, in combination with an appropriate version mkisofs, allow
the creation of compressed CD-ROM filesystems.

%description -l pl.UTF-8
Są to programy narzędziowe, które przy przy wykorzystaniu odpowiedniej
wersji mkisofs, umożliwiają tworzenie skompresowanych systemów plików
na CD-ROM.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALLROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*
