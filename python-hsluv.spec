%global pypi_name hsluv

Name:           python-%{pypi_name}
Version:        5.0.2
Release:        5
Summary:        Human-friendly HSL
License:        MIT
URL:            https://github.com/hsluv/hsluv-python
Source:         https://files.pythonhosted.org/packages/91/bf/6f819c811c2f6ed71e3cd619b66571850ef8e1fc13966b760c04d852ee97/hsluv-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Provides:	python-%{pypi_name} = %{EVRD}

%description
A Python implementation of HSLuv (revision 4).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/hsluv.py
%{python_sitelib}/%{pypi_name}-*.egg-info/
