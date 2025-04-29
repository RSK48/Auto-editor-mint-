@echo off
setlocal enabledelayedexpansion

:: Process all .mp4 and .wav files with auto-editor
for %%F in (*.mp4 *.wav) do auto-editor "%%F" --margin 0.2sec

:: Rename files by removing "_ALTERED" from their names
for %%F in (*_ALTERED*) do (
    set "name=%%F"
    ren "%%F" "!name:_ALTERED=!"
)

endlocal
