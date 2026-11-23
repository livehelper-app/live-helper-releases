# Live Helper downloads

This is the home of the Live Helper installers for Mac and Windows. Here you can download the newest version and read how to install it.

## What is Live Helper?

Live Helper is a small floating window for macOS and Windows. It listens to a live session and streams short answers you can say out loud. The answers come from the setup and the profile you saved, so they sound like you and fit your situation.

It works in modes. Today there are two:

- **Interview.** Save the company, the role and the job description. Live Helper answers in the voice of your own experience.
- **Study.** Save a subject and, if you like, a syllabus. Live Helper answers as a student would, for nearly any subject.

The app is built for more modes later.

How a session goes: you open the window, choose to listen to the call or to your microphone, and press a hotkey when you need an answer. The answer streams in token by token. You read it and say it in your own words. The window is built to stay out of screen sharing and recordings while it stays visible to you. How well that works depends on the app that does the sharing, so test it with a practice call first.

AI is included with a plan, so there is nothing to set up. Plans have a monthly allowance, and a small free plan may be on offer too. Spoken answers (the app reads an answer aloud) are an optional extra that comes with the top plan only. Plans and prices are on the website: [livehelper.app](https://livehelper.app).

AI can be wrong. Treat the answers as a helper, check what matters, and follow the rules of the place where you use it. You are responsible for what you say.

## Download

These links always give the newest version.

| Your computer | Download |
| --- | --- |
| Mac with an Apple M chip (M1 and newer) | [Live-Helper-mac-arm64.dmg](../../releases/latest/download/Live-Helper-mac-arm64.dmg) |
| Mac with an Intel processor | [Live-Helper-mac-x64.dmg](../../releases/latest/download/Live-Helper-mac-x64.dmg) |
| Windows, 64 bit | [Live-Helper-win-x64.exe](../../releases/latest/download/Live-Helper-win-x64.exe) |

Not sure which Mac you have?

1. Click the Apple menu in the top left corner of the screen, then choose About This Mac.
2. Look for the line that says Chip or Processor.
3. If it says Apple M1, M2, M3 or another Apple M, pick the Apple Silicon file (`mac-arm64`).
4. If it says Intel, pick the Intel file (`mac-x64`).

You can also download from the [website](https://livehelper.app/en/download). Get Live Helper only from this repository or from the website.

## Install and open it

**Live Helper is not code signed yet.** Because of that, your system may say the app is unknown or not certified the first time you open it. This is expected for a new app. The steps below open it anyway.

### Mac

1. Open the downloaded file and drag Live Helper into the Applications folder.
2. Open Live Helper from Applications. A warning appears and the app does not open. Close the warning.
3. Open System Settings, then Privacy & Security.
4. Scroll down. Next to Live Helper, press Open Anyway.
5. Confirm with your password or Touch ID, then press Open.

Live Helper needs two permissions on Mac:

- **Microphone.** macOS asks the first time you listen to your microphone.
- **Screen Recording.** It is needed to hear the call (system audio) and to take screenshots. Allow it in System Settings, Privacy & Security, Screen Recording. Then quit Live Helper and open it again.

Allow both, or the app cannot hear you or see your screen. Because the app is not code signed, macOS treats every new install or update as a new app. After an update it may ask for both permissions again, and the Open Anyway warning may show again too.

### Windows

1. Open the file you downloaded.
2. If you see "Windows protected your PC", press More info.
3. Press Run anyway.
4. Follow the installer. When it finishes, open Live Helper like any other app.

On Windows there is no screen permission. For the microphone, make sure "Let desktop apps access your microphone" is on in Settings, Privacy & security, Microphone.

## How the app works

### Connect your account

Open the app and sign in with your email. The app sends a code to that email, and you type the code in. There is no password. If you bought a plan on the website, sign in with the same email and your plan is ready. If you reach the limit of devices for your account, the app asks which one to replace.

### Updates

- The app asks about a new version when it starts and then about every hour.
- When a newer version is out, a banner tells you what is new.
- **On Mac,** pressing Update opens the download. Install the new version the same way as the first time.
- **On Windows,** pressing Update downloads the new version and installs it inside the app.
- The app never installs while a live session is running, and the banner stays away during a session.
- **Later** hides the banner for 24 hours.
- Some releases are marked **Mandatory**. Older versions stop at an update screen until you update. This is used rarely, for a fix that old versions must not keep running.

### Where your data lives

Your saved setups, profile and settings live on your computer:

- Mac: `~/Library/Application Support/live-helper`
- Windows: `%APPDATA%\\live-helper`

Your API keys, if you ever add any, are encrypted by the system (the Keychain on Mac, DPAPI on Windows). Sessions (the transcript and the answers) are never saved to disk. The app has no telemetry.

With Included AI, the audio, the transcript and the context for one request go to the Live Helper server, which passes them to its approved AI providers. The server does not store or log them. The server also handles your account: sign in, plan, usage and devices. A small random marker is kept in a folder called LiveHelperShared, next to the data folder, so updates and reinstalls keep the same marker. It is made at random and is not made from your hardware.

## How releases are made here

This repository holds only the finished downloads. It has no source code. The app is built in a private repository.

- A release starts when a new version tag is pushed in the private repository. A workflow there builds the Mac and Windows installers and publishes them here.
- Nothing is uploaded by hand.
- The release stays hidden until every file is built and checked. If a build fails, nothing goes public.
- Only the newest version is public. When a new version comes out, the earlier releases are hidden again. Their files are kept, but nobody can download them from here.
- Each release has these five files. You need only one of the first three. The last two are for the Windows updater.

| File | What it is |
| --- | --- |
| `Live-Helper-mac-arm64.dmg` | Mac, Apple Silicon |
| `Live-Helper-mac-x64.dmg` | Mac, Intel |
| `Live-Helper-win-x64.exe` | Windows installer |
| `Live-Helper-win-x64.exe.blockmap` | Windows update file |
| `latest.yml` | Windows update file |

The text of each release has a line `Summary EN:` and a line `Summary UK:`, a short summary in English and in Ukrainian. A release that must not be skipped also has the line `Mandatory: yes`.

## Latest releases

This list updates by itself. A small workflow in this repository rewrites it whenever a release is published, changed or hidden, and once a day. It shows the public releases, newest first, up to ten. Because only the newest version stays public, expect one entry. A hidden release does not appear here.

<!-- releases:start -->
- **v1.1.0** (2026-11-23): Answers can now appear automatically, plans are clearer, and sign in is smoother. Please update to keep using Live Helper. Mandatory update. [Release page](https://github.com/livehelper-app/live-helper-releases/releases/tag/v1.1.0)
<!-- releases:end -->

## Help

For help, go to the website: [livehelper.app](https://livehelper.app). The Support page inside the app is there too.

## License and safety

This repository has no license file, and it holds no source code. The downloads are the Live Helper app, and the Terms of Service and the Privacy Policy are on the [website](https://livehelper.app). Because the app is not code signed yet, download it only from this repository or from the website, and never from a link someone sent you.
