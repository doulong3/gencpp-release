Name:           ros-kinetic-gencpp
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS gencpp package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-genmsg
BuildRequires:  ros-kinetic-catkin >= 0.5.78
BuildRequires:  ros-kinetic-genmsg

%description
C++ ROS message and service generators.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Feb 08 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.0-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.5-0
- Autogenerated by Bloom

* Mon Mar 14 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.4-0
- Autogenerated by Bloom

* Wed Mar 09 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.3-0
- Autogenerated by Bloom

