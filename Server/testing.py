import Password_work
import Face_code.face_verification

str_img = Face_code.face_verification.check_image()

if str_img:
    # tell what password on what user to save and encrypt
    Password_work.encrypt("sdf", "password", "te", str_img, "parola", "user_2")
    print(Password_work.decrypt("sdf", "te", str_img, "user_2", "parola"))
    print(Password_work.check_password("sdf", "te", str_img, "user_2", "parola"))
    print(Password_work.common_used_passwords("sdf", "te", str_img, "user_2", "parola"))
