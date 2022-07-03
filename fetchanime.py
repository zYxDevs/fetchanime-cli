import os
import webbrowser
import json
from anikimiapi import AniKimi
from colorama import Fore

with open('settings.json', 'r') as f:
    settings = json.load(f)

anime = AniKimi(
    gogoanime_token=settings['gogoanime_token'],
    auth_token=settings['auth_token'],
    host=settings['host']  
)

os.system('cls')
print(f'''
,--.     .       .    ,.                  
|        |       |   /  \     o           
|-   ,-. |-  ,-. |-. |--| ;-. . ;-.-. ,-. 
|    |-' |   |   | | |  | | | | | | | |-' 
'    `-' `-' `-' ' ' '  ' ' ' ' ' ' ' `-'                           

{Fore.YELLOW}Author: {Fore.WHITE}Profility
{Fore.YELLOW}Description: {Fore.WHITE}CLI Tool that searches for anime in GoGoAnime and retrieves sources using AniKimi API.                                                                                                                                                            ''')

if __name__ == '__main__':
    input_query = input(f"{Fore.CYAN}Search Anime => {Fore.WHITE}")
    results_list = []
    count = 0
    try:
        results = anime.search_anime(query=input_query)
    except:
        print(f'{Fore.RED}ERROR: Failed to get search results, please try again.')
        exit()

    for i in results:
        print(f" {Fore.GREEN}[{count}] {Fore.WHITE}{i.title}")
        results_list.append(i.animeid)
        count = count + 1

    input_anime = input(f"{Fore.CYAN}Choose Anime => {Fore.WHITE}")
    if not input_anime.isdigit():
        print(
            f'{Fore.RED}ERROR: Chosen anime is not an integer, please choose a number.'
        )

        exit()
    if int(input_anime) not in range(len(results_list)):
        print(f'{Fore.RED}ERROR: Chosen anime is not in range.')
        exit()

    resultsid = results_list[int(input_anime)]
    details = anime.get_details(animeid=resultsid)

    input_episode = input(f"{Fore.CYAN}Choose Episode (1-{details.episodes}) => {Fore.WHITE}")
    if not input_episode.isdigit():
        print(
            f'{Fore.RED}ERROR: Chosen episode is not an integer, please choose a number.'
        )

        exit()
    if int(input_episode) not in range(details.episodes + 1):
        print(f'{Fore.RED}ERROR: Chosen episode is not in range.')
        exit()

    anime_link = anime.get_episode_link_basic(animeid=resultsid, episode_num=input_episode)

    streamtapelink = anime_link.link_streamtape
    streamsblink = anime_link.link_streamsb
    xstreamcdnlink = anime_link.link_xstreamcdn
    mixdroplink = anime_link.link_mixdrop
    mp4uploadlink = anime_link.link_mp4upload
    doodstreamlink = anime_link.link_doodstream
    gogolink = f"https://gogoanime.vc/{resultsid}-episode-{input_episode}"
    animixplaylink = f"https://animixplay.to/v1/{resultsid}/ep{input_episode}"

    print(f'{Fore.GREEN} [0]{Fore.WHITE} StreamTape: {streamtapelink}\n{Fore.GREEN} [1]{Fore.WHITE} StreamUSB: {streamsblink}\n{Fore.GREEN} [2]{Fore.WHITE} XStreamCDN: {xstreamcdnlink}\n{Fore.GREEN} [3]{Fore.WHITE} MixDrop: {mixdroplink}\n{Fore.GREEN} [4]{Fore.WHITE} Mp4Upload: {mp4uploadlink}\n{Fore.GREEN} [5]{Fore.WHITE} DoodStream: {doodstreamlink}\n{Fore.GREEN} [6]{Fore.WHITE} GoGoAnime: {gogolink}\n{Fore.GREEN} [7]{Fore.WHITE} AniMixPlay: {animixplaylink}')
    input_source = input(f"{Fore.CYAN}Choose Source => {Fore.WHITE}")
    if not input_source.isdigit():
        print(
            f'{Fore.RED}ERROR: Chosen source is not an integer, please choose a number.'
        )

        exit()
    if int(input_source) not in range(7 + 1):
        print(f'{Fore.RED}ERROR: Chosen source is not in range.')
        exit()

    if input_source == '0':
        if streamtapelink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(streamtapelink)
    if input_source == '1':
        if streamsblink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(streamsblink)
    if input_source == '2':
        if xstreamcdnlink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(xstreamcdnlink)
    if input_source == '3':
        if mixdroplink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(mixdroplink)
    if input_source == '4':
        if mp4uploadlink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(mp4uploadlink)
    if input_source == '5':
        if doodstreamlink == "None":
            print(f'{Fore.RED}ERROR: Chosen source has no value.')
            exit()
        webbrowser.open(doodstreamlink)
    if input_source == '6':
        webbrowser.open(gogolink)
    if input_source == '7':
        webbrowser.open(animixplaylink)