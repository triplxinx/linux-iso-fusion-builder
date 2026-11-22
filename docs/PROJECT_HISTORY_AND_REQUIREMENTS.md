# Linux ISO Fusion Builder — History and requirements
## About
Cross-platform workbench for safely planning and eventually building customized Debian/Ubuntu-family live systems by importing compatible ISO/root filesystem components, analyzing package conflicts, customizing in an isolated workspace and exporting bootable media. Related existing repositories: studio-live-kit, studio-live-kit-workbench and custom-linux-build; do not duplicate or overwrite them.

## Revision history
- 2026-11-09: Ubuntu Studio-based live kit, GitHub Actions ISO builds, boot testing, wallpapers/splashes, categorized installable software, Wine/Android/web integration and browser choices.
- 2026-11-09–13: Requested desktop installer from running live OS, EFI/GPT/vfat recovery support, QEMU testing, GitHub-hosted artifacts, first-boot setup and portable update injection into Studio-Live-Kit v7.
- 2026-11-13: Requested 80 GiB+ workspace, selecting up to three compatible live Linux ISOs, package compatibility/category comparison, pulling components into new rootfs, chroot updates and export.
- 2026-11-13: Requested direct-install mode to virtually boot Debian-family live distro, customize from within and install to a dedicated partition.
- 2026-11-13: Requested Qt5, FLTK and bundled HTML/CSS/JS frontends with dedicated workflows, dialogs and walkthroughs; web Browse button reportedly nonfunctional.
- Additional requested features: Bedrock/Blend-OS-style isolation, package/source interoperability, chroot tooling, native Linux/Windows/Android/web launch categories, ASCII TTY interface via libcaca, compatibility and crash indicators.
- 2026-11-22: Separate public planning scaffold repo created; not a functional ISO compiler.

## Feature inventory
### Input, compatibility and workspace
- [ ] Host environment detection and safe tooling bootstrap, including immutable Linux hosts and Windows-supported preparation pathways.
- [ ] At least 80 GiB dedicated workspace, explicit disk/partition selection, non-destructive previews, backup warnings and privilege boundaries.
- [ ] Import 1–3 live ISOs of compatible distributions; verify hashes, signatures, architectures, base families, kernel/initrd/bootloader, package and licensing compatibility.
- [ ] Compare installed/installable software by category, show compatible/conflicting packages and dependencies, with a reproducible merge plan.
- [ ] Extract compatible filesystems into isolated rootfs, stage overlays and track provenance; controlled chroot/container updates and rollback.
### Build, boot and installation
- [ ] Export reproducible bootable live ISO, UEFI/BIOS boot paths, squashfs and bootloader assembly.
- [ ] GitHub Actions build artifacts and automated QEMU boot tests; optional supported online test environment.
- [ ] Direct-install workflow for Debian-family live distro customization and dedicated-partition installation with explicit destructive-action confirmation.
- [ ] EFI/GPT, vfat /boot, multiple EFI partitions, e2fsck/journal diagnostic and recovery guides; never auto-repair partitions without explicit consent.
- [ ] Incremental patch/injection into existing Studio-Live-Kit ZIP instead of mandatory full rebuild; first-boot autoinstall choices.
### UX and software catalog
- [ ] Qt5 desktop frontend, FLTK lightweight frontend and self-contained HTML/JS/CSS UI with working file picker.
- [ ] Guided setup, workflow buttons, status, dry-run preview, errors and help dialogs.
- [ ] TTY ASCII menu interface using libcaca, terminal input/status panes, configurable hotkeys and ranked green/unknown/crashed package status.
- [ ] Custom wallpapers/splash, OpenArtistHQ scripts, browser integration, WineHQ database references, Linux/Windows/Android/web app launch categories, Snap/Flatpak and isolated multi-distro package support.

## Verified current repository
Safe Python dry-run planning CLI with 1–3 ISO count and >=80 GiB checks, basic tests and roadmap. No disk modifications, ISO compilation, actual compatibility analysis, GUI or boot tests implemented.

## TODO
1. [ ] Audit studio-live-kit, studio-live-kit-workbench, custom-linux-build and prior ZIP sources; identify authoritative implementation.
2. [ ] Add read-only ISO inspection, hash/signature verification and compatibility matrix.
3. [ ] Design least-privilege workspace, isolation, rollback and confirmation model before partition/chroot operations.
4. [ ] Implement deterministic filesystem staging and package conflict resolution with reproducible manifests.
5. [ ] Implement bootable ISO assembly, UEFI/BIOS boot and QEMU CI validation.
6. [ ] Build Qt5, FLTK and HTML frontends, fix browse/file-picker workflow.
7. [ ] Add guarded direct installer, EFI diagnostics, incremental patch workflow and documentation.
8. [ ] Log verified implementation milestones in CHANGELOG.md.

## Historical integrity
Requirements reconstructed from accessible prompts. No claim that a feature is already built unless explicitly verified.
