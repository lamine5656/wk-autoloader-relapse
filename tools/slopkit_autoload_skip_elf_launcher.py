#!/usr/bin/env python3
"""Deprecated (0.2.14+): WKAL always sends elf-launcher.elf after JB.

install_home_icon skip (when version already installed) lives inside
elf-launcher itself via /data/elf-launcher/.home_icon_ver — not here.
This script is intentionally a no-op kept so older docs/scripts do not fail.
"""
import sys
print("slopkit_autoload_skip_elf_launcher: no-op (always-send since 0.2.14)")
raise SystemExit(0)
