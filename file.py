import json

class Jsonku:
    def __init__(self, nama_file):
        self.nama_file = nama_file

    def baca(self):
        try:
            with open(self.nama_file, 'r') as file:
                data = json.load(file) 
                print(json.dumps(data, indent=4)) 
        except Exception as e:
            print(f"Error: {e}")

    def tulis(self):
        try:
            with open(self.nama_file, 'r') as file:
                data = json.load(file)
            if not isinstance(data, list):
                data = [data]
    
            print("Data saat ini:")
            print(json.dumps(data, indent=4))
    
            judul = input("Masukkan judul: ")
            pengarang = input("Masukkan pengarang: ")
            tahun_terbit = int(input("Masukkan tahun terbit (angka): "))
    
            data.append({"judul": judul, "pengarang": pengarang, "tahun_terbit": tahun_terbit})
    
            with open(self.nama_file, 'w') as file:
                json.dump(data, file, indent=4)
            print("Data berhasil ditulis.")
        except Exception as e:
            print(f"Error: {e}")

    def edit(self):
        try:
            with open(self.nama_file, 'r') as file:
                data = json.load(file)
                print("Data saat ini:")
                print(json.dumps(data, indent=4))
    
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return
    
            index = int(input("Masukkan indeks baris yang ingin diperbarui (mulai dari 0): "))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return
    
            key_to_update = input("Masukkan kunci yang ingin diperbarui (judul/pengarang/tahun_terbit): ")
            if key_to_update not in data[index]:
                print(f"Kunci {key_to_update} tidak ditemukan.")
                return
    
            if key_to_update == "tahun_terbit":
                try:
                    new_value = int(input("Masukkan nilai baru (angka): "))
                except ValueError:
                    print("Nilai harus berupa angka.")
                    return
            else:
                new_value = input("Masukkan nilai baru: ")
    
            data[index][key_to_update] = new_value
            with open(self.nama_file, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"{key_to_update} berhasil diperbarui.")
        except Exception as e:
            print(f"Error: {e}")

    def hapus(self):
        try:
            with open(self.nama_file, 'r') as file:
                data = json.load(file)
                print("Data saat ini:")
                print(json.dumps(data, indent=4))
                
            if not isinstance(data, list):
                print("Data tidak dalam format list.")
                return

            index = int(input("Masukkan indeks baris yang ingin dihapus (mulai dari 0): "))
            if index < 0 or index >= len(data):
                print("Indeks tidak valid.")
                return

            del data[index]
            with open(self.nama_file, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data pada baris {index} berhasil dihapus.")
        except Exception as e:
            print(f"Error: {e}")