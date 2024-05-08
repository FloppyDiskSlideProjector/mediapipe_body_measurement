Body parts size measurement with media pipe pose detection 
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

# Get started
## clone
- `git clone https://github.com/FloppyDiskSlideProjector/mediapipe_body_measurement`

## install requirements
- `pip install -r requirements.txt`

## update environment
### this step will update some factors such as scale for your real wrold environment.
- Take a picture of chess board image in real world. that image will be the criteria of measuring the length.
- Place the picture file into `data/resoource` with name `chess_bord.jpeg`.
- Run the command `python main.py --action update_environment`

# run
## update environment: 
### Once the update environment above is done, this step is unnecessary unless you change the environment because program will remember most recent environment update
### if you want new environment, this step is likely necessary for accurate measurement
- Just like above, place the picture file into `data/resoource` with name `chess_bord.jpeg`.
- Type `python main.py --action update_environment` to update and prepare image correction
- Picture of chess board image with same environment such as same camera, same angle, same distance, and so an...

## measure
### iamge of a person to measure the body length is needed
- Take a picture of person who's body length will be measured.
- Environment of taking picture should be same as taking chess board. Same environment such as same camera, same angle, same distance, and so an...
- Place the image into `data/image` with name `sample.jpg`
- run the command `python main.py` or `python main.py --action measure`

## output and customize
### First it shows up the plotted image of body part
- if you don't want, you can remove the `plot_points(detection_result = detection_result)` line in `main.py` measurement function
### Next it prints result of measurement
- `measure` function in `main.py` prints the result of `get_measurement` function which is dictionary type. You can manipulate the result of `get_measurement` to customize
### Update the path or name of the file can be done easily
- `scripts/options.py` file contains many information and path that the program will use. Change the file path or file name can be easily done by changing the lines of `options.py`

## caution
### Operating System
- This has been tested in window and linux(Ubuntu). May not work correctly in other environment
### Accuracy and size of chess board
- Size of chess board to setup may effect accuracy. I used letter paper size chess board so there was a little gap between real life and measurement.
- I added additional scale to fill out the gap between real world length and measurement from chess board but if very big chess board is used, `real_life_x_scale` and `real_life_y_scale` may useless and maybe working wrong direction.
- If big chess board is used but there was too much gap between real world length and measurement, set `real_life_x_scale` and `real_life_y_scale` as 1 could be the solution.
