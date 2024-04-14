all: 
	meson setup build --reconfigure -Dbuildtype=release
	ninja -C build
	python create_manifest.py

install: all
	cp -r build/bundles/* "${HOME}/.lv2"

