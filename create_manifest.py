from pathlib import Path
import shutil

build_dir = Path("build/")
build_bundles_dir = build_dir / "bundles"


def copy_and_log(input: Path, output: Path):
    print(f"\tCopy {input.resolve()} to {output.resolve()}")
    shutil.copy(input, output)


bundles = [
    "Ambience",
    "Bandisto",
    "BeatBox",
    "Combo",
    "DX10",
    "DeEss",
    "Degrade",
    "Delay",
    "Detune",
    "Dither",
    "DubDelay",
    "Dynamics",
    "EPiano",
    "Image",
    "JX10",
    "Leslie",
    "Limiter",
    "Loudness",
    "MultiBand",
    "Overdrive",
    "Piano",
    "RePsycho",
    "RezFilter",
    "RingMod",
    "RoundPan",
    "Shepard",
    "Splitter",
    "Stereo",
    "SubSynth",
    "TalkBox",
    "TestTone",
    "ThruZero",
    "Tracker",
    "Transient",
    "VocInput",
    "Vocoder",
]

for bundle_name in bundles:
    print(f"Operating on {bundle_name}")
    bundle_input_dir = Path(f"bundles/mod-mda-{bundle_name}.lv2/")
    bundle_output_dir = build_bundles_dir / bundle_name

    bundle_output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\tCreating directory {bundle_output_dir}")

    manifest_file = bundle_input_dir / "manifest.ttl.in"
    output_manifest = manifest_file.read_text().replace("@LIB_EXT@", ".so")
    output_file = bundle_output_dir / "manifest.ttl"
    output_file.write_text(output_manifest)
    print(f"\tWrote manifest file to {output_file.resolve()}")

    configuration_files = bundle_input_dir.glob("*.ttl")
    for configuration in configuration_files:
        copy_and_log(configuration, bundle_output_dir / configuration.name)

    so_file = f"{bundle_name}.so"
    library_file = build_dir / so_file
    copy_and_log(library_file, bundle_output_dir / so_file)
