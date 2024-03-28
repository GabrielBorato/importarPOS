$exclude = @("venv", "Importar_POS.prod.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Importar_POS.prod.zip" -Force