#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)

Summary:	Extended pickling support for Python objects
Summary(pl.UTF-8):	Rozszerzona obsługa operacji pickle dla obiektów pythonowych
Name:		python3-cloudpickle
Version:	3.1.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cloudpickle/
Source0:	https://files.pythonhosted.org/packages/source/c/cloudpickle/cloudpickle-%{version}.tar.gz
# Source0-md5:	68ae8d8eea1c5ebd2fcfffe2c5259721
URL:		https://pypi.org/project/cloudpickle/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-numpy
BuildRequires:	python3-psutil
BuildRequires:	python3-pytest
BuildRequires:	python3-scipy
BuildRequires:	python3-tornado
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cloudpickle makes it possible to serialize Python constructs not
supported by the default pickle module from the Python standard
library.

cloudpickle is especially useful for cluster computing where Python
code is shipped over the network to execute on remote hosts, possibly
close to the data.

Among other things, cloudpickle supports pickling for lambda functions
along with functions and classes defined interactively in the __main__
module (for instance in a script, a shell or a Jupyter notebook).

%description -l pl.UTF-8
cloudpickle pozwala serializować konstrukcje pythonowe nie obsługiwane
domyślnie przez moduł pickle z biblioteki standardowej Pythona.

cloudpickle jest przydatne szczególnie przy obliczeniach klastrowych,
gdzie kod pythonowy jest rozmieszczony po sieci, aby wykonywał się na
zdalnych maszynach, możliwie blisko danych.

cloudpickle obsługuje m.in. operacje pickle na funkcjach lambda oraz
funkcjach lub klasach definiowanych interaktywnie w module __main__
(np. w skrypcie, z powłoki lub w postaci Jupyter notebook).

%prep
%setup -q -n cloudpickle-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd):$(pwd)/tests/cloudpickle_testpkg \
%{__python3} -m unittest tests/cloudpickle_test.py tests/cloudpickle_file_test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/cloudpickle
%{py3_sitescriptdir}/cloudpickle-%{version}.dist-info
