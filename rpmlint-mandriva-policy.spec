%define rpmlint_config %{_datadir}/rpmlint/config.d/

Name:           rpmlint-mandriva-policy
Version:        0.3.8
Release:        1
Summary:        Rpmlint mandriva policy
Group:          Development/Other
License:        GPLv2+
URL:            http://wiki.mandriva.com/
Source0:        mandriva.conf
Source1:        mandriva.error.list
BuildArch:      noarch
Requires:       rpmlint

%description
Official rpmlint Mandriva policy, install this if you want to  produce RPMs
for Mandriva.

%prep

%build

%install
install -m644 %{SOURCE0} -D %{buildroot}%{rpmlint_config}/mandriva.conf
install -m644 %{SOURCE1} -D %{buildroot}%{rpmlint_config}/mandriva.error.list

%files
%{rpmlint_config}/*
