%global srcname trello-wrapper

Name: Trello-Unofficial
Version: 0.0.0
Release: 0%{?dist}
License: GPLv3
Summary: A Trello wrapper using electron
Url: https://pagure.io/%{srcname}

# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: x86_64

%if 0%{?el6}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
BuildRequires: npm
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: npm
%endif

%description
This is the copr spec file for building automatically Trello wrapper

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
electron-builder build

%install
mkdir %{_buildrootdir}/%{name}-%{version}/rpm_result
cp dist/*.rpm %{_buildrootdir}/rpm_result/out.rpm

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
#%{_bindir}/hellocopr
/rpm_result/out.rpm

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
