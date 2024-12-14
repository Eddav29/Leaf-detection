import requests

# URL server Flask yang berjalan
URL = "http://127.0.0.1:5001/predict"

# Path ke gambar yang akan dites
TEST_IMAGE_PATH = "test_image.jpg"

def test_prediction_api():
    """
    Mengirim gambar ke endpoint Flask dan mengecek respons.
    """
    # Membuka gambar sebagai file
    with open(TEST_IMAGE_PATH, 'rb') as img_file:
        files = {'file': img_file}

        # Mengirim POST request ke API Flask
        response = requests.post(URL, files=files)

        # Menampilkan respons
        if response.status_code == 200:
            print("Prediksi Berhasil!")
            print("Hasil Respons:")
            print(response.json())  # Output JSON dari API Flask
        else:
            print(f"Error! Status code: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    # Jalankan fungsi test
    print("Testing Flask API...")
    test_prediction_api()
