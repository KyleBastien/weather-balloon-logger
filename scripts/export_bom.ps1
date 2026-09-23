$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$schematic = Join-Path $repoRoot "weather-balloon-logger.kicad_sch"
$output = Join-Path $repoRoot "outputs/BOM.csv"
$jlcOutput = Join-Path $repoRoot "outputs/jlcpcb-bom.csv"

& kicad-cli sch export bom $schematic `
    --output $output `
    --fields "Reference,MPN,QUANTITY" `
    --labels "refdes,MPN,qty" `
    --group-by "MPN" `
    --sort-field "Reference"

if ($LASTEXITCODE -ne 0) {
    throw "KiCad BOM export failed with exit code $LASTEXITCODE"
}

$rows = Import-Csv $output
$quantity = ($rows | Measure-Object -Property qty -Sum).Sum
$missingMpn = @($rows | Where-Object { [string]::IsNullOrWhiteSpace($_.MPN) })

if ($quantity -ne 10) {
    throw "Expected 10 populated refdes, found $quantity"
}

if ($missingMpn.Count -ne 0) {
    throw "BOM contains $($missingMpn.Count) row(s) without an MPN"
}

Write-Output "BOM exported: $($rows.Count) grouped rows, $quantity populated refdes, no blank MPNs"

& kicad-cli sch export bom $schematic `
    --output $jlcOutput `
    --fields "Value,Reference,Footprint,LCSC" `
    --labels "Comment,Designator,Footprint,LCSC Part #" `
    --group-by "Value,Footprint,LCSC" `
    --sort-field "Reference"

if ($LASTEXITCODE -ne 0) {
    throw "KiCad JLCPCB-reference BOM export failed with exit code $LASTEXITCODE"
}

Write-Output "JLCPCB reference BOM exported (hand-assembly convenience only)"
