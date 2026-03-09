%global module check-manifest
%define oname check_manifest
%bcond tests 1

Name:		python-check-manifest
Version:	0.51
Release:	1
License:	MIT
Summary:	Tool to check the completeness of MANIFEST.in for Python packages
Group:		Development/Python
URL:		https://github.com/mgedmin/check-manifest
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(sphinx)
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(wheel)
%endif

%description
Tool to check the completeness of MANIFEST.in for Python packages.

%prep
%autosetup -n %{module}-%{version} -p1

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.rst
%license LICENSE.rst
%{_bindir}/%{module}
%{python_sitelib}/%{oname}.py
%{python_sitelib}/%{oname}-%{version}-py%{pyver}.egg-info
