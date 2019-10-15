# Created by pyp2rpm-2.0.0
%global pypi_name check_manifest
%define tarname	check-manifest
%global with_python2 0

Name:           python-%{pypi_name}
Version:	0.40
Release:	1
Group:          Development/Python
Summary:        Easy update of MANIFEST.in.Easy update of MANIFEST.in.

License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source0:	https://files.pythonhosted.org/packages/10/2a/71cf4f24856ecef4a86be5b90591fcfb490adef38c424f6e7698af4269bb/check-manifest-0.40.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
 
%if %{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
%endif # if with_python2


%description
Tool for managing the python package manifest

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        Easy update of MANIFEST.in.

%description -n python2-%{pypi_name}
Tool for managing the python package manifest
%endif # with_python2


%prep
%setup -q -n %{tarname}-%{version}
# Remove bundled egg-info
rm -rf %{tar_name}.egg-info

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

%endif # with_python2


%build
%{__python} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python} setup.py build
popd
%endif # with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES.rst README.rst LICENSE.rst
%{_bindir}/%{tarname}
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/*
%{python_sitelib}/__pycache__/*
%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc CHANGES.rst README.rst LICENSE.rst
%{python2_sitelib}/%{pypi_name}.py
%{python2_sitelib}/%{tarname}-%{version}-py?.?.egg-info/*
%endif # with_python2

