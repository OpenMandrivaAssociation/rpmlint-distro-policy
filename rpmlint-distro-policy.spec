# (ngompa) disable rpmlint to avoid terrible cyclic dependency problem in rpm5->rpm4 + python2->python3 transition
# remove after rpm5->rpm4 transition is complete
%undefine _build_pkgcheck_set
%undefine _build_pkgcheck_srpm
%undefine _nonzero_exit_pkgcheck_terminate_build
###


Summary:	Rpmlint %{_target_vendor} policy
Name:		rpmlint-distro-policy
Version:	0.3.32
Release:	1
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
mkdir -p cp -a %{buildroot}%{_datadir}/rpmlint/config.d
cp -a %{SOURCE0} %{buildroot}%{rpmlint_config}/
cp -a %{SOURCE1} %{buildroot}%{rpmlint_config}/
cp -a %{SOURCE2} %{buildroot}%{rpmlint_config}/

%files
%{_datadir}/rpmlint/config.d/*
