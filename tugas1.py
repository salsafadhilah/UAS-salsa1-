def sa():
    print("modul nilai mahasiswa")
    
nama = raw_input("masukkan Nama Lengkap Anda  :")

uas = input("Masukkan NIlai UAS Anda     :")

uts = input("Masukkan Nilai UTS Anda     :")

tugas = input("Masukkan Nilai Tugas Anda   :")

akhir = input("Masukkan Nilai Akhir Anda   :")

print "\n HASIL NILAI AKHIR MAHASISWA \n<><><><><><><><><><><><><><><><><><>\n"

print "Nilai Anda Adalah          : %s"%nama
print "Nilai UAS Anda Adalah      : %d"%uas
print "Nilai UTS Anda Adalah      : %d"%uts
print "Nilai Tugas Anda Adalah    : %d"%tugas
print "Nilai Akhir Anda Adalah    : %d"%akhir

nilai= uas+uts+tugas+akhir
print "JUMLAH NILAI ANDA SEMUA    : %d"%nilai
print "NILAI HURUF ANDA ADALAH    : "

if nilai >= 80 :
    print "A"
elif nilai >= 70 :
    print "B"
elif nilai >= 60 :
    print "C"
elif nilai >= 40 :
    print "D"
elif nilai <= 30 :
    print "E"
if nilai <= 60 :
    print "KETERANGAN : GAGAL"
else :
    print "KETERANGAN : LULUS"

