$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pcbPath = Join-Path $repoRoot "weather-balloon-logger.kicad_pcb"
$outputPath = Join-Path $repoRoot "outputs/renders/board-fit-check-1to1.pdf"

& kicad-cli pcb export pdf `
    --output $outputPath `
    --layers "F.Fab,F.Silkscreen,Edge.Cuts" `
    --sketch-pads-on-fab-layers `
    --black-and-white `
    --drill-shape-opt 2 `
    --mode-single `
    --scale 1 `
    $pcbPath

if ($LASTEXITCODE -ne 0) {
    throw "KiCad 1:1 fit-check PDF export failed"
}

if (-not (Test-Path $outputPath)) {
    throw "Fit-check PDF was not created"
}

Write-Output "Wrote 1:1 fit-check PDF to '$outputPath'"
