# Created by pyp2rpm-2.0.0
%global pypi_name check-manifest
%define altpypi_name check_manifest
%global with_python2 0

Name:           python-%{pypi_name}
Version:	0.45
Release:	3
Group:          Development/Python
Summary:        Easy update of MANIFEST.in.Easy update of MANIFEST.in.

License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source0:	https://files.pythonhosted.org/packages/ee/8d/1f98cb6bf7bbee73e3ba333c39c0dd4585a334d20b4c7ba658ca12007311/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
 
%if %{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif 
#if with_python2


%description
Tool for managing the python package manifest

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        Easy update of MANIFEST.in.

%description -n python2-%{pypi_name}
Tool for managing the python package manifest
%endif 
# with_python2


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
#sphinx-build -C docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
# generate html docs 
#sphinx-build2 docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%endif 
# with_python2


%build
%py3_build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python} setup.py build
popd
%endif 
# with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif 
# with_python2

%py3_install


%files
%doc CHANGES.rst README.rst LICENSE.rst
%{_bindir}/%{pypi_name}
%{python_sitelib}/%{altpypi_name}.py
%{python_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info/*
%{python_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info/PKG-INFO
%{python_sitelib}/__pycache__/*
%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc CHANGES.rst README.rst LICENSE.rst
%{python2_sitelib}/%{altpypi_name}.py
%{python2_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info/*
%{python2_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info/PKG-INFO
%endif 
# with_python2

