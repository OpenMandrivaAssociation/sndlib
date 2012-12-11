%define	name		sndlib
# Version numbers are listed in HISTORY.sndlib. Look closely.
%define	version		20
# Take from the last change recorded in HISTORY.sndlib.
# Actually, they don't seem to be updating it reliably, so
# just go with today's date...
%define date		20120922
%define	rel		1
%define	release		1.%{date}.%{rel}
%define	lib_name_orig	lib%{name}
%define develname	%mklibname %{name} -d
%define staticname	%mklibname %{name} -s -d

Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}.tar.gz
License:	BSD-like
Group:		System/Libraries
URL:		http://www-ccrma.stanford.edu/software/snd/sndlib/
Summary:	Library of sound-related functions
BuildRequires: 	guile-devel
BuildRequires: 	pkgconfig(alsa)

%description
The sound library is a collection of sound file and audio hardware
handlers written in C, Forth, Scheme, Common Lisp, and Ruby, and
running currently on SGI, Sun, Linux, Mac, HPUX, LinuxPPC, Mac OSX,
and Windoze systems (but I'm not making any effort to keep the Windoze
code going). It provides relatively straightforward access to many
sound file headers and data types, and most of the features of the
audio hardware.

%package -n	%{develname}
Summary:	Development tools for %name
Group:		Development/C++
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The sound library is a collection of sound file and audio hardware
handlers written in C, Forth, Scheme, Common Lisp, and Ruby, and
running currently on SGI, Sun, Linux, Mac, HPUX, LinuxPPC, Mac OSX,
and Windoze systems (but I'm not making any effort to keep the Windoze
code going). It provides relatively straightforward access to many
sound file headers and data types, and most of the features of the
audio hardware.

%package -n	%{staticname}
Summary:	Sndlib static library
Group:		Development/C++
Requires:	%{develname} = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{staticname}
%name static library.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC" LDFLAGS="-ldl -lm" \
%configure2_5x --with-alsa
%make

%install
%makeinstall

#multiarch
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/%{name}-config

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.a

%files -n %{develname}
%defattr(-,root,root)
%doc README.sndlib HISTORY.sndlib sndins/README
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%multiarch %{multiarch_bindir}/%{name}-config


%changelog
* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 20-1.20070906.1mdv2008.1
+ Revision: 170551
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Adam Williamson <awilliamson@mandriva.com>
    - refresh tarball

* Fri Jul 20 2007 Adam Williamson <awilliamson@mandriva.com> 20-1.20070625.1mdv2008.0
+ Revision: 53983
- explicitly enable ALSA in build
- drop a bunch of bogus buildrequires
- spec clean
- improve versioning
- new release 20 (20070625)
- Import sndlib



* Fri May 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 18-4mdk
- multiarch
- %%mkrel

* Fri Jan 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 18-3mdk
- rebuild 

* Sat Dec 27 2003 Austin Acton <austin@linux.ca> 18-2mdk
- lib-devel doesn't require lib

* Sun Dec 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 18-1mdk
- initial release
