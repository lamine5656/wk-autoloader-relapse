#!/usr/bin/env python3
"""Deprecated (0.2.14+): WKAL always sends elf-launcher.elf after JB.

install_home_icon skip lives inside elf-launcher; this script is a no-op.
"""
import sys
print("umtx2_autoload_skip_elf_launcher: no-op (always-send since 0.2.14)")
raise SystemExit(0)
