# PowerShell Script: prepare_dataset.ps1

# Set dataset ID and paths
$datasetId = "sujaykapadnis/emotion-recognition-dataset"
$downloadDir = "download"
$extractDir = "raw_data"
$readFrom = "raw_data/dataset"
$writeTo = "dataset"
$seed = 0

# Step 1: Download and extract dataset
Write-Host "`n--- Downloading and extracting dataset ---`n"
python downloader.py --dataset $datasetId --download-dir $downloadDir --extract-to $extractDir

# Step 2: Run image processor
Write-Host "`n--- Preprocessing images ---`n"
python image_processor.py --read-from $readFrom --write-to $writeTo --seed $seed

Write-Host "`nDataset preparation completed successfully."
