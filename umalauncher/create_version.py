import pyinstaller_versionfile
from constants import UMLAUNCHER_VERSION

def generate():
    pyinstaller_versionfile.create_versionfile(
        output_file="version.rc",
        version=UMLAUNCHER_VERSION,
        file_description="Uma Launcher",
        internal_name="Uma Launcher",
        original_filename="UmaLauncher.exe",
        product_name="Uma Launcher"
    )

if __name__ == "__main__":
    generate()
