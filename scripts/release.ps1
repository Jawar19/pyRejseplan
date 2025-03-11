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
python -m venv .venv
./.venv/Scripts/activate
pip install -e .[dev]

# Get the version using setuptools_scm
$version = python -m setuptools_scm
if (-not $version) {
    Write-Host "Failed to retrieve version using setuptools_scm."
    exit 1
}
$newVersion = $version.Trim()

# Commit the changes and create a new git tag
git add .
git commit -m $commitMessage
git tag -a $newVersion -m $commitMessage
git push origin --tags

# Build the distribution files using python -m build
python -m build

$version = Get-Content $versionFilePath -Raw
$version = $version.Trim()

# Parse the version and bump the build number
if ($version -match '^(\d+)\.(\d+)\.(\d+)$') {
    $major = [int]$matches[1]
    $minor = [int]$matches[2]
    $build = [int]$matches[3]
    $newVersion = "$major.$minor.$build"
} else {
    Write-Host "Invalid version format. Expected format: major.minor.build"
    exit 1
}

# Get the commit message from the user
param (
    [string]$commitMessage
)

if (-not $commitMessage) {
    Write-Host "Commit message is required."
    exit 1
}

$files = Get-ChildItem -Path "dist" -Filter "*$newVersion*" -File
if ($files.Count -eq 0) {
    Write-Host "No files found matching version $newVersion in the dist folder."
    exit 1
}
# Upload the distribution files using Twine
twine upload $files

# Check if GitHub CLI is available
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "GitHub CLI (gh) is not installed or not available in the PATH."
    Write-Host "You can install it using winget with the following command:"
    Write-Host "winget install --id GitHub.cli"
    exit 1
}

# Create a new GitHub release and upload the files
$releaseNotes = "Release version $newVersion\n$commitMessage"
gh release create $newVersion $files --title "Release $newVersion" --notes $releaseNotes --latest

