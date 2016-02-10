%global _version 2.2.3


Name:           pg_partman
Version:        %{_version}
Release:        1%{?dist}
Summary:	pg_partman is an extension to create and manage both time-based and serial-based table partition sets

Group:          Development/Tools
License:	pg_partman is released under the PostgreSQL License, a liberal Open Source license, similar to the BSD or MIT licenses.
URL:            https://github.com/keithf4/pg_partman
Source:         https://github.com/keithf4/pg_partman/archive/master.tar.gz
Obsoletes:      pg_partman <= 2.2.3
Provides:       pg_partman => 2.2.3


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

make

###############################################################################################################################################################
%install
#mkdir -p %{buildroot}/etc/profile.d
#echo "export PATH=$PATH:%{pg_dir}/bin/" >> %{buildroot}/etc/profile.d/pg_partman.sh
#echo "export USE_PGXS=1" >> %{buildroot}/etc/profile.d/pg_partman.sh
#source %{buildroot}/etc/profile.d/pg_partman.sh

%make_install


###############################################################################################################################################################
%files
%{pg_dir}/bin/check_unique_constraint.py
%{pg_dir}/bin/dump_partition.py
%{pg_dir}/bin/partition_data.py
%{pg_dir}/bin/reapply_constraints.py
%{pg_dir}/bin/reapply_foreign_keys.py
%{pg_dir}/bin/reapply_indexes.py
%{pg_dir}/bin/undo_partition.py
%{pg_dir}/lib/pg_partman_bgw.so
%{pg_dir}/share/extension/pg_partman--0.1.0--0.1.1.sql
%{pg_dir}/share/extension/pg_partman--0.1.1--0.1.2.sql
%{pg_dir}/share/extension/pg_partman--0.1.2--0.2.0.sql
%{pg_dir}/share/extension/pg_partman--0.2.0--0.3.0.sql
%{pg_dir}/share/extension/pg_partman--0.3.0--0.3.1.sql
%{pg_dir}/share/extension/pg_partman--0.3.1--0.3.2.sql
%{pg_dir}/share/extension/pg_partman--0.3.2--0.4.0.sql
%{pg_dir}/share/extension/pg_partman--0.4.0--0.4.1.sql
%{pg_dir}/share/extension/pg_partman--0.4.1--0.4.2.sql
%{pg_dir}/share/extension/pg_partman--0.4.2--1.0.0.sql
%{pg_dir}/share/extension/pg_partman--1.0.0--1.1.0.sql
%{pg_dir}/share/extension/pg_partman--1.1.0--1.2.0.sql
%{pg_dir}/share/extension/pg_partman--1.2.0--1.3.0.sql
%{pg_dir}/share/extension/pg_partman--1.3.0--1.4.0.sql
%{pg_dir}/share/extension/pg_partman--1.4.0--1.4.1.sql
%{pg_dir}/share/extension/pg_partman--1.4.1--1.4.2.sql
%{pg_dir}/share/extension/pg_partman--1.4.2--1.4.3.sql
%{pg_dir}/share/extension/pg_partman--1.4.3--1.4.4.sql
%{pg_dir}/share/extension/pg_partman--1.4.4--1.4.5.sql
%{pg_dir}/share/extension/pg_partman--1.4.5--1.5.0.sql
%{pg_dir}/share/extension/pg_partman--1.5.0--1.5.1.sql
%{pg_dir}/share/extension/pg_partman--1.5.1--1.6.0.sql
%{pg_dir}/share/extension/pg_partman--1.6.0--1.6.1.sql
%{pg_dir}/share/extension/pg_partman--1.6.1--1.7.0.sql
%{pg_dir}/share/extension/pg_partman--1.7.0--1.7.1.sql
%{pg_dir}/share/extension/pg_partman--1.7.1--1.7.2.sql
%{pg_dir}/share/extension/pg_partman--1.7.2--1.8.0.sql
%{pg_dir}/share/extension/pg_partman--1.8.0--1.8.1.sql
%{pg_dir}/share/extension/pg_partman--1.8.1--1.8.2.sql
%{pg_dir}/share/extension/pg_partman--1.8.2--1.8.3.sql
%{pg_dir}/share/extension/pg_partman--1.8.3--1.8.4.sql
%{pg_dir}/share/extension/pg_partman--1.8.4--1.8.5.sql
%{pg_dir}/share/extension/pg_partman--1.8.5--1.8.6.sql
%{pg_dir}/share/extension/pg_partman--1.8.6--1.8.7.sql
%{pg_dir}/share/extension/pg_partman--1.8.7--1.8.8.sql
%{pg_dir}/share/extension/pg_partman--1.8.7--2.0.0.sql
%{pg_dir}/share/extension/pg_partman--1.8.8--2.0.0.sql
%{pg_dir}/share/extension/pg_partman--2.0.0--2.1.0.sql
%{pg_dir}/share/extension/pg_partman--2.1.0--2.2.0.sql
%{pg_dir}/share/extension/pg_partman--2.2.0--2.2.1.sql
%{pg_dir}/share/extension/pg_partman--2.2.1--2.2.2.sql
%{pg_dir}/share/extension/pg_partman--2.2.2--2.2.3.sql
%{pg_dir}/share/extension/pg_partman--2.2.3.sql
%{pg_dir}/share/extension/pg_partman.control
/usr/share/doc/pgsql/extension/pg_partman.md
/usr/share/doc/pgsql/extension/pg_partman_howto.md
