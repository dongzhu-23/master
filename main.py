#主函数

import compress
import huffman_tree
import huffman_code

def main():
    input_file = "input.txt"
    encoded_file = "encoded.txt"
    decoded_file = "decoded.txt"

    # 压缩
    print("Compressing...")
    codes, root = compress.compress_file(input_file, encoded_file)
    print("Compression finished. Encoded file:", encoded_file)

    # 解压缩
    print("Decompressing...")
    compress.decompress_file(encoded_file, decoded_file, root)
    print("Decompression finished. Decoded file:", decoded_file)

if __name__ == "__main__":
    main()
