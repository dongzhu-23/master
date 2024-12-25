#生成哈夫曼编码和解码

def generate_huffman_codes(root):
    codes = {}

    def _generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        _generate_codes(node.left, current_code + "0")
        _generate_codes(node.right, current_code + "1")

    _generate_codes(root, "")
    return codes


def encode(data, codes):
    return ''.join(codes[char] for char in data)


def decode(encoded_data, root):
    decoded_data = []
    current_node = root
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root
    return ''.join(decoded_data)
