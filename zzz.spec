Summary:	A simple program to suspend or hibernate your computer
Name:		zzz
Version:	0.1.1
Release:	1
License:	MIT
Group:		System/Configuration/Hardware
Url:		https://github.com/jirutka/zzz
Source0:	https://github.com/jirutka/zzz/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	asciidoctor

%description
A simple program to suspend or hibernate your computer. It supports hooks
before and after suspending.

%files
%license LICENSE
%doc README.adoc
%config(noreplace) %{_sysconfdir}/zzz.d/
%{_bindir}/*
%{_mandir}/man8/*

%prep
%autosetup -p1

%build
%set_build_flags
export CFLAGS="%{optflags} -DZZZ_LOCK_FILE='\"/run/zzz.lock\"'"
%make_build

%install
%make_install prefix=/usr sbindir=/usr/bin

