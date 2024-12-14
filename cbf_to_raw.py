import fabio  # Library for reading various image formats including CBF
import numpy as np  # Library for numerical computations
import os  # Library for file path manipulations

def cbf_to_raw(file_path, output_dir):
    # Open the CBF file using fabio
    cbf_image = fabio.open(file_path)
    # Extract the image data as a numpy array
    data = cbf_image.data

    # Extract the base file name without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Create output file path for little-endian RAW format
    output_file_le = os.path.join(output_dir, f"{base_name}_s32le-1x2463x2527.raw")
    # Convert data to 32-bit signed integers and save in little-endian format
    data.astype(np.int32).tofile(output_file_le)

    # Convert data to big-endian format by byteswapping
    data_be = data.astype(np.int32).byteswap().newbyteorder()
    # Create output file path for big-endian RAW format
    output_file_be = os.path.join(output_dir, f"{base_name}_s32be-1x2463x2527.raw")
    # Save the big-endian formatted data to file
    data_be.tofile(output_file_be)

if __name__ == "__main__":
    # Define input CBF file path and output directory
    input_file = "/media/arnau/Data/MX_data/D1/1_1_0001.cbf"
    output_dir = "/media/arnau/Data/converted_data/D1"

    # Call the conversion function
    cbf_to_raw(input_file, output_dir)
