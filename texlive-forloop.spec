Name:		texlive-forloop
Version:	3.0
Release:	1
Summary:	Iteration in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/forloop
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a command \forloop for doing iteration in
LaTeX macro programming.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/forloop/forloop.sty
%doc %{_texmfdistdir}/doc/latex/forloop/README
%doc %{_texmfdistdir}/doc/latex/forloop/forloop.pdf
#- source
%doc %{_texmfdistdir}/source/latex/forloop/forloop.dtx
%doc %{_texmfdistdir}/source/latex/forloop/forloop.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}