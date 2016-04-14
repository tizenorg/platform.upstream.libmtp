%define _unpackaged_files_terminate_build 0

Name:       libmtp
Summary:    Library for media transfer protocol (mtp)
Version:    1.1.11
Release:    1
Group:      Network & Connectivity/Other
License:    LGPL-2.1
Source0:    libmtp-%{version}.tar.gz

ExcludeArch: %ix86 x86_64

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(libexif)
BuildRequires: libtool-ltdl-devel
BuildRequires: gettext-devel

%description
Libmtp support media transfer protocol, role is initiator
This package contains the library.


%package devel
Summary:    libmtp development package
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS+=" -fPIC -DTIZEN_EXT -flto"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=%{_libdir}"
%autogen
%configure --prefix=/usr --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest libmtp.manifest
%defattr(-,root,root,-)
%{_libdir}/libmtp.so*
/lib/udev/rules.d/69-libmtp.rules

%files devel
%defattr(-,root,root,-)
%{_libdir}/libmtp.so*
%{_libdir}/pkgconfig/libmtp.pc
/usr/include/*
/lib/udev/mtp-probe
/usr/bin/mtp-hotplug
