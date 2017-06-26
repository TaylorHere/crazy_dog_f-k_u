import json
import threading
from weibo import Client
from types import SimpleNamespace as Namespace
from single_fuck import single_fuck

def json_to_namedSpace(data):
    """
    convert json object to namedtuple
    """
    return json.loads(data, object_hook=lambda d: Namespace(**d))

def load_settings(settings_file_name):
    """
    load settings for init client
        or
    load rull for start fuck
    """
    with open(settings_file_name) as f:
        json = f.read()
    return json_to_namedSpace(json)

def client_init(settings):
    """
    use settings init the clients.
    """
    clients = []
    for user in settings.users:
        if 'api_secret' in dir(user):
            c = Client(user.app_key,
                user.api_secret,
                user.redirect_uri,
                username=user.username,
                password=user.password)
            clients.append(c)
        else:
            c = Client(settings.app_key,
                settings.api_secret,
                settings.redirect_uri,
                username=user.username,
                password=user.password)
            clients.append(c)
    return clients


def main():
    """
    single fuck:
        load settings first
        then init client
        then use client fuck the weibo
    if only one user
        use the single fuck
    else
        make a thread use sinle fuck, and change the client
    """
    # './fuck_rull.json'
    try:
        settings = load_settings('./user_configs.json')
    except Exception as e:
        raise Exception('load settings err')
    finally:

        try:
            rulls = load_settings('./fuck_rull.json')
        except Exception as e:
            raise Exception('load rulls err')
        finally:

            try:
                clients = client_init(settings)
            except Exception as e:
                raise Exception('load clients err')
            finally:
                print('you have %d users in this fuck' % len(clients))
                for index, client in enumerate(clients):
                    t = threading.Thread(target=single_fuck,args=(client,settings,rulls))
                    t.setDaemon(True)
                    print('fucker %d start' % (index+1))
                    t.start()
                t.join()

if __name__ == '__main__':
    main()