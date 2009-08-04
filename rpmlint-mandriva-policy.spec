%define rpmlint_config %{_datadir}/rpmlint/config.d/

Name:           rpmlint-mandriva-policy
Version:        0.2.2
Release:        %mkrel 1
Summary:        Rpmlint mandriva policy
Group:          Development/Other
License:        GPLv2+
URL:            http://wiki.mandriva.com/
Source0:        mandriva.conf
Source1:        mandriva.error.list
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:       rpmlint
%description
Official rpmlint mandriva policy, install this if you want to 
produces rpm for mandriva.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/%rpmlint_config
cp -a %{SOURCE0} %{buildroot}/%rpmlint_config/
cp -a %{SOURCE1} %{buildroot}/%rpmlint_config/

%files
%defattr(-,root,root,-)
%rpmlint_config/*
