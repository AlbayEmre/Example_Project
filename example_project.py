import os

def unused_variables_and_dead_code():
    x = 100  # Kullanılmayan değişken
    y = 0
    if False:
        print("Asla çalışmayacak kod")

def division_by_zero_handling():
    try:
        result = 10 / 0  # Sıfıra bölme
    except ZeroDivisionError as e:
        print(f"Hata: {e}")

def file_operations_with_leak():
    f = open("example.txt", "w")  # Dosya kapatılmıyor
    f.write("Merhaba dünya")  # Dosya düzgün kapatılmadığı için sorun olabilir

def unsafe_type_operations():
    value = "123"
    result = value + 10  # TypeError

def unsafe_index_access():
    lst = [1, 2, 3]
    return lst[10]  # IndexError

def unsafe_conversion():
    num = int("oniki")  # ValueError

def poor_exception_handling():
    try:
        risky = [][2]
    except:
        pass  # Kötü uygulama: ne hata olduğu bilinmiyor

def missing_import_usage():
    # math modülünü import etmedik
    return math.sqrt(16)  # NameError

def infinite_loop():
    while True:
        break  # Sadece örnek, gerçek sonsuz döngü olmaması için break

def logic_bug():
    is_logged_in = False
    if is_logged_in:
        return "Hoş geldiniz!"
    else:
        return "Giriş yapıldı"  # Mantıksal hata: yanlış mesaj

def no_return_function():
    a = 10 + 5  # Değer dönmüyor

# syntax error: print("Eksik parantez"  # bu yorum satırında

if __name__ == "__main__":
    unused_variables_and_dead_code()
    division_by_zero_handling()
    file_operations_with_leak()
    unsafe_type_operations()
    unsafe_index_access()
    unsafe_conversion()
    poor_exception_handling()
    missing_import_usage()
    infinite_loop()
    logic_bug()
    no_return_function()
