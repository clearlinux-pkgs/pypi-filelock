#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-filelock
Version  : 3.10.2
Release  : 54
URL      : https://files.pythonhosted.org/packages/f2/5e/b941f8db11ef0cebc50e27702930b1643232843275459ee443ba3d2bdcde/filelock-3.10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/f2/5e/b941f8db11ef0cebc50e27702930b1643232843275459ee443ba3d2bdcde/filelock-3.10.2.tar.gz
Summary  : A platform independent file lock.
Group    : Development/Tools
License  : Unlicense
Requires: pypi-filelock-license = %{version}-%{release}
Requires: pypi-filelock-python = %{version}-%{release}
Requires: pypi-filelock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# py-filelock
[![PyPI](https://img.shields.io/pypi/v/filelock)](https://pypi.org/project/filelock/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/filelock.svg)](https://pypi.org/project/filelock/)
[![Documentation
status](https://readthedocs.org/projects/py-filelock/badge/?version=latest)](https://py-filelock.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock)
[![check](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml)

%package license
Summary: license components for the pypi-filelock package.
Group: Default

%description license
license components for the pypi-filelock package.


%package python
Summary: python components for the pypi-filelock package.
Group: Default
Requires: pypi-filelock-python3 = %{version}-%{release}

%description python
python components for the pypi-filelock package.


%package python3
Summary: python3 components for the pypi-filelock package.
Group: Default
Requires: python3-core
Provides: pypi(filelock)

%description python3
python3 components for the pypi-filelock package.


%prep
%setup -q -n filelock-3.10.2
cd %{_builddir}/filelock-3.10.2
pushd ..
cp -a filelock-3.10.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679585107
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-filelock
cp %{_builddir}/filelock-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-filelock/24944bf7920108f5a4790e6071c32e9102760c37 || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-filelock/24944bf7920108f5a4790e6071c32e9102760c37

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
