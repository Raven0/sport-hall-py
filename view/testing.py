import helper.AuthHelper as AuthHelper
time = AuthHelper.AuthHelper
asup= input()

if time.authVerification(asup):
    print("berhasil masuk")
else:
    print("ggagal")