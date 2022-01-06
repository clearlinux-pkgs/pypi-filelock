#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-filelock
Version  : 3.4.2
Release  : 32
URL      : https://files.pythonhosted.org/packages/11/d1/22318a1b5bb06c9be4c065ad6a09cb7bfade737758dc08235c99cd6cf216/filelock-3.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/d1/22318a1b5bb06c9be4c065ad6a09cb7bfade737758dc08235c99cd6cf216/filelock-3.4.2.tar.gz
Summary  : A platform independent file lock.
Group    : Development/Tools
License  : Unlicense
Requires: pypi-filelock-license = %{version}-%{release}
Requires: pypi-filelock-python = %{version}-%{release}
Requires: pypi-filelock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: filelock
Provides: filelock-python
Provides: filelock-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# py-filelock
[![PyPI](https://img.shields.io/pypi/v/filelock?style=flat-square)](https://pypi.org/project/filelock/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/filelock.svg)](https://pypi.org/project/filelock/)
[![Documentation
status](https://readthedocs.org/projects/py-filelock/badge/?version=latest&style=flat-square)](https://py-filelock.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock/month)
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
%setup -q -n filelock-3.4.2
cd %{_builddir}/filelock-3.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641435458
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-filelock
cp %{_builddir}/filelock-3.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-filelock/24944bf7920108f5a4790e6071c32e9102760c37
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
