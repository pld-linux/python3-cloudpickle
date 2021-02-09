#
# Conditional build:
%bcond_with	tests	# unit tests (some incompatible with python2, few failing on python3.8)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Extended pickling support for Python objects
Summary(pl.UTF-8):	Rozszerzona obsługa operacji pickle dla obiektów pythonowych
Name:		python-cloudpickle
# keep 1.3.x here for python2 support
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cloudpickle/
Source0:	https://files.pythonhosted.org/packages/source/c/cloudpickle/cloudpickle-%{version}.tar.gz
# Source0-md5:	625d9c80e1b4f2a3dea01f1b4c149511
URL:		https://pypi.org/project/cloudpickle/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-numpy
BuildRequires:	python-pytest
BuildRequires:	python-scipy
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-numpy
BuildRequires:	python3-pytest
BuildRequires:	python3-scipy
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-cloudpickle
Summary:	Extended pickling support for Python objects
Summary(pl.UTF-8):	Rozszerzona obsługa operacji pickle dla obiektów pythonowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-cloudpickle
cloudpickle makes it possible to serialize Python constructs not
supported by the default pickle module from the Python standard
library.

cloudpickle is especially useful for cluster computing where Python
code is shipped over the network to execute on remote hosts, possibly
close to the data.

Among other things, cloudpickle supports pickling for lambda functions
along with functions and classes defined interactively in the __main__
module (for instance in a script, a shell or a Jupyter notebook).

%description -n python3-cloudpickle -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/cloudpickle
%{py_sitescriptdir}/cloudpickle-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cloudpickle
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/cloudpickle
%{py3_sitescriptdir}/cloudpickle-%{version}-py*.egg-info
%endif
