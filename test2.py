import struct

def decode_raw_audio(filename):
    with open(filename, 'rb') as file:
        raw_data = file.read()

    # Decode raw audio data to integers
    decoded_data = []
    print(len(raw_data))
    for i in range(0, len(raw_data), 2):
        sample = struct.unpack('<h', raw_data[i:i+2])[0]  # Assuming little-endian signed 16-bit integers
        decoded_data.append(sample)

    return decoded_data

def main():
    filename = "output6/output_audio_000000.raw"
    decoded_data = decode_raw_audio(filename)
    print(decoded_data)

if __name__ == "__main__":
    main()
