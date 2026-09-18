$ErrorActionPreference = "Stop"

& uv run --with cairosvg python `
    (Join-Path $PSScriptRoot "export_green_render.py")

if ($LASTEXITCODE -ne 0) {
    throw "Flat green-board render failed"
}
