%global module hsluv
%bcond tests 1

Name:		python-hsluv
Version:	5.0.4
Release:	1
Summary:	Human-friendly HSL
License:	MIT
Group:		Development/Python
URL:		https://github.com/hsluv/hsluv-python
Source: 	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif
Provides:	python-%{module} = %{EVRD}

%description
A Python implementation of HSLuv (revision 4).

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.md
%license LICENSE.txt
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}*.*-info
