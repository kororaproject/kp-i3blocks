%global debug_package %{nil}

Name:           i3blocks
Version:        1.4
Release:        2%{?dist}
Summary:        highly flexible status line for the i3 window manager

License:        GPLv3
URL:            https://github.com/vivien/i3blocks
Source0:        https://github.com/vivien/i3blocks/releases/download/%{version}/i3blocks-%{version}.tar.gz

%description
i3blocks is a highly flexible status line for the i3 window manager. It handles clicks, signals and language-agnostic user scripts.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX="/usr"

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/i3blocks.conf
%{_bindir}/i3blocks
%{_libexecdir}/i3blocks/
%{_mandir}/man1/i3blocks.1*


%changelog
* Mon Oct  9 2017 Ian Firns <firnsy@kororaproject.org> - 1.4-2
- Updated to fetch source from upstream.

* Mon Jul  4 2016 Matthew Oliver
- initial package.
