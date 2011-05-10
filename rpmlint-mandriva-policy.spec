%define rpmlint_config %{_datadir}/rpmlint/config.d/

Name:           rpmlint-mandriva-policy
Version:        0.2.6
Release:        6
Summary:        Rpmlint mandriva policy
Group:          Development/Other
License:        GPLv2+
URL:            http://wiki.mandriva.com/
Source0:        mandriva.conf
Source1:        mandriva.error.list
BuildArch:      noarch
Requires:       rpmlint

%description
Official rpmlint mandriva policy, install this if you want to 
produces rpm for mandriva.

%prep

%build

%install
install -m644 %{SOURCE0} -D %{buildroot}%{rpmlint_config}/mandriva.conf
install -m644 %{SOURCE1} -D %{buildroot}%{rpmlint_config}/mandriva.error.list

%files
%{rpmlint_config}/*
