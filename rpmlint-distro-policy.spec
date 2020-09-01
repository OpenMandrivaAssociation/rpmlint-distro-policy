Summary:	Rpmlint %{_target_vendor} policy
Name:		rpmlint-distro-policy
Version:	0.3.32
Release:	4
Group:		Development/Other
License:	GPLv2+
URL:		%{disturl}
Source0:	distribution.exceptions.conf
Source1:	distribution.error.conf
Source2:	distribution.error.list
BuildArch:	noarch
BuildRequires:	rpmlint >= 1.10
BuildRequires:	python >= 3
Requires:	rpmlint >= 1.10
Provides:	rpmlint-%{_target_vendor}-policy = %{EVRD}
%rename		rpmlint-mandriva-policy

%description
Official rpmlint %{vendor} policy, install this if you
want to produce RPMs for %{vendor}.

%prep
# nothing to do

%build
# nothing to do

%check
# prevent upload with a wrong config file
export PYTHONPATH=/usr/share/rpmlint
# this need some work, as this requires rpmlint-mageia-policy to be present to work fully
#python %{SOURCE1}
python %{SOURCE0}

%install
mkdir -p  %{buildroot}%{_datadir}/rpmlint/config.d
cp -a %{SOURCE0} %{buildroot}%{_datadir}/rpmlint/config.d/
cp -a %{SOURCE1} %{buildroot}%{_datadir}/rpmlint/config.d/
cp -a %{SOURCE2} %{buildroot}%{_datadir}/rpmlint/config.d/

%files
%{_datadir}/rpmlint/config.d/*
