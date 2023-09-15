# Changelog

## 1.0.0 (2023-09-15)


### Features

* Add akmods signing keys ([00b1a67](https://github.com/andersrh/akmods/commit/00b1a67b7fb891484f717a3acd227b0a7371c561))
* add all-builds check job ([1d58504](https://github.com/andersrh/akmods/commit/1d58504fab4c8594a734a42d998658bdcd6b091c))
* add broadcom legacy wl driver ([14b9def](https://github.com/andersrh/akmods/commit/14b9def3cf609cdb6b3e2c5f9260ad60547c4c22)), closes [#3](https://github.com/andersrh/akmods/issues/3)
* Add evdi kmod to support displaylink ([de8dbed](https://github.com/andersrh/akmods/commit/de8dbed3050de11232472c415d5e1b02a21fe6c2))
* Add gcadapter_oc driver kmod ([33487af](https://github.com/andersrh/akmods/commit/33487afb2585b2d3189060e3ebcbdef28211b124))
* Add Google Coral TPU Gasket & Apex drivers ([238d8be](https://github.com/andersrh/akmods/commit/238d8bea41225fc4b24f1911707e546af9252e5b))
* Add new ublue-os/akmod copr repo ([b2c0452](https://github.com/andersrh/akmods/commit/b2c0452a234a357f9377619e6b0290322aaa4375))
* add nvidia kmod builds and ublue-os-nvidia-addons ([eb462ee](https://github.com/andersrh/akmods/commit/eb462ee50a40eeaf54b594f015a81a3712b94c7e))
* Add OpenRGB kernel modules ([9f870f4](https://github.com/andersrh/akmods/commit/9f870f42865a24a3f5e7f27528b2844487bdb5c6))
* Add steamdeck driver kmod ([a51dbe3](https://github.com/andersrh/akmods/commit/a51dbe37467248825c9b2a6b068d928f85f783e0))
* add xbox controller kmods ([b35d0fd](https://github.com/andersrh/akmods/commit/b35d0fdc1712ae12823cdcfea7846c6110d6121c))
* Add xpad-noone driver ([205d07f](https://github.com/andersrh/akmods/commit/205d07f6f2e01b955eeeb6f19593668eb67d3edc))
* build wl driver again ([bba4766](https://github.com/andersrh/akmods/commit/bba4766cf8ce2c1cc705d62842ea189f93999d76))
* enable 3rd party repos for akmods ([f2fec1b](https://github.com/andersrh/akmods/commit/f2fec1b3f18a98ee2a823c33bce09dad53268964))
* split nvidia akmods into distinct images ([#54](https://github.com/andersrh/akmods/issues/54)) ([4007e0c](https://github.com/andersrh/akmods/commit/4007e0cb22a9715634eda8cd773315c5e74b1a6a))
* Upgrade to steamdeck drivers from SteamOS 3.5 ([383b5f9](https://github.com/andersrh/akmods/commit/383b5f9b7abd0d205e4b7a100defb27267fd2a6a))


### Bug Fixes

* Added link from /usr/bin/rpm-ostree to /usr/bin/ dnf ([52f0433](https://github.com/andersrh/akmods/commit/52f0433d0c2b940090a79db8c7523f4140f1d07a))
* attempt fix build with extra quotes ([#9](https://github.com/andersrh/akmods/issues/9)) ([caff9d3](https://github.com/andersrh/akmods/commit/caff9d33ceb7b3e7741d74486183ef6dd29fb9df))
* disable xone until as it disables too many controllers ([e0135d0](https://github.com/andersrh/akmods/commit/e0135d08d0528cf02098d9576b7671007058c0ac))
* Remove no longer needed ltrf216a driver ([7144d4b](https://github.com/andersrh/akmods/commit/7144d4b20a1044ba1473fba16612a2ba44c14e04))
* Restore steamdeck and gcadapter_oc akmods ([b2c0452](https://github.com/andersrh/akmods/commit/b2c0452a234a357f9377619e6b0290322aaa4375))
* sign akmods-nvidia images properly ([e71d7b2](https://github.com/andersrh/akmods/commit/e71d7b22c30f63fe273ba2015fe8cdc40c755690))
* Switch to building jupiter driver instead of steamdeck ([e9c0078](https://github.com/andersrh/akmods/commit/e9c0078220e1cff3cb8192d9c1de930092b05c17))
* temporarily disable xone kmod build ([76806ad](https://github.com/andersrh/akmods/commit/76806adc856db2163c188125ba7546362282cee2))
* typo in v4l2loop rpm query ([#8](https://github.com/andersrh/akmods/issues/8)) ([ff5f9b8](https://github.com/andersrh/akmods/commit/ff5f9b874842e2b2314355293534c27aceabc9e3))
* use correct signing key 20230518 ([686c8d0](https://github.com/andersrh/akmods/commit/686c8d0522155e213a262eee9e67a8b376686b5d))
* Use existing ublue-os/akmods repo file instead of redownloading, fix removed file for negativo17 repo akmods ([1fd1ad7](https://github.com/andersrh/akmods/commit/1fd1ad78a43998377f43c04738895b085cdc97ba))
* use proper step output for image name ([f1c48ab](https://github.com/andersrh/akmods/commit/f1c48ab3e98b5819c01f7146237e2506b1fdc718))
