@echo off
setlocal enabledelayedexpansion

set "indent="
set "subindent1=  "
set "subindent2=    "

for /d %%i in (*) do (
    echo !indent!- %%i
    set "subfolder=%%i"
    for /d %%j in ("!subfolder!\*") do (
        echo !subindent1!- %%j
        set "subsubfolder=%%j"
        for /d %%k in ("!subsubfolder!\*") do (
            echo !subindent2!- %%k
        )
    )
)
