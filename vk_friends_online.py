import vk
from getpass import getpass


APP_ID = 6964099
VERSION_API = '5.95'


def get_user_login():
    login = input('Please enter your login: ')
    return login


def get_user_password():
    password = getpass('Please enter your password: ')
    return password


def get_vk_api(login, password):

    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=VERSION_API)
    return api


def get_online_friends(api):

    id_friends_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=id_friends_online)

    return friends_online


def output_friends_to_console(friends_online):
    if friends_online:
        print('Online friends')
        for friend in friends_online:
            print('{} {}'.format(friend['last_name'], friend['first_name']))
    else:
        print('No online friends')


def main():
    login = get_user_login()
    password = get_user_password()
    try:
        api = сonnect_to_account(login, password)
        friends_online = get_online_friends(api)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        pass


if __name__ == '__main__':
    main()
