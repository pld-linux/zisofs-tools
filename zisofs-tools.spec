Summary: Utilities to create compressed CD-ROM filesystems.
Name: zisofs-tools
Version: 1.0.3
Release: 3
License: GPL
Group: Applications/System
URL: http://www.kernel.org/pub/linux/utils/fs/zisofs/
Source: http://www.kernel.org/pub/linux/utils/fs/zisofs/zisofs-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Tools that, in combination with an appropriately patched version of
mkisofs, allow the creation of compressed CD-ROM filesystems.

%prep
%setup -q 

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALLROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README zisofs.magic
%{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*

%changelog
* Sat Feb 23 2002 Mike A. Harris <mharris@redhat.com> 1.0.3-3
- Rebuilt with new build toolchain

* Tue Feb  5 2002 Mike A. Harris <mharris@redhat.com> 1.0.3-2
- Initial Red Hat build for incorporation into distribution

* Thu Nov  8 2001 H. Peter Anvin <hpa@zytor.com> 1.0.3
- Revision update.

* Mon Oct 29 2001 H. Peter Anvin <hpa@zytor.com> 1.0.2
- Initial version.
