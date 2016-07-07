Name:           i3blocks
Version:        1.4
Release:        1%{?dist}
Summary:        highly flexible status line for the i3 window manager

License:        GPLv3
URL:            https://github.com/vivien/i3blocks
Source0:        %{name}-%{version}.tar.gz

BuildRequires: rubygem-ronn

%description
i3blocks is a highly flexible status line for the i3 window manager. It handles clicks, signals and language-agnostic user scripts.


%prep
%setup -q
sed -e 's|PREFIX=/usr/local|PREFIX=%{_prefix}|g' -i Makefile

%build
make clean all
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README.md
%{_bindir}/i3blocks
%config(noreplace) %{_sysconfdir}/*.conf
%{_libexecdir}/i3blocks/*
%{_mandir}/man1/i3blocks.1*


%changelog
* Mon Jul  4 2016 Matthew Oliver
- 
