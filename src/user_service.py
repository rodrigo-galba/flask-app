class UserService:
    users_list = []

    def __init__(self):
        print("initializing")

    def create(self, user):
        index = len(UserService.users_list) + 1

        user['id'] = index

        UserService.users_list.append(user)

        return user

    def list(self):
        return UserService.users_list

    def delete(self):
        total = len(UserService.users_list)
        if total == 0:
            return {}

        user = UserService.users_list.pop(0)
        return user
