import Password_work
import Face_code.face_verification

str_img = Face_code.face_verification.check_image()
if str_img:
    Password_work.encrypt("sdfg", "ssword", "te", str_img)
    print(Password_work.decrypt("sdfg", "te", str_img))