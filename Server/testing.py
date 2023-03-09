import Password_work
import Face_code.face_verification

str_img = Face_code.face_verification.check_image()
if str_img:
    file = open("Password_work/database.json", "r")
    new_json = Password_work.encrypt("sdf", "sord", "te", str_img, file.read())
    file.close()
    file = open("Password_work/database.json", "w")
    file.write(new_json)
    file.close()
    file = open("Password_work/database.json", "r")
    print(Password_work.decrypt("sdf", "te", str_img, file.read()))
    print(Password_work.check_password("sdf", "te", str_img, file.read()))
    file.close()
