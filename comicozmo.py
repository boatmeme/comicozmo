import cozmo
import random
import json
import re
from urllib.request import Request, urlopen
from urllib.parse import urlencode

jokeSources = [
    lambda: getJoke('https://icanhazdadjoke.com/')
]

intros = [
    'anim_cozmosays_speakloop_01',
    'anim_cozmosays_speakloop_02',
    'anim_cozmosays_speakloop_03',
]

punchlines = [
   'anim_pyramid_lookinplaceforfaces_short_head_angle_20',
   'anim_pyramid_lookinplaceforfaces_short_head_angle_40',
   'anim_bored_getout_01',
   'anim_neutral_eyes_01',
   'anim_mm_thinking',
]

reactions = [
    'anim_poked_giggle',
    'anim_gif_gleeserious_01',
    'anim_gif_no_01',
    'anim_poked_01',
    'anim_poked_giggle',
    'anim_peekaboo_success_03',
    'anim_reacttocliff_pickup_06'
]

splitRegex = re.compile('[.!?:]\s')

def getJoke(jokeUrl, query={}):
    queryStr = urlencode(query)
    req = Request(jokeUrl + '?' + queryStr, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'text/plain'})
    res = urlopen(req).read()
    return str(res, 'UTF-8')


def cozmo_program(robot: cozmo.robot.Robot):
    jokeStr = random.choice(jokeSources)()
    lineArr = splitRegex.split(jokeStr)
    print(jokeStr)

    for line in lineArr:
        if line == lineArr[-1]:
            robot.play_anim(name=random.choice(punchlines)).wait_for_completed()
        robot.say_text(line).wait_for_completed()

    robot.play_anim(name=random.choice(reactions)).wait_for_completed()
    intro = robot.play_anim(name=random.choice(intros)).wait_for_completed()

cozmo.run_program(cozmo_program)
