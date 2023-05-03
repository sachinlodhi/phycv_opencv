
# OpenCV Implementation of Phycv Library

This project is an OpenCV implementation of the Phycv library. It allows you to take live feed from the camera and apply Vevid, PST, and Page algorithms. You can also change various parameters on live feed and see the results. Please note that this implementation only supports the CPU version and does not include support for the GPU version.

## Installation

To use this project, please ensure you have the following dependencies installed:

- matplotlib==3.5.2
- numpy==1.21.5
- opencv_contrib_python==4.6.0.66
- phycv==1.2.5
- torch==2.0.0

You can install these dependencies using the following command:

```
pip install -r requirements.txt
```

Sure, here's an updated usage section for your project's README:

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/sachinlodhi/phycv_opencv.git
   ```
2. Navigate to the project directory:
   ```
   cd phycv_opencv
   ```
3. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the main Python script to open the live camera feed and apply the VeVID, PST, and Page algorithms:
   ```
   python main.py
   ```
5. Adjust the parameters using the trackbars provided in the windows to see the effect on the output.

Note: The Page algorithm output is not fully implemented and won't be shown. All the four windows namely input image, VeVID operation, PST operation and Page operation will be shown at once. The implementation is done for CPU version only and GPU version is not implemented yet.

## Contributing

This project is open to contributions. If you have any suggestions or ideas on how to improve this implementation, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contribution
For more information on the phycv library, you can refer to the original research paper at [paper](https://arxiv.org/abs/2301.12531) and the GitHub repository at [JalaliLab](https://github.com/JalaliLabUCLA/phycv).
