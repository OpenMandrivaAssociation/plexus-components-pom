%global short_name plexus-components

Name:           %{short_name}-pom
Version:        14.2
Release:        1
Summary:        Plexus Components POM
Group:          Development/Java
BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	-N validate

License:        ASL 2.0
URL:            https://plexus.codehaus.org/%{short_name}
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  plexus-pom

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
