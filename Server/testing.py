import Password_work
import Face_code.face_verification

str_img = Face_code.face_verification.check_image()
if str_img:
    file = open("Password_work/database.json", "r")
    # tell what password on what user to save and encrypt
    new_json = Password_work.encrypt("sdf", "password", "te", str_img, file.read())
    file.close()
    file = open("Password_work/database.json", "w")
    file.write(new_json)
    file.close()
    file = open("Password_work/database.json", "r")
    test = file.read()
    # tell what password on what user to decrypt
    print(Password_work.decrypt("sdf", "te", str_img, test))
    print(Password_work.check_password("sdf", "te", str_img, test))
    print(Password_work.common_used_passwords("sdf", "te", str_img, test))
    file.close()
