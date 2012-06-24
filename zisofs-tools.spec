Summary:	Utilities to create compressed CD-ROM filesystems
Summary(pl):	Narz�dzia do tworzenia skompresowanych system�w plik�w na CD-ROM
Name:		zisofs-tools
Version:	1.0.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/utils/fs/zisofs/%{name}-%{version}.tar.gz
# Source0-md5:	feb9e86dddf8cac6a649afbbcc0fe9d2
URL:		http://www.kernel.org/pub/linux/utils/fs/zisofs/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools that, in combination with an appropriate version mkisofs, allow
the creation of compressed CD-ROM filesystems.

%description -l pl
S� to programy narz�dziowe, kt�re przy przy wykorzystaniu odpowiedniej
wersji mkisofs, umo�liwiaj� tworzenie skompresowanych system�w plik�w
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
