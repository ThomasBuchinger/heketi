%if 0%{?fedora}
%global with_devel 1
%global with_python 1
%global with_bundled 1
%global with_debug 0
# there is a race in the test-cases:
# https://github.com/heketi/heketi/issues/1468
%global with_check 0
%global with_unit_test 1
%else
%global with_devel 0
%global with_python 0
%global with_bundled 1
%global with_debug 0
%global with_check 1
%global with_unit_test 0
%endif

# Determine if systemd will be used
%if ( 0%{?fedora} && 0%{?fedora} > 16 ) || ( 0%{?rhel} && 0%{?rhel} > 6 )
%global with_systemd 1
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         heketi
%global repo            heketi
# https://github.com/heketi/heketi
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           %{repo}
Version:        9.0.0
Release:        6%{?dist}
Summary:        RESTful based volume management framework for GlusterFS
License:        LGPLv3+ and GPLv2
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://%{provider_prefix}/releases/download/v%{version}/%{name}-deps-v%{version}.tar.gz
Source2:        %{name}.json
Source3:        %{name}.service
Source4:        %{name}.initd

%description
ODO



%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
