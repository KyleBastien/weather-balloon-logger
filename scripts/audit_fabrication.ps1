$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$pcbPath = Join-Path $repoRoot "weather-balloon-logger.kicad_pcb"
$schPath = Join-Path $repoRoot "weather-balloon-logger.kicad_sch"
$bomPath = Join-Path $repoRoot "outputs/BOM.csv"
$drillPath = Join-Path $repoRoot "outputs/gerbers/weather-balloon-logger.drl"

$pcb = Get-Content $pcbPath -Raw
$sch = Get-Content $schPath -Raw
$bom = Import-Csv $bomPath
$drill = Get-Content $drillPath -Raw

$smdPads = [regex]::Matches($pcb, '(?m)^\s*\(pad\s+"[^"]*"\s+smd\b').Count
$pthPads = [regex]::Matches($pcb, '(?m)^\s*\(pad\s+"[^"]*"\s+thru_hole\b').Count
$npthPads = [regex]::Matches($pcb, '(?m)^\s*\(pad\s+"[^"]*"\s+np_thru_hole\b').Count
$footprints = [regex]::Matches($pcb, '(?m)^\s*\(footprint\s+').Count
$mpnProperties = [regex]::Matches($sch, '(?m)^\s*\(property "MPN"').Count
$slotCommands = [regex]::Matches($drill, 'G85').Count
$bomQuantity = ($bom | Measure-Object -Property qty -Sum).Sum
$blankMpn = @($bom | Where-Object { [string]::IsNullOrWhiteSpace($_.MPN) }).Count
$unverifiedMpn = @($bom | Where-Object { $_.MPN -match 'UNVERIFIED' }).Count

$requiredFabFiles = @(
    'weather-balloon-logger-F_Cu.gbr',
    'weather-balloon-logger-B_Cu.gbr',
    'weather-balloon-logger-F_Mask.gbr',
    'weather-balloon-logger-B_Mask.gbr',
    'weather-balloon-logger-F_Silkscreen.gbr',
    'weather-balloon-logger-Edge_Cuts.gbr',
    'weather-balloon-logger.drl',
    'weather-balloon-logger-job.gbrjob'
)

$missingFabFiles = @($requiredFabFiles | Where-Object {
    -not (Test-Path (Join-Path $repoRoot "outputs/gerbers/$_"))
})

Write-Output "Fabrication source audit"
Write-Output "  Footprints: $footprints (expected 15: 10 populated + 4 mounting holes + 1 graphic)"
Write-Output "  SMD pads: $smdPads (expected 0)"
Write-Output "  Plated through-hole pads: $pthPads"
Write-Output "  Non-plated through-hole pads: $npthPads (expected 4)"
Write-Output "  Schematic MPN properties: $mpnProperties (expected 10)"
Write-Output "  BOM populated quantity: $bomQuantity (expected 10)"
Write-Output "  BOM blank MPN rows: $blankMpn (expected 0)"
Write-Output "  BOM unverified MPN rows: $unverifiedMpn (expected 0)"
Write-Output "  Plated-slot drill commands: $slotCommands (expected 0)"
Write-Output "  Missing core fabrication files: $($missingFabFiles.Count)"

$failures = @()
if ($footprints -ne 15) { $failures += "Unexpected footprint count" }
if ($smdPads -ne 0) { $failures += "SMD pads present" }
if ($npthPads -ne 4) { $failures += "Unexpected NPTH count" }
if ($mpnProperties -ne 10) { $failures += "Not every populated symbol has an MPN" }
if ($bomQuantity -ne 10) { $failures += "Unexpected BOM quantity" }
if ($blankMpn -ne 0) { $failures += "Blank BOM MPN" }
if ($unverifiedMpn -ne 0) { $failures += "Unverified BOM MPN" }
if ($slotCommands -ne 0) { $failures += "Unexpected plated-slot count" }
if ($missingFabFiles.Count -ne 0) { $failures += "Missing core fabrication output" }

if ($failures.Count -ne 0) {
    throw ($failures -join "; ")
}

Write-Output "Fabrication source audit passed"
