#文件的压缩和解压缩

import huffman_tree
import huffman_code
import file_io


def compress_file(input_filename, output_filename):
    # 读取文件内容
    data = file_io.read_file(input_filename)

    # 统计频率
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # 构建哈夫曼树并生成哈夫曼编码
    root = huffman_tree.build_huffman_tree(data, freq)
    codes = huffman_code.generate_huffman_codes(root)

    # 编码文件内容
    encoded_data = huffman_code.encode(data, codes)

    # 将编码后的数据写入文件
    file_io.write_file(output_filename, encoded_data)
    return codes, root


def decompress_file(encoded_filename, output_filename, root):
    # 读取编码文件
    encoded_data = file_io.read_file(encoded_filename)

    # 解码数据
    decoded_data = huffman_code.decode(encoded_data, root)

    # 将解码后的数据写入文件
    file_io.write_file(output_filename, decoded_data)
