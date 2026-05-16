# Testing Guide

Customise this file for each project.

## General testing expectations

Agents should run the smallest relevant test set first, then broader checks when needed.

Typical commands to customise:

```bash
npm test
npm run lint
npm run typecheck
npm run build
```

For Python:

```bash
pytest
ruff check .
mypy .
```

For Android/Gradle:

```bash
./gradlew test
./gradlew lint
./gradlew assembleDebug
./gradlew connectedAndroidTest
```

## Running an Android emulator from a terminal

Android AVDs can be started and controlled from any terminal as long as the Android SDK command-line tools (`emulator`, `adb`, `sdkmanager`) are installed and on your `PATH`. This is the recommended setup for agent workflows because the agent can drive the emulator with the same commands you would.

If `emulator` or `adb` is not found, check that `ANDROID_HOME` (or `ANDROID_SDK_ROOT`) is set and that `$ANDROID_HOME/emulator` and `$ANDROID_HOME/platform-tools` are on your `PATH`.

Common commands:

List available emulators:

```bash
emulator -list-avds
```

Start an emulator:

```bash
emulator -avd <AVD_NAME>
```

Start with a clean-ish boot option:

```bash
emulator -avd <AVD_NAME> -no-snapshot-load
```

Check connected devices:

```bash
adb devices
```

Install a debug APK:

```bash
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

Run connected Android tests:

```bash
./gradlew connectedAndroidTest
```

Run unit tests only:

```bash
./gradlew test
```

Build debug APK:

```bash
./gradlew assembleDebug
```

View logs:

```bash
adb logcat
```

Clear app data:

```bash
adb shell pm clear your.package.name
```

## Suggested Android agent workflow

1. Start on a feature branch.
2. Ask the agent to inspect the Android module structure.
3. Run local unit tests first:

```bash
./gradlew test
```

4. Build the debug app:

```bash
./gradlew assembleDebug
```

5. Start an emulator from terminal:

```bash
emulator -list-avds
emulator -avd <AVD_NAME>
```

6. Confirm device is connected:

```bash
adb devices
```

7. Run instrumentation tests:

```bash
./gradlew connectedAndroidTest
```

8. Ask Claude Code to review the diff before committing.

## Testing rules for agents

- Prefer targeted tests for changed code.
- Add regression tests for bug fixes.
- Do not remove failing tests to make a build pass.
- If tests fail, explain the failure.
- If tests cannot be run, explain why and list the exact command that should be run.
