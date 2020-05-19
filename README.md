# README

Generate model input data from geological maps. Revision of objectives in [https://github.com/Loop3D/map2loop](https://github.com/Loop3D/map2loop)

## Dependencies

If you wish to, create your own python virtual environment with the following modules to run the map2loop examples.

- python=3.7
- numpy
- pandas
- geopandas
- matplotlib
- rasterio
- networkx
- owslib
- pyamg
- descartes
- mplstereonet

## Build with Docker

Download and install the docker containerisation software and CLI [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

1. Clone this repo and navigate inside. 
2. Run the following command and click on the link Jupyter outputs to access the original [map2loop](https://github.com/Loop3D/map2loop) notebooks.

    ```bash
    docker-compose up
    ```

3. To jump into a bash shell in the container itself, open a new terminal and issue the following command. 

    ```bash
    docker exec -it map2loop-2_dev_1 bash
    ```

## Install via PyPi

Still to come...

### Bugs

### References