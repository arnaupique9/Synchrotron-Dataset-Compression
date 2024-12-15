import enb
import os

# File to be compressed
input_file = "data/D1/1_1_0001_s32be-1x2463x2527.raw"
compressed_output_dir = "results/compressed/"
reconstructed_output_dir = "results/original/"

# Import codecs
from plugins.arithmetic_codec.arithmetic_codec import ArithmeticCodec
from plugins.bwt.bwt_codec import BWT
from plugins.fse.fse_codec import FSE
from plugins.fse.huffman_codec import FSEHuffman
from plugins.huffman.huffman_codec import HuffmanCodec
from plugins.lpaq8.lpaq8_codec import LPAQ8
from plugins.lz4.lz4_codec import Lz4
from plugins.rle.rle_codec import RLECodec
from plugins.zfp.zfp_codec import Zfp
from plugins.zip.zip_codecs import LZ77Huffman
from plugins.zip.zip_codecs import BZIP2
from plugins.zstd.zstd_codec import Zstandard

# Define the codecs will use
codecs = [
    ArithmeticCodec(),
    BWT(),
    FSE(),
    FSEHuffman(),
    HuffmanCodec(),
    LPAQ8(),
    Lz4(compression_level=9),
    RLECodec(packbits=True),
    Zfp(),
    LZ77Huffman(compression_level=9),
    BZIP2(compression_level=9),
    Zstandard(compression_level=22),
]

# Define and execute the compression experiment
exp = enb.icompression.LosslessCompressionExperiment(
    codecs=codecs,
    dataset_paths=[input_file],
    compressed_copy_dir_path=compressed_output_dir,
    reconstructed_dir_path=reconstructed_output_dir
)

# Execute the experiment
df = exp.get_df()

