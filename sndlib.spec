%define	name		sndlib
%define	version		18
%define	rel		4
%define	release		%mkrel %{rel}
%define	lib_name_orig	lib%{name}
%define	lib_name        %mklibname %{name}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:	%{name}.tar.bz2
License:	LGPL
Group:		System/Libraries
URL:		http://www-ccrma.stanford.edu/software/snd/sndlib/
Summary:	SndLib is a library of sound-related functions
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	gsl-devel ladspa-devel lesstif-devel xpm-devel guile-devel
BuildRequires: 	gettext alsa-lib-devel XFree86-devel gtk+-devel = 1.2.10 glibc-static-devel

%description
The sound library is a collection of sound file and audio hardware
handlers written in C, Forth, Scheme, Common Lisp, and Ruby, and
running currently on SGI, Sun, Linux, Mac, HPUX, LinuxPPC, Mac OSX,
and Windoze systems (but I'm not making any effort to keep the Windoze
code going). It provides relatively straightforward access to many
sound file headers and data types, and most of the features of the
audio hardware.

%package -n	%{lib_name}-devel
Summary:	Development tools for %name
Group:		Development/C++
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
The sound library is a collection of sound file and audio hardware
handlers written in C, Forth, Scheme, Common Lisp, and Ruby, and
running currently on SGI, Sun, Linux, Mac, HPUX, LinuxPPC, Mac OSX,
and Windoze systems (but I'm not making any effort to keep the Windoze
code going). It provides relatively straightforward access to many
sound file headers and data types, and most of the features of the
audio hardware.

%package -n	%{lib_name}-static-devel
Summary:	sndlib static library
Group:		Development/C++
Requires:	%{lib_name}-devel = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
%name static library.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC" \
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#multiarch
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/%{name}-config

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README.sndlib HISTORY.sndlib sndins/README
%{_bindir}/%{name}-config
%multiarch %{multiarch_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%files -n %{lib_name}-static-devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.a
