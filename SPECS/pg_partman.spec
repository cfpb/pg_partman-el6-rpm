%global _version 2.2.3


Name:           pg_partman%{_suffix}
Version:        %{_version}
Release:        1%{?dist}
Summary:	pg_partman is an extension to create and manage both time-based and serial-based table partition sets

Group:          Development/Tools
License:	pg_partman is released under the PostgreSQL License, a liberal Open Source license, similar to the BSD or MIT licenses.
URL:            https://github.com/keithf4/pg_partman
Source:         https://github.com/keithf4/pg_partman/archive/master.tar.gz
Obsoletes:      pg_partman%{_suffix} <= 2.2.3
Provides:       pg_partman%{_suffix} = 2.2.3


%description
pg_partman is an extension to create and manage both time-based and serial-based table partition sets. 
Sub-partitoning is also supported. Child table & trigger function creation is all managed by the extension itself. 
Tables with existing data can also have their data partitioned in easily managed smaller batches. 
Optional retention policy can automatically drop partitions no longer needed. 
A background worker (BGW) process is included to automatically run partition maintenance without the need of an external scheduler (cron, etc) in most cases.

###############################################################################################################################################################
# Build requirements

BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)


###############################################################################################################################################################
#PREP and SETUP
# The prep directive removes existing build directory and extracts source code so we have a fresh code base .....-n flag where present, defines the name of the directory

%prep
%setup -n pg_partman-master


###############################################################################################################################################################
%build
CFLAGS="-O3 -Wall -Wno-format-security"
LDFLAGS="-pthread"

make %{?_smp_mflags}

###############################################################################################################################################################
%install

make install USE_PGXS=1 DESTDIR=${RPM_BUILD_ROOT}


###############################################################################################################################################################
%files
%{pg_dir}
%{pg_dir}/bin/dump_partition.py
