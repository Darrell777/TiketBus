from os import system
from time import sleep
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Penyimpanan Data Penumpang Sederhana
	[1]. Lihat Semua Data Penumpang
	[2]. Tambah Data Penumpang Baru
	[3]. Cari Data Penumpang
	[4]. Hapus Data Penumpang
	[5]. Update Data Penumpang
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)
 
def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False
def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_contact=None, telp=True, alamat=True, all_data=False):
	if id_contact != None and all_data == False:
		print(f"ID : {id_contact}")
		print(f"NAMA : {contacts[id_contact]['nama']}")
		print(f"TELP : {contacts[id_contact]['telp']}")
		print(f"ALAMAT : {contacts[id_contact]['alamat']}")
	elif alamat == False and all_data == False:
		print(f"ID : {id_contact}")
		print(f"NAMA : {contacts[id_contact]['nama']}")
		print(f"TELP : {contacts[id_contact]['telp']}")
	elif all_data == True:
		for id_contact in contacts:
			nama = contacts[id_contact]["nama"]
			telp = contacts[id_contact]["telp"]
			alamat = contacts[id_contact]["alamat"]
			print(f"ID : {id_contact} - NAMA : {nama} - TELP : {telp} - Alamat : {alamat}")

def view_contacts():
	print_header("DAFTAR DATA PENUMPANG YANG TERSIMPAN")
	if not_empty(contacts):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA DATA PENUMPANG YANG TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_contact(name, phone):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day
 
	counter = len(contacts) + 1
	first = name[0].upper()
	last_4 = phone[-4:]
 
	id_contact = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_contact

def add_contact():
	print_header("MENAMBAHKAN DATA PENUMPANG BARU")
	nama = input("NAMA \t: ")
	telp = input("TELP \t: ")
	alamat = input("ALAMAT \t: ")
	respon = input(f"Apakah yakin ingin membuat data : {nama} ? (Y/N) ")
	if verify_ans(respon):
		id_contact = create_id_contact(name=nama, phone=telp)
		contacts[id_contact] = {
			"nama" : nama,
			"telp" : telp,
			"alamat" : alamat
		}
		print("Data Penumpang Tersimpan.")
	else:
		print("Data Penumpang Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_name(contact):
	for id_contact in contacts:
		if contacts[id_contact]['nama'] == contact:
			return id_contact
	else:
		return False

def find_contact():
	print_header("MENCARI DATA PENUMPANG")
	nama = input("Nama Penumpang yang Dicari : ")
	exists = searching_by_name(nama)
	if exists:
		print("Data Penumpang Ditemukan")
		print_data(id_contact=exists)
	else:
		print("Data Penumpang Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_contact():
	print_header("MENGHAPUS DATA PENUMPANG")
	nama = input("Nama Penumpang yang akan Dihapus : ")
	exists = searching(nama)
	if exists:
		print_data(contact=nama)
		respon = input(f"Yakin ingin menghapus {nama} ? (Y/N) ")
		if verify_ans(respon):
			del contacts[nama]
			print("Data Penumpang Telah Dihapus")
		else:
			print("Data Penumpang Batal Dihapus")
	else:
		print("Data Penumpang Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
 
def update_contact_nama(contact):
	print(f"Nama Lama : {contact}")
	new_name = input("Masukkan Nama baru : ")
	respon = input("Apakah yakin data Penumpang ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		contacts[new_name] = contacts[contact]
		del contacts[contact]
		print("Data Penumpang Telah di simpan")
		print_data(new_name)
	else:
		print("Data Penumpang Batal diubah")

def update_contact_telp(contact):
	print(f"Nomor Telpon Lama : {contacts[contact]['telp']}")
	new_telp = input("Masukkan Nomor Telepon Baru : ")
	respon = input("Apakah yakin data Penumpang ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		contacts[contact]['telp'] = new_telp
		print("Data Penumpang Telah di simpan")
		print_data(contact)
	else:
		print("Data Penumpang Batal diubah")

def update_contact_hobi(contact):
	print(f"Alamat Lama : {contacts[contact]['alamat']}")
	new_alamat = input("Masukkan Alamat Baru : ")
	respon = input("Apakah yakin data Penumpang ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		contacts[contact]['alamat'] = new_telp
		print("Data Penumpang Telah di simpan")
		print_data(contact)
	else:
		print("Data Penumpang Batal diubah")

def update_contact():
	print_header("MENGUPDATE DATA PENUMPANG")
	nama = input("Nama Penumpang yang akan di-update : ")
	exists = searching(nama)
	if exists:
		print_data(nama)
		print("EDIT FIELD [1] NAMA - [2] TELP - [3] ALAMAT")
		respon = input("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_contact_nama(nama)
		elif respon == "2":
			update_contact_telp(nama)
		elif respon == "3":
			update_contact_alamat(nama)
	else:
		print("Data Penumpang Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_contacts()
	elif char == "2":
		add_contact()
	elif char == "3":
		find_contact()
	elif char == "4":
		delete_contact()
	elif char == "5":
		update_contact()

contacts = {
	"20201007-C001D6288" : {
		"nama" : "Darel",
		"telp" : "081241806288",
		"alamat" : "Jl. Musi Raya"
	},
	"20201008-C002G1059" : {
		"nama" : "Gede",
		"telp" : "081367631059",
		"alamat" : "Komplek Grand Garden"
	}
}
stop = False
 
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)