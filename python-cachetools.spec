%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global pypi_name cachetools

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://github.com/tkem/cachetools
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Extensible memoizing collections and decorators

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Extensible memoizing collections and decorators
%endif
%description

This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library `@lru_cache`_
function decorator.

%prep
%setup -qc

mv %{pypi_name}-%{version} python2
pushd python2
cp -a LICENSE ..
cp -a README.rst ..
popd

%if 0%{?with_python3}
cp -a python2 python3
%endif

%build
pushd python2
%{__python2} setup.py build
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py build
popd
%endif # with_python3

%install
pushd python2
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%check
pushd python2
%{__python2} setup.py test
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py test
popd
%endif

%files
%doc README.rst 
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-.*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst 
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-.*-py?.?.egg-info
%endif


%changelog
