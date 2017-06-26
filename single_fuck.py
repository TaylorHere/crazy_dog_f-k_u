from time import sleep
from random import choice,randint
def single_fuck(client, settings, fuck_rull):
    # use the rull start the fuck
    ##创建关注关系
    # for you in fuck_rull.fuck_you:
    #     client.post('friendships/create',screen_name=you.screen_name)
    try:
        # get home timeline and statues ids
        timeline = client.get('statuses/home_timeline')
        statuses = timeline['statuses']
        statuses_ids = [status['id'] for status in statuses if status['user']['screen_name'] in fuck_rull.fuck_you]
        for status_id in statuses_ids:
            # fuck every status
            if 'status' in fuck_rull.fuck_mode:
                fuck_you = choice(fuck_rull.f_words)
                skip_words = choice(fuck_rull.skip_words)
                fuck_word = fuck_you.text+skip_words
                print('sleep for weibo limit %s s' % randint(0,settings.api_limit_time))
                sleep(randint(0,settings.api_limit_time))
                try:
                    client.post('comments/create',comment=fuck_word,id=status_id)
                    print('fuck a status')
                except Exception as e:
                    print('rate limit ,script running...')
            # fuck every comments
            if 'comment' in fuck_rull.fuck_mode:
                # get every coments in the statues
                comments = client.get('comments/show',id=status_id)
                if comments != '':
                    coment_ids = [coment['id'] for coment in comments['comments']]
                    for coment_id in coment_ids:
                        fuck_you = choice(fuck_rull.f_words)
                        skip_words = choice(fuck_rull.skip_words)
                        fuck_word = fuck_you.text+skip_words
                        print('sleep for weibo limit %s s' % randint(0,settings.api_limit_time))
                        sleep(randint(0,settings.api_limit_time))
                        try:
                            client.post('comments/reply',comment=fuck_word,id=status_id,cid=coment_id)
                            print('fuck a coment')
                        except Exception as e:
                            print('rate limit ,script running...')
    except Exception as e:
        raise Exception('get home timeline err')