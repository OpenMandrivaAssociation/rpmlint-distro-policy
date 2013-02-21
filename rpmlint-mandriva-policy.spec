Name:		rpmlint-mandriva-policy
Version:	0.3.27
Release:	1
Summary:	Rpmlint %{_target_vendor} policy
Group:		Development/Other
License:	GPLv2+
URL:		http://wiki.mandriva.com/
Source0:	mandriva.conf
Source1:	mandriva.error.list
BuildArch:	noarch
BuildRequires:	rpmlint
Requires:	rpmlint

%description
Official rpmlint %{vendor} policy, install this if you want to produce RPMs
for %{vendor}.

%prep

%build

%check
PYTHONPATH=%{_datadir}/rpmlint python %{SOURCE0}

%install
install -m644 %{SOURCE0} -D %{buildroot}%{_datadir}/rpmlint/config.d/mandriva.conf
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/rpmlint/config.d/mandriva.error.list

%files
%{_datadir}/rpmlint/config.d/*
