Name:           intel-vision
Summary:        Metadata package for Intel vision drivers
Version:        2025112.WW46.3_25_ptl_pv
Release:        3%{?dist}
License:        GPL-2.0-or-later

URL:            https://github.com/intel/vision-drivers

BuildRequires:  systemd-rpm-macros
Provides:       intel-vision-kmod-common = %{version}
Requires:       kernel-uname-r > 6.16.12-200
Requires:       intel-vision-kmod

BuildArch:      noarch
ExclusiveArch:  x86_64


%description
This is the metadata package for Intel vision drivers.
Intel vision-drivers supports the Intel Lunar Lake (LNL) CVS-enabled Platforms.
It depends on
Intel LNL platform BIOS and CVS device
Intel LJCA USB driver, adding LNL GPIO PID (INTC10B5) support


%files


%changelog
* Tue Dec 30 2025 Kate Hsuan <hpa@redhat.com> - 2025112.WW46.3_25_ptl_pv-3
- Update kernel version dependency
- Update dependency

* Thu Nov 20 2025 Ben Matteson <bmatteso@us.ibm.com> - WW46.3_25_ptl_pv-2
- Update spec file

* Thu Oct 30 2025 Ben Matteson <bmatteso@us.ibm.com> - WW46.3_25_ptl_pv-1
- Update to WW46.3_25_ptl_pv
