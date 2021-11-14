%global pypi_name check-manifest
%define altpypi_name check_manifest
%bcond_with python2

Name:           python-%{pypi_name}
Version:	0.47
Release:	1
Group:          Development/Python
Summary:        Easy update of MANIFEST.in

License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source0:	https://files.pythonhosted.org/packages/06/bf/19135a8e930f6d7fd3049a34ae5316c7870b0badd14f07dd53ba58c2bf93/check-manifest-0.47.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
 
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif 

%description
Tool for managing the python package manifest

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Easy update of MANIFEST.in.

%description -n python2-%{pypi_name}
Tool for managing the python package manifest
%endif 

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# generate html docs 
#sphinx-build -C docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%if %{with python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
# generate html docs 
#sphinx-build2 docs/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}
%endif 

%build
%py3_build

%if %{with python2}
pushd %{py2dir}
%{__python} setup.py build
popd
%endif 


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif 

%py3_install

%files
%doc CHANGES.rst README.rst LICENSE.rst
%{_bindir}/%{pypi_name}
%{python_sitelib}/%{altpypi_name}.py
%{python_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info
%{python_sitelib}/__pycache__/*

%if %{with python2}
%files -n python2-%{pypi_name}
%doc CHANGES.rst README.rst LICENSE.rst
%{python2_sitelib}/%{altpypi_name}.py
%{python2_sitelib}/%{altpypi_name}-%{version}-py?.?.egg-info
%endif 
