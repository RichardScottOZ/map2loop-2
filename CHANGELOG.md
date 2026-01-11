# Changelog

## [2.0.0](https://github.com/RichardScottOZ/map2loop-2/compare/v1.3.8...2.0.0) (2026-01-11)


### ⚠ BREAKING CHANGES

* DO NOT PULL THIS COMMIT - SA remote sources and the dtm generally likely won't work
* Persisting issues with SA remote data sources - not creating fault_displacements3.csv in output
* **exporting:** SA remote sources do not create output/fault_displacements3.csv and break the projectfile creation

### Features

* Adding workflow updating to proj.update_config to set and reset the model engine and associated flags (loopstructural, noddy, gempy etc) ([737aada](https://github.com/RichardScottOZ/map2loop-2/commit/737aada21a9c5447026822c8c317ab550a3d18f1))
* **exporting:** Creating valid .loop3d projectfile if one isn't given or doesn't exist ([5c773fa](https://github.com/RichardScottOZ/map2loop-2/commit/5c773fa3f141efdf1019839c5019d54f8a0edd61))
* Merged classes into master, with version bump ([4cc796e](https://github.com/RichardScottOZ/map2loop-2/commit/4cc796e38abcc4d7be4a641b64da54b17e637eed))
* Moving run flags to the update_config function in project.py so that flags are usable inside the config object, as well as in the project class run function. Accessible with proj.run_flags and proj.config.run_flags. ([b1b2962](https://github.com/RichardScottOZ/map2loop-2/commit/b1b296229c2ada89161f638037af5d4e45eb3fa6))
* Writing and testing custom build scripts locally using act ([551f622](https://github.com/RichardScottOZ/map2loop-2/commit/551f6223a34175164e2762de9f95e21fd75ecae5))


### Bug Fixes

* Add clipping of local file dtm ([3359927](https://github.com/RichardScottOZ/map2loop-2/commit/3359927b8ef7f9bc78527cb0e6f70982deca581f))
* add crs to temporary geodataframe to solve crs mismatch ([4d7023a](https://github.com/RichardScottOZ/map2loop-2/commit/4d7023aa45265b5b729d5cea573fe955103ba6e3))
* Add python version to continuous integration ([6835882](https://github.com/RichardScottOZ/map2loop-2/commit/6835882ab1f3723e016ed7fd4bee71419be996fc))
* Add supergroup to stratigraphic column, fix thickness values in projectfile output ([8387655](https://github.com/RichardScottOZ/map2loop-2/commit/83876550293d0143d6dac0914d67807e93343bad))
* added function to check if the filenames exist ([f7b6475](https://github.com/RichardScottOZ/map2loop-2/commit/f7b6475333a74895644a3f6b19dcb3bd750f5fc0))
* adding sphinx documentation ([e3a61c5](https://github.com/RichardScottOZ/map2loop-2/commit/e3a61c5fddeb0df1e24a314e82b3b9b35232f1ec))
* black format ([314ee87](https://github.com/RichardScottOZ/map2loop-2/commit/314ee87f5f8a266ac2ab724f0b3faff2bb89e20d))
* casting numeric columns as float ([2755546](https://github.com/RichardScottOZ/map2loop-2/commit/275554669d70c5319d81fd58c1afd2497d02685c))
* change rasterio dependency to enable python 3.7 to work ([2fb5b80](https://github.com/RichardScottOZ/map2loop-2/commit/2fb5b80ad9c86afae9b3d79fef2acfceea4e0d43))
* Change to force CICD ([f05ee0f](https://github.com/RichardScottOZ/map2loop-2/commit/f05ee0f99160bb38264c6554a61c5257ab4aa8dd))
* Configuring git credentials for building on action ([c754428](https://github.com/RichardScottOZ/map2loop-2/commit/c754428ea911afc049838ef12fb76d2c0554f791))
* **dtm:** Resolving load_dtm in config.py to accept http dtm files ([b82bf65](https://github.com/RichardScottOZ/map2loop-2/commit/b82bf65981e8e467af1860006563b39f9e4872b0))
* error with typehint return type for tuple ([9c091f6](https://github.com/RichardScottOZ/map2loop-2/commit/9c091f64150c777efe77ea78d30310b71d28cf65))
* extract basal contacts using geopandas native functions rather than point operations. Not working yet ([91938c7](https://github.com/RichardScottOZ/map2loop-2/commit/91938c7079ddca9a818c870bbe7a51229b3adf23))
* Fill nan in id column of geology shapefile causing missing layers ([55ebd9c](https://github.com/RichardScottOZ/map2loop-2/commit/55ebd9cd15e48b97a86ef579b2e09f065ecc4010))
* Fix strike conversion logic, Replace drift_prefix with ignore_codes option, remove opentopography dtm ([97d26ed](https://github.com/RichardScottOZ/map2loop-2/commit/97d26ed0f6f6d5545a4c3c3ad2c47dee3bfe7c9a))
* Fixing all versioning and conda/pip issues ([906a1b4](https://github.com/RichardScottOZ/map2loop-2/commit/906a1b4560337e457b2e6b50a0c43f3d835a0089))
* Forgot to access series and typecast to int result ([864857b](https://github.com/RichardScottOZ/map2loop-2/commit/864857b175f7a12519a6181b7d16a1ed49f2d968))
* **interpolate:** Initialising l, m and n before use - passing remote and local WA/SA tests ([a79c592](https://github.com/RichardScottOZ/map2loop-2/commit/a79c5926f76984765db5163be33b00dc59a7d96d))
* m2l_map_checker.py added type conversion for string comparisons, *.py coding standard compliance changes ([57ed24c](https://github.com/RichardScottOZ/map2loop-2/commit/57ed24c44ad5c1244cd4b0ed82b476b7e6df7705))
* Making conda import version without using jinja ([c618c62](https://github.com/RichardScottOZ/map2loop-2/commit/c618c622703e69a4336686a28d53b71a62136c7b))
* Move crs assignment to after geology has been specified ([e74e9e9](https://github.com/RichardScottOZ/map2loop-2/commit/e74e9e91918571b227ed368e8ef21b21f3906fe7))
* Move sjoin out of loop for efficiency ([fe59514](https://github.com/RichardScottOZ/map2loop-2/commit/fe59514b2737aaed751b334bd2a62bd47b8d7f5b))
* moving away from c_l and using human readable names ([57eeeb7](https://github.com/RichardScottOZ/map2loop-2/commit/57eeeb702afc2620e15e32bbb201f6249c6e2db6))
* normalising fault trace vector before comparing to dip direction ([bda0ddd](https://github.com/RichardScottOZ/map2loop-2/commit/bda0dddfd6d4dee0cc6b347d62ac08da540671db))
* ordering ([8901d03](https://github.com/RichardScottOZ/map2loop-2/commit/8901d0306ba9c1659869662449af76ae521aa324))
* Passing SA remote tests by correctly processing min fault lengths and mindep file checking, also allowing passing a bool to the overwrite flag ([c71cadf](https://github.com/RichardScottOZ/map2loop-2/commit/c71cadf02bc761c95017f56897aff76448ea53ca))
* Reactivating quiet flag in other map2model call ([2fb4e96](https://github.com/RichardScottOZ/map2loop-2/commit/2fb4e96f45df36303b512b6d10941e0b7c84aec1))
* remove osx conda build ([7209704](https://github.com/RichardScottOZ/map2loop-2/commit/72097049f479714c9c3e73941bb978e4523977b4))
* Remove pypi dependencies while gdal and rasterio can't install easily ([17c9076](https://github.com/RichardScottOZ/map2loop-2/commit/17c9076d11e104e24ab79aa777c69e951f0c058c))
* Removed bug where southern dipdir were being inverted ([92eef44](https://github.com/RichardScottOZ/map2loop-2/commit/92eef44cde1905639b40d326522670abf657b20d))
* Removing conflict resolving marks from July2021 merge and reactivating map2model quiet flag ([8241557](https://github.com/RichardScottOZ/map2loop-2/commit/8241557bffe899a96dd3b7e92a180dc55ed299b7))
* Removing modules file ([9a09c12](https://github.com/RichardScottOZ/map2loop-2/commit/9a09c12316e1ec593aa4a85a784c5b49c49efb81))
* Removing notebooks submoule to speed up installs and testing ([6afe569](https://github.com/RichardScottOZ/map2loop-2/commit/6afe569628293e2074f02a8cc86703640de6d0b2))
* Removing submodule cache ([79563d0](https://github.com/RichardScottOZ/map2loop-2/commit/79563d0b13a2796277bcca9b4003b0ea04d66050))
* removing type hint for python 3.8 ([587441f](https://github.com/RichardScottOZ/map2loop-2/commit/587441fb87b7fdf34ef6abe66cc1b771cf0d94c8))
* Reset tags to not include v and attempt to get pip install working ([2d0924b](https://github.com/RichardScottOZ/map2loop-2/commit/2d0924b4127e7e659e99a2c3258b5cb983e28bd0))
* Rework contact calculations to use geopandas functions rather than multi-layered for loop. Potential fix to Bug [#101](https://github.com/RichardScottOZ/map2loop-2/issues/101) ([ffb263e](https://github.com/RichardScottOZ/map2loop-2/commit/ffb263ec6c511b28a6fc44cf29c8e1a62484bdd2))
* rework of topology file structure and graph usage ([a5419e8](https://github.com/RichardScottOZ/map2loop-2/commit/a5419e8d8f70a5dbd41db4fd842a0127b52b89aa))
* Set interpolated contact observations default to false ([948d817](https://github.com/RichardScottOZ/map2loop-2/commit/948d8178e318d33d29c39cd42b667c3518adc5e6))
* Temporary fix to avoid rasterio/gdal conflicts ([23e5f6a](https://github.com/RichardScottOZ/map2loop-2/commit/23e5f6a9fce11281add61161fb0d6637b37d1da9))
* Testing github workflow ([4953f0a](https://github.com/RichardScottOZ/map2loop-2/commit/4953f0a1811c5e0ce9b73a3e191eed4a07726ee5))
* Testing jinja again ([0f373a4](https://github.com/RichardScottOZ/map2loop-2/commit/0f373a42cc829343e5bbeb123410c1a4dbe0f048))
* Trying to use the jinja trigger to passively load the version number ([cbe1c8b](https://github.com/RichardScottOZ/map2loop-2/commit/cbe1c8b7f99a1e3921c43477f854f73d6f1e0add))
* Type casting of object_ids so that mixture of str, numeric and nans can be evaluated. Please type fix ([633d62d](https://github.com/RichardScottOZ/map2loop-2/commit/633d62d1808c2c8fab761fc872308a2cab0a89d6))
* Updating build scripts and changing imports to fit with loopy ([6c79dec](https://github.com/RichardScottOZ/map2loop-2/commit/6c79dece4e266ee572ff7df589c3cd767e334f94))
* version bump ([d9bdd34](https://github.com/RichardScottOZ/map2loop-2/commit/d9bdd343461f1bf278da4e7665aca18ebf5a8422))
* version bump ([e9200d1](https://github.com/RichardScottOZ/map2loop-2/commit/e9200d18337835546aea202f0ac62ec705253ad2))
* Version bump ([d844980](https://github.com/RichardScottOZ/map2loop-2/commit/d84498072187458f1d313523dfe10f77157885e2))
* Version bump ([a92fa41](https://github.com/RichardScottOZ/map2loop-2/commit/a92fa4145586b944a322f7a6fd9d6256b0624c9a))
* Version bump ([22b4912](https://github.com/RichardScottOZ/map2loop-2/commit/22b49128803b1bb29c192c9f5391af693e0a148b))
* version bump for mambaforge build ([31eabb3](https://github.com/RichardScottOZ/map2loop-2/commit/31eabb37eab016b30d918d8793f159769fa4313c))
* Without explicit string type replacement silently fails ([451a876](https://github.com/RichardScottOZ/map2loop-2/commit/451a876b9c3549e49d3f3f9691d87c2ee595ddd0))
* Write a short and imperative summary of the code changes: (lower case and no period) ([a2316a9](https://github.com/RichardScottOZ/map2loop-2/commit/a2316a9850a3f0d40d9b2292b33436ba654906ed))


### Documentation

* adding templates for issues ([2874b97](https://github.com/RichardScottOZ/map2loop-2/commit/2874b97feb883078a5e7af7a8a86fd78ec76bada))
* formatting documentation folder ([b720fce](https://github.com/RichardScottOZ/map2loop-2/commit/b720fce11ef2bde131e67fad4a6df29aa3748818))
* Trying to ignore editor configuration settings ([78905bd](https://github.com/RichardScottOZ/map2loop-2/commit/78905bda629f76583a1b2cfa31b43bada96b194d))


### Tests

* Testing after projectfile generation/local dtms/various pull requests, mostly passing ([9c8a7ad](https://github.com/RichardScottOZ/map2loop-2/commit/9c8a7ada454131b8e312d7fc30c960238ae7d431))


### Continuous Integration

* Making conda build import version number from setup.py and testing ([ddac3be](https://github.com/RichardScottOZ/map2loop-2/commit/ddac3befe2385c98f34bcb10596b1b7a1e50bb32))

## [1.3.8](https://github.com/Loop3D/map2loop-2/compare/1.3.7...1.3.8) (2023-11-28)


### Bug Fixes

* Change to force CICD ([f05ee0f](https://github.com/Loop3D/map2loop-2/commit/f05ee0f99160bb38264c6554a61c5257ab4aa8dd))

## [1.3.7](https://github.com/Loop3D/map2loop-2/compare/1.3.6...1.3.7) (2023-08-14)


### Bug Fixes

* Forgot to access series and typecast to int result ([864857b](https://github.com/Loop3D/map2loop-2/commit/864857b175f7a12519a6181b7d16a1ed49f2d968))
* Type casting of object_ids so that mixture of str, numeric and nans can be evaluated. Please type fix ([633d62d](https://github.com/Loop3D/map2loop-2/commit/633d62d1808c2c8fab761fc872308a2cab0a89d6))
* Version bump ([d844980](https://github.com/Loop3D/map2loop-2/commit/d84498072187458f1d313523dfe10f77157885e2))

## [1.3.6](https://github.com/Loop3D/map2loop-2/compare/1.3.5...1.3.6) (2023-05-29)


### Bug Fixes

* Fill nan in id column of geology shapefile causing missing layers ([55ebd9c](https://github.com/Loop3D/map2loop-2/commit/55ebd9cd15e48b97a86ef579b2e09f065ecc4010))
* Rework contact calculations to use geopandas functions rather than multi-layered for loop. Potential fix to Bug [#101](https://github.com/Loop3D/map2loop-2/issues/101) ([ffb263e](https://github.com/Loop3D/map2loop-2/commit/ffb263ec6c511b28a6fc44cf29c8e1a62484bdd2))
* Version bump ([a92fa41](https://github.com/Loop3D/map2loop-2/commit/a92fa4145586b944a322f7a6fd9d6256b0624c9a))

## [1.3.5](https://github.com/Loop3D/map2loop-2/compare/1.3.4...1.3.5) (2023-02-22)


### Bug Fixes

* Removed bug where southern dipdir were being inverted ([92eef44](https://github.com/Loop3D/map2loop-2/commit/92eef44cde1905639b40d326522670abf657b20d))
* Set interpolated contact observations default to false ([948d817](https://github.com/Loop3D/map2loop-2/commit/948d8178e318d33d29c39cd42b667c3518adc5e6))

## [1.3.4](https://github.com/Loop3D/map2loop-2/compare/1.3.3...1.3.4) (2023-02-09)


### Bug Fixes

* m2l_map_checker.py added type conversion for string comparisons, *.py coding standard compliance changes ([57ed24c](https://github.com/Loop3D/map2loop-2/commit/57ed24c44ad5c1244cd4b0ed82b476b7e6df7705))
* Version bump ([22b4912](https://github.com/Loop3D/map2loop-2/commit/22b49128803b1bb29c192c9f5391af693e0a148b))

## [1.3.3](https://github.com/Loop3D/map2loop-2/compare/1.3.2...1.3.3) (2022-12-04)


### Bug Fixes

* version bump ([d9bdd34](https://github.com/Loop3D/map2loop-2/commit/d9bdd343461f1bf278da4e7665aca18ebf5a8422))

## [1.3.2](https://github.com/Loop3D/map2loop-2/compare/1.3.1...1.3.2) (2022-11-30)


### Bug Fixes

* Add clipping of local file dtm ([3359927](https://github.com/Loop3D/map2loop-2/commit/3359927b8ef7f9bc78527cb0e6f70982deca581f))
* Fix strike conversion logic, Replace drift_prefix with ignore_codes option, remove opentopography dtm ([97d26ed](https://github.com/Loop3D/map2loop-2/commit/97d26ed0f6f6d5545a4c3c3ad2c47dee3bfe7c9a))
* Move sjoin out of loop for efficiency ([fe59514](https://github.com/Loop3D/map2loop-2/commit/fe59514b2737aaed751b334bd2a62bd47b8d7f5b))
* version bump ([e9200d1](https://github.com/Loop3D/map2loop-2/commit/e9200d18337835546aea202f0ac62ec705253ad2))

## [1.3.1](https://github.com/Loop3D/map2loop-2/compare/1.3.0...1.3.1) (2022-11-08)


### Bug Fixes

* version bump for mambaforge build ([31eabb3](https://github.com/Loop3D/map2loop-2/commit/31eabb37eab016b30d918d8793f159769fa4313c))

## [1.3.0](https://github.com/Loop3D/map2loop-2/compare/v1.2.10...1.3.0) (2022-11-01)


### Features

* Merged classes into master, with version bump ([4cc796e](https://github.com/Loop3D/map2loop-2/commit/4cc796e38abcc4d7be4a641b64da54b17e637eed))


### Bug Fixes

* add crs to temporary geodataframe to solve crs mismatch ([4d7023a](https://github.com/Loop3D/map2loop-2/commit/4d7023aa45265b5b729d5cea573fe955103ba6e3))
* Add supergroup to stratigraphic column, fix thickness values in projectfile output ([8387655](https://github.com/Loop3D/map2loop-2/commit/83876550293d0143d6dac0914d67807e93343bad))
* Move crs assignment to after geology has been specified ([e74e9e9](https://github.com/Loop3D/map2loop-2/commit/e74e9e91918571b227ed368e8ef21b21f3906fe7))
* rework of topology file structure and graph usage ([a5419e8](https://github.com/Loop3D/map2loop-2/commit/a5419e8d8f70a5dbd41db4fd842a0127b52b89aa))
* Without explicit string type replacement silently fails ([451a876](https://github.com/Loop3D/map2loop-2/commit/451a876b9c3549e49d3f3f9691d87c2ee595ddd0))

## [1.2.10](https://github.com/Loop3D/map2loop-2/compare/v1.2.9...v1.2.10) (2022-08-20)


### Bug Fixes

* Remove pypi dependencies while gdal and rasterio can't install easily ([17c9076](https://github.com/Loop3D/map2loop-2/commit/17c9076d11e104e24ab79aa777c69e951f0c058c))

### [1.2.9](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.8...v1.2.9) (2022-08-18)


### Bug Fixes

* Reset tags to not include v and attempt to get pip install working ([2d0924b](https://www.github.com/Loop3D/map2loop-2/commit/2d0924b4127e7e659e99a2c3258b5cb983e28bd0))

### [1.2.8](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.7...v1.2.8) (2022-08-03)


### Bug Fixes

* change rasterio dependency to enable python 3.7 to work ([2fb5b80](https://www.github.com/Loop3D/map2loop-2/commit/2fb5b80ad9c86afae9b3d79fef2acfceea4e0d43))

### [1.2.7](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.6...v1.2.7) (2022-08-02)


### Bug Fixes

* ordering ([8901d03](https://www.github.com/Loop3D/map2loop-2/commit/8901d0306ba9c1659869662449af76ae521aa324))

### [1.2.6](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.5...v1.2.6) (2022-08-02)


### Bug Fixes

* remove osx conda build ([7209704](https://www.github.com/Loop3D/map2loop-2/commit/72097049f479714c9c3e73941bb978e4523977b4))

### [1.2.5](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.4...v1.2.5) (2022-08-02)


### Bug Fixes

* Add python version to continuous integration ([6835882](https://www.github.com/Loop3D/map2loop-2/commit/6835882ab1f3723e016ed7fd4bee71419be996fc))

### [1.2.4](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.3...v1.2.4) (2022-08-02)


### Bug Fixes

* Temporary fix to avoid rasterio/gdal conflicts ([23e5f6a](https://www.github.com/Loop3D/map2loop-2/commit/23e5f6a9fce11281add61161fb0d6637b37d1da9))

### [1.2.3](https://www.github.com/Loop3D/map2loop-2/compare/v1.2.2...v1.2.3) (2022-07-27)


### Bug Fixes

* added function to check if the filenames exist ([f7b6475](https://www.github.com/Loop3D/map2loop-2/commit/f7b6475333a74895644a3f6b19dcb3bd750f5fc0))
* black format ([314ee87](https://www.github.com/Loop3D/map2loop-2/commit/314ee87f5f8a266ac2ab724f0b3faff2bb89e20d))
* casting numeric columns as float ([2755546](https://www.github.com/Loop3D/map2loop-2/commit/275554669d70c5319d81fd58c1afd2497d02685c))
* normalising fault trace vector before comparing to dip direction ([bda0ddd](https://www.github.com/Loop3D/map2loop-2/commit/bda0dddfd6d4dee0cc6b347d62ac08da540671db))
* removing type hint for python 3.8 ([587441f](https://www.github.com/Loop3D/map2loop-2/commit/587441fb87b7fdf34ef6abe66cc1b771cf0d94c8))


### Documentation

* adding templates for issues ([2874b97](https://www.github.com/Loop3D/map2loop-2/commit/2874b97feb883078a5e7af7a8a86fd78ec76bada))
