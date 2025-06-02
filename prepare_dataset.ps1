# PowerShell Script: prepare_dataset.ps1

# Parameters
$datasetId = "sujaykapadnis/emotion-recognition-dataset"
$downloadDir = "download"
$extractDir = "raw_data"
$readFrom = "raw_data/dataset"
$writeTo = "dataset"
$seed = 0
$width = 48
$height = 48
$limit = 100

# Step 1: Download and extract dataset
# Write-Host "`n--- Downloading and extracting dataset ---`n"
# python scripts/downloader.py --dataset $datasetId --download-dir $downloadDir --extract-to $extractDir

# Step 2: Run image processor with all arguments
Write-Host "`n--- Preprocessing images ---`n"
python scripts/image_processor.py `
    --read-from $readFrom `
    --write-to $writeTo `
    --seed $seed `
    --size $width $height `
    --limit $limit

Write-Host "`nDataset preparation completed successfully."
