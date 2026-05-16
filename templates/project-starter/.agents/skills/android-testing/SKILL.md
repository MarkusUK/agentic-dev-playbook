---
name: android-testing
description: Run or plan Android unit, lint, build, emulator, and instrumentation testing from the terminal.
---

# Android Testing Skill

Use terminal-first Android workflows. VS Code is not required.

## Common commands

List AVDs:

```bash
emulator -list-avds
```

Start an emulator:

```bash
emulator -avd <AVD_NAME>
```

Check devices:

```bash
adb devices
```

Build debug APK:

```bash
./gradlew assembleDebug
```

Run unit tests:

```bash
./gradlew test
```

Run lint:

```bash
./gradlew lint
```

Run connected tests:

```bash
./gradlew connectedAndroidTest
```

View logs:

```bash
adb logcat
```

## Workflow

1. Run unit tests first.
2. Build the debug APK.
3. Start emulator if connected tests are needed.
4. Confirm with `adb devices`.
5. Run `connectedAndroidTest`.
6. Report failures with relevant stack traces and next steps.
