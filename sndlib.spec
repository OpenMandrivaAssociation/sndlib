%define	name		sndlib
# Version numbers are listed in HISTORY.sndlib. Look closely.
%define	version		20
# Take from the last change recorded in HISTORY.sndlib.
# Actually, they don't seem to be updating it reliably, so
# just go with today's date...
%define date		20070906
%define	rel		1
%define	release		%mkrel 1.%{date}.%{rel}
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
Summary:	SndLib is a library of sound-related functions
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	guile-devel
BuildRequires: 	alsa-lib-devel

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
Summary:	sndlib static library
Group:		Development/C++
Requires:	%{develname} = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{staticname}
%name static library.

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC" \
%configure2_5x --with-alsa
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#multiarch
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/%{name}-config

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{develname}
%defattr(-,root,root)
%doc README.sndlib HISTORY.sndlib sndins/README
%{_bindir}/%{name}-config
%multiarch %{multiarch_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.a
