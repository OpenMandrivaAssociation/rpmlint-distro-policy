Name:		rpmlint-distro-policy
Version:	0.3.30
Release:	1
Summary:	Rpmlint %{_target_vendor} policy
Group:		Development/Other
License:	GPLv2+
URL:		%{disturl}
Source0:	distro.conf
Source1:	distro.error.list
BuildArch:	noarch
BuildRequires:	rpmlint
Requires:	rpmlint
%rename		rpmlint-mandriva-policy

%description
Official rpmlint %{vendor} policy, install this if you
want to produce RPMs for %{vendor}.

%prep

%build

%check
# (proyvind): disable check for when building with older naming...
test -f %{_datadir}/rpmlint/config.d/distro.conf || exit 0
PYTHONPATH=%{_datadir}/rpmlint python %{SOURCE0}

%install
install -m644 %{SOURCE0} -D %{buildroot}%{_datadir}/rpmlint/config.d/distro.conf
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/rpmlint/config.d/distro.error.list

%files
%{_datadir}/rpmlint/config.d/*
