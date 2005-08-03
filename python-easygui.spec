%define		module	easygui
Summary:	EasyGUI is a module for very simple, very easy GUI programming
Summary(pl):	Pakiet GUI dla Pythona
Name:		python-%{module}
Version:	0.72
Release:	1
License:	CCA v2.0
Group:		Libraries/Python
Source0:	http://www.ferg.org/easygui/easygui.zip
# Source0-md5:	32aefe99d98aaea41576038da0513e07
URL:		http://www.ferg.org/easygui/
BuildRequires:	python-devel >= 2.2
%pyrequires_eq	python-modules
Requires:	python-tkinter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Experienced Pythonistas need support for quick and dirty GUI features.
New Python programmers need GUI capabilities that don't require any
knowledge of Tkinter, frames, widgets, callbacks or lambda. This is
what EasyGUI provides. Using EasyGUI, all GUI interactions are invoked
by simple function calls.

EasyGUI is different from other GUIs in that EasyGUI is NOT
event-driven. It allows you to program in a traditional linear
fashion, and to put up dialogs for simple input and output when you
need to. If you have not yet learned the event-driven paradigm for GUI
programming, EasyGUI will allow you to be productive with very basic
tasks immediately.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

install easygui.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{py_sitescriptdir}/*.py[co]
