def read_raw_audio(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return raw_data

if __name__ == "__main__":
    file_path = "output2/output_audio_000000.raw"
    raw_audio_data = read_raw_audio(file_path)
    print(raw_audio_data)
