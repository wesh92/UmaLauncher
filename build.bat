cd ./umalauncher
uv run python create_version.py
uv run pyinstaller threader.spec
cd ..