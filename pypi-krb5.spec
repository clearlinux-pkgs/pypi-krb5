#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-krb5
Version  : 0.5.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/58/e3/50ce47968c1ae283b99410ebb6eaa595b2f016f35f15a9d11426db65ae3e/krb5-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/e3/50ce47968c1ae283b99410ebb6eaa595b2f016f35f15a9d11426db65ae3e/krb5-0.5.0.tar.gz
Summary  : Kerberos API bindings for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-krb5-filemap = %{version}-%{release}
Requires: pypi-krb5-lib = %{version}-%{release}
Requires: pypi-krb5-license = %{version}-%{release}
Requires: pypi-krb5-python = %{version}-%{release}
Requires: pypi-krb5-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : krb5-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Python Kerberos 5 Library
[![Test workflow](https://github.com/jborean93/pykrb5/actions/workflows/ci.yml/badge.svg)](https://github.com/jborean93/pykrb5/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/krb5.svg)](https://badge.fury.io/py/krb5)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jborean93/pykrb5/blob/main/LICENSE)

%package filemap
Summary: filemap components for the pypi-krb5 package.
Group: Default

%description filemap
filemap components for the pypi-krb5 package.


%package lib
Summary: lib components for the pypi-krb5 package.
Group: Libraries
Requires: pypi-krb5-license = %{version}-%{release}
Requires: pypi-krb5-filemap = %{version}-%{release}

%description lib
lib components for the pypi-krb5 package.


%package license
Summary: license components for the pypi-krb5 package.
Group: Default

%description license
license components for the pypi-krb5 package.


%package python
Summary: python components for the pypi-krb5 package.
Group: Default
Requires: pypi-krb5-python3 = %{version}-%{release}

%description python
python components for the pypi-krb5 package.


%package python3
Summary: python3 components for the pypi-krb5 package.
Group: Default
Requires: pypi-krb5-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(krb5)

%description python3
python3 components for the pypi-krb5 package.


%prep
%setup -q -n krb5-0.5.0
cd %{_builddir}/krb5-0.5.0
pushd ..
cp -a krb5-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676920576
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-krb5
cp %{_builddir}/krb5-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-krb5/8a44655c77dbb71243a0df4c3acc932bdd73e4fb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-krb5

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-krb5/8a44655c77dbb71243a0df4c3acc932bdd73e4fb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
