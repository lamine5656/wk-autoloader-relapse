#!/usr/bin/env python3
"""Register elf-launcher.elf as a hidden WKAL PAYLOADS entry (like payload.elf).

Without this, sendPayloadToElfldr('elf-launcher.elf') throws
'payload is not listed in this menu' and WKAL reports jailbreak failed.
"""
import sys
from pathlib import Path

OLD = (
    '    { title: "WKAL autoload", description: "", name: "payload.elf",\n'
    '        info: "payload.elf", hidden: true }'
)
NEW = (
    '    { title: "WKAL autoload", description: "", name: "payload.elf",\n'
    '        info: "payload.elf", hidden: true },\n'
    '    { title: "WKAL autoload elf-launcher", description: "", name: "elf-launcher.elf",\n'
    '        info: "elf-launcher.elf", hidden: true }'
)


def patch_file(path: Path) -> bool:
    t = path.read_text()
    if 'name: "elf-launcher.elf"' in t:
        print(f"already listed: {path}")
        return False
    if OLD not in t:
        print(f"WARN: WKAL payload.elf tile not found in {path}", file=sys.stderr)
        return False
    path.write_text(t.replace(OLD, NEW, 1))
    print(f"listed elf-launcher: {path}")
    return True


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    for name in ("poops.html", "p2jb.html"):
        paths = [root / name] if (root / name).is_file() else list(root.rglob(name))
        for path in paths:
            if "slopkit" in str(path):
                patch_file(path)


if __name__ == "__main__":
    main()
