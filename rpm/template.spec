%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-depthai
Version:        2.26.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS depthai package

License:        MIT
URL:            https://www.luxonis.com/
Source0:        %{name}-%{version}.tar.gz

Requires:       json-devel
Requires:       libusbx-devel
Requires:       opencv-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  json-devel
BuildRequires:  libusbx-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ros-environment
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
DepthAI core is a C++ library which comes with firmware and an API to interact
with OAK Platform

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Jun 12 2024 Adam Serafin <adam.serafin@luxonis.com> - 2.26.1-1
- Autogenerated by Bloom

* Fri May 31 2024 Adam Serafin <adam.serafin@luxonis.com> - 2.26.0-1
- Autogenerated by Bloom

* Thu Mar 07 2024 Sachin Guruswamy <sachin@luxonis.com> - 2.24.0-1
- Autogenerated by Bloom

* Wed Nov 15 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.23.0-1
- Autogenerated by Bloom

* Thu Jun 15 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.22.0-1
- Autogenerated by Bloom

* Wed Apr 05 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.21.2-1
- Autogenerated by Bloom

* Mon Apr 03 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.21.0-1
- Autogenerated by Bloom

* Wed Feb 01 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.20.2-1
- Autogenerated by Bloom

* Sun Jan 29 2023 Sachin Guruswamy <sachin@luxonis.com> - 2.20.1-1
- Autogenerated by Bloom

* Mon Nov 28 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.19.1-1
- Autogenerated by Bloom

* Thu Nov 03 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.19.0-1
- Autogenerated by Bloom

* Thu Sep 22 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.17.4-1
- Autogenerated by Bloom

* Mon Sep 05 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.17.3-1
- Autogenerated by Bloom

* Tue Jul 12 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.17.0-1
- Autogenerated by Bloom

* Thu Jun 02 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.15.5-1
- Autogenerated by Bloom

* Wed May 25 2022 Sachin Guruswamy <sachin@luxonis.com> - 2.15.4-1
- Autogenerated by Bloom

