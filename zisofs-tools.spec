Summary:	Utilities to create compressed CD-ROM filesystems
Summary(pl):	Narzêdzia do tworzenia skompresowanych systemów plików na CD-ROM
Name:		zisofs-tools
Version:	1.0.3
Release:	3
License:	GPL
Group:		Applications/System
URL:		http://www.kernel.org/pub/linux/utils/fs/zisofs/
Source0:	http://www.kernel.org/pub/linux/utils/fs/zisofs/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools that, in combination with an appropriately patched version of
mkisofs, allow the creation of compressed CD-ROM filesystems.

%description -l pl

S± to programy narzêdziowe, które przy przy wykorzystaniu odpowiednio
przygotowanej wersji mkisofs, umo¿liwiaj± tworzenie skompresowanych
systemów plików na CD-ROM.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALLROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README zisofs.magic
%attr(755,root,root) %{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*
