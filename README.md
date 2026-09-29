# WK Autoloader

PS5 homebrew: jailbreak UI on port **1022**. Chains: **umtx2** (1–5.xx), **relapse** (7.00–13.60).

Current release: **[v1.0.1](https://github.com/X-F1REBALL-X/wk-autoloader-relapse/releases/tag/v1.0.1)** — download `installer.elf`.

## Screenshots

<table>
  <tr>
    <td align="center" width="50%">
      <img src="docs/screenshots/01-splash.jpg" alt="Splash — home screen" width="100%" /><br/>
      <sub><b>Splash</b> — home screen</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/screenshots/02-progress.jpg" alt="Progress — jailbreak running" width="100%" /><br/>
      <sub><b>Progress</b> — jailbreak running</sub>
    </td>
  </tr>
</table>

## Use

1. Download `installer.elf` from **[v1.0.1](https://github.com/X-F1REBALL-X/wk-autoloader-relapse/releases/tag/v1.0.1)**.
2. Send it to elfldr (`9021`).
3. Open the home icon or `http://PS5_IP:1022`.
4. Pick **Payload Manager** (`:8084`) or **Elf Launcher** (`:1000`), then **Start Jailbreak**.

## Elf Launcher

For downloading and sending `elf-launcher.elf` via BinLoader (`elfldr`) on port `9021`, see the [Elf Launcher repository](https://github.com/X-F1REBALL-X/elf-launcher) and its [releases](https://github.com/X-F1REBALL-X/elf-launcher/releases). It is the companion UI bundled with WK Autoloader for loading ELF payloads.

## Firmware

| FW | Chain |
|----|-------|
| 1.xx–5.xx | umtx2 |
| 6.xx | unsupported |
| 7.00–13.60 | relapse |

## Credits

**Ohad / X-F1REBALL-X** — packaging, routing, UI.

### umtx2 (1.xx–5.xx)

[idlesauce/umtx2](https://github.com/idlesauce/umtx2): exploit largely from @shahrilnet / @n0llptr (lua UMTX); setup from @SpecterDev / @ChendoChap ([PS5-UMTX-Jailbreak](https://github.com/PS5Dev/PS5-UMTX-Jailbreak/)); PSFree by abc; ELF loader by @john-tornblom.

### Relapse (7.00–13.60)

ntfargo, ufm42, Sonic_Iso, Jordy, Dr. Yenyen, TheFlow, SlidyBat, Flatz, cow, nhk, bollarz, Sleirsgoevy, EchoStretch, EarthOnion

## Build

```bash
./tools/download_deps.sh
make clean all          # needs PS5 SDK at /opt/ps5-payload-sdk
# or: ./build_release.sh  # Docker
```
