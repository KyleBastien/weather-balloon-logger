$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pcbPath = Join-Path $repoRoot "weather-balloon-logger.kicad_pcb"
$outputPath = Join-Path $repoRoot "outputs/renders/board-green-top.png"

& kicad-cli pcb render `
    --output $outputPath `
    --side top `
    --quality high `
    --width 2400 `
    --height 2400 `
    --background opaque `
    $pcbPath

if ($LASTEXITCODE -ne 0) {
    throw "KiCad green-board render failed"
}

if (-not (Test-Path $outputPath)) {
    throw "Green-board render was not created"
}

Write-Output "Wrote green-board render to '$outputPath'"
