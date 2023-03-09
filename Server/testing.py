import Password_work
import Face_code.face_verification

str = Face_code.face_verification.check_image()
if str:
    Password_work.encrypt("test", "password", "website", str)
    print(Password_work.decrypt("test", "website", str))