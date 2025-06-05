# example_project.py

def unused_variable():
    a = 42  # Kullanılmayan değişken
    return True

def divide_by_zero():
    b = 1 / 0  # Sıfıra bölme hatası

def index_error():
    arr = [1, 2, 3]
    return arr[5]  # IndexError

def type_error():
    c = 'abc' + 10  # TypeError

def file_open():
    f = open("file.txt", "r")  # Dosya kapatılmıyor

def syntax_error()
    print("Eksik parantez")  # Syntax hatası

def always_false():
    if False:
        return "Should never happen"
    else:
        return

def no_exception_handling():
    return int("not a number")  # ValueError, yakalanmıyor

if __name__ == "__main__":
    unused_variable()
    divide_by_zero()
    index_error()
    type_error()
    file_open()
    syntax_error()
    always_false()
    no_exception_handling()
