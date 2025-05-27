<#
.SYNOPSIS
Installs and activates the Python environment.

.DESCRIPTION
This script installs the necessary Python environment and activates it for use.

.PARAMETER commitMessage
Specifies the commit message for the release.

.EXAMPLE
.\release.ps1
This will run the script to install and activate the Python environment.

.NOTES
File Path: /c:/git/pyRejseplan/scripts/release.ps1
#>
# Get the commit message from the user
param (
    [string]$commitMessage
)

if (-not $commitMessage) {
    Write-Host "Commit message is required."
    exit 1
}

# Install and activate the Python environment
if (-Not (Test-Path -Path "./.venv")) {
    python -m venv .venv
}
./.venv/Scripts/activate
uv sync --dev

# Get the version using setuptools_scm
$version = python -m setuptools_scm --strip-dev
if (-not $version) {
    Write-Host "Failed to retrieve version using setuptools_scm."
    exit 1
}
$version = $version.Trim()

# Extract the major.minor.build part from the version string
if ($version -match '^(\d+)\.(\d+)\.(\d+)?$') {
    Write-Information "Valid version format, new version is $version"
} else {
    Write-Host "Invalid version format. Expected format: major.minor.build, got $version"
    exit 1
}

# Commit the changes and create a new git tag
git add .
git commit -m $commitMessage
git tag -a "v$version" -m $commitMessage
git push origin --tags
