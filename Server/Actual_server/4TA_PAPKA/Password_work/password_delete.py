import json
import os


def delete_password(user, website, username):
    path_for_file = os.path.dirname(os.path.abspath(__file__))
    path_for_file += r"/Database/new_database/" + str(username) + ".json"

    if(os.path.exists(path_for_file)):
        file = open(path_for_file, "r")
        if os.path.getsize(path_for_file) > 0:
            data = file.read()
            data = json.loads(data)
            if (user in data):
                if(website in data[user]):
                    del data[user][website]
                    file.close()
                    file = open(path_for_file, "w")
                    file.write(json.dumps(data))
                    file.close()
                    return True
                else:
                    file.close()
                    return False
            else:
                file.close()
                return False
        else:
            file.close()
            return False