#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import time
import requests

# Constants
BRAZIL = 'br'
EUROPE_NORDIC_EAST = 'eune'
EUROPE_WEST = 'euw'
KOREA = 'kr'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
NORTH_AMERICA = 'na'
OCEANIA = 'oce'
RUSSIA = 'ru'
TURKEY = 'tr'

# Platforms
platforms = {
    BRAZIL: 'BR1',
    EUROPE_NORDIC_EAST: 'EUN1',
    EUROPE_WEST: 'EUW1',
    KOREA: 'KR',
    LATIN_AMERICA_NORTH: 'LA1',
    LATIN_AMERICA_SOUTH: 'LA2',
    NORTH_AMERICA: 'NA1',
    OCEANIA: 'OC1',
    RUSSIA: 'RU',
    TURKEY: 'TR1'
}

queue_types = [
    'CUSTOM',  # Custom games
    'NORMAL_5x5_BLIND',  # Normal 5v5 blind pick
    'BOT_5x5',  # Historical Summoners Rift coop vs AI games
    'BOT_5x5_INTRO',  # Summoners Rift Intro bots
    'BOT_5x5_BEGINNER',  # Summoner's Rift Coop vs AI Beginner Bot games
    'BOT_5x5_INTERMEDIATE',  # Historical Summoner's Rift Coop vs AI Intermediate Bot games
    'NORMAL_3x3',  # Normal 3v3 games
    'NORMAL_5x5_DRAFT',  # Normal 5v5 Draft Pick games
    'ODIN_5x5_BLIND',  # Dominion 5v5 Blind Pick games
    'ODIN_5x5_DRAFT',  # Dominion 5v5 Draft Pick games
    'BOT_ODIN_5x5',  # Dominion Coop vs AI games
    'RANKED_SOLO_5x5',  # Ranked Solo 5v5 games
    'RANKED_PREMADE_3x3',  # Ranked Premade 3v3 games
    'RANKED_PREMADE_5x5',  # Ranked Premade 5v5 games
    'RANKED_TEAM_3x3',  # Ranked Team 3v3 games
    'RANKED_TEAM_5x5',  # Ranked Team 5v5 games
    'BOT_TT_3x3',  # Twisted Treeline Coop vs AI games
    'GROUP_FINDER_5x5',  # Team Builder games
    'ARAM_5x5',  # ARAM games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1v1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2v2 games
    'SR_6x6',  # Hexakill games
    'URF_5x5',  # Ultra Rapid Fire games
    'BOT_URF_5x5',  # Ultra Rapid Fire games played against AI games
    'NIGHTMARE_BOT_5x5_RANK1',  # Doom Bots Rank 1 games
    'NIGHTMARE_BOT_5x5_RANK2',  # Doom Bots Rank 2 games
    'NIGHTMARE_BOT_5x5_RANK5',  # Doom Bots Rank 5 games
    'ASCENSION_5x5',  # Ascension games
    'HEXAKILL',  # 6v6 games on twisted treeline
    'KING_PORO_5x5',  # King Poro game games
    'COUNTER_PICK',  # Nemesis games,
    'BILGEWATER_5x5',  # Black Market Brawlers games
]

game_maps = [
    {'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
    {'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
    {'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
    {'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
    {'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
    {'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
    {'map_id': 11, 'name': "Summoner's Rift", 'notes': "Current Version"},
    {'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
    {'map_id': 14, 'name': "Butcher's Bridge", 'notes': "ARAM Map"},
]

game_modes = [
    'CLASSIC',  # Classic Summoner's Rift and Twisted Treeline games
    'ODIN',  # Dominion/Crystal Scar games
    'ARAM',  # ARAM games
    'TUTORIAL',  # Tutorial games
    'ONEFORALL',  # One for All games
    'ASCENSION',  # Ascension games
    'FIRSTBLOOD',  # Snowdown Showdown games
    'KINGPORO',  # King Poro games
]

game_types = [
    'CUSTOM_GAME',  # Custom games
    'TUTORIAL_GAME',  # Tutorial games
    'MATCHED_GAME',  # All other games
]

sub_types = [
    'NONE',  # Custom games
    'NORMAL',  # Summoner's Rift unranked games
    'NORMAL_3x3',  # Twisted Treeline unranked games
    'ODIN_UNRANKED',  # Dominion/Crystal Scar games
    'ARAM_UNRANKED_5v5',  # ARAM / Howling Abyss games
    'BOT',  # Summoner's Rift and Crystal Scar games played against AI
    'BOT_3x3',  # Twisted Treeline games played against AI
    'RANKED_SOLO_5x5',  # Summoner's Rift ranked solo queue games
    'RANKED_TEAM_3x3',  # Twisted Treeline ranked team games
    'RANKED_TEAM_5x5',  # Summoner's Rift ranked team games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1x1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2x2 games
    'SR_6x6',  # Hexakill games
    'CAP_5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URF_BOT',  # Ultra Rapid Fire games against AI
    'NIGHTMARE_BOT',  # Nightmare bots
    'ASCENSION',  # Ascension games
    'HEXAKILL',  # Twisted Treeline 6x6 Hexakill
    'KING_PORO',  # King Poro games
    'COUNTER_PICK',  # Nemesis games
    'BILGEWATER',  # Black Market Brawlers games
]

player_stat_summary_types = [
    'Unranked',  # Summoner's Rift unranked games
    'Unranked3x3',  # Twisted Treeline unranked games
    'OdinUnranked',  # Dominion/Crystal Scar games
    'AramUnranked5x5',  # ARAM / Howling Abyss games
    'CoopVsAI',  # Summoner's Rift and Crystal Scar games played against AI
    'CoopVsAI3x3',  # Twisted Treeline games played against AI
    'RankedSolo5x5',  # Summoner's Rift ranked solo queue games
    'RankedTeams3x3',  # Twisted Treeline ranked team games
    'RankedTeams5x5',  # Summoner's Rift ranked team games
    'OneForAll5x5',  # One for All games
    'FirstBlood1x1',  # Snowdown Showdown 1x1 games
    'FirstBlood2x2',  # Snowdown Showdown 2x2 games
    'SummonersRift6x6',  # Hexakill games
    'CAP5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URFBots',  # Ultra Rapid Fire games played against AI
    'NightmareBot',  # Summoner's Rift games played against Nightmare AI
    'Hexakill',  # Twisted Treeline 6x6 Hexakill games
    'KingPoro',  # King Poro games
    'CounterPick',  # Nemesis games
    'Bilgewater',  # Black Market Brawlers games
]

solo_queue, ranked_5s, ranked_3s = 'RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3'

api_versions = {
    'champion': 1.2,
    'current-game': 1.0,
    'featured-games': 1.0,
    'game': 1.3,
    'league': 2.5,
    'lol-static-data': 1.2,
    'lol-status': 1.0,
    'match': 2.2,
    'matchhistory': 2.2,
    'matchlist': 2.2,
    'stats': 1.3,
    'summoner': 1.4,
    'team': 2.4
}


class LoLException(Exception):
    def __init__(self, error, response):
        self.error = error
        self.headers = response.headers

    def __str__(self):
        return self.error


error_400 = "Bad request"
error_401 = "Unauthorized"
error_404 = "Game data not found"
error_429 = "Too many requests"
error_500 = "Internal server error"
error_503 = "Service unavailable"


def raise_status(response):
    if response.status_code == 400:
        raise LoLException(error_400, response)
    elif response.status_code == 401:
        raise LoLException(error_401, response)
    elif response.status_code == 404:
        raise LoLException(error_404, response)
    elif response.status_code == 429:
        raise LoLException(error_429, response)
    elif response.status_code == 500:
        raise LoLException(error_500, response)
    elif response.status_code == 503:
        raise LoLException(error_503, response)
    else:
        response.raise_for_status()


class RateLimit:
    def __init__(self, allowed_requests, seconds):
        self.allowed_requests = allowed_requests
        self.seconds = seconds
        self.made_requests = deque()

    def __reload(self):
        t = time.time()
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def add_request(self):
        self.made_requests.append(time.time() + self.seconds)

    def request_available(self):
        self.__reload()
        return len(self.made_requests) < self.allowed_requests


class RiotWatcher:
    def __init__(self, key, default_region=NORTH_AMERICA, limits=(RateLimit(10, 10), RateLimit(500, 600), )):
        self.key = key
        self.default_region = default_region
        self.limits = limits

    def can_make_request(self):
        for lim in self.limits:
            if not lim.request_available():
                return False
        return True

    def base_request(self, url, region, static=False, **kwargs):
        if region is None:
            region = self.default_region
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        r = requests.get(
            'https://{proxy}.api.pvp.net/api/lol/{static}{region}/{url}'.format(
                proxy='global' if static else region,
                static='static-data/' if static else '',
                region=region,
                url=url
            ),
            params=args
        )
        if not static:
            for lim in self.limits:
                lim.add_request()
        raise_status(r)
        return r.json()

    def _observer_mode_request(self, url, proxy=None, **kwargs):
        if proxy is None:
            proxy = self.default_region
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        r = requests.get(
            'https://{proxy}.api.pvp.net/observer-mode/rest/{url}'.format(
                proxy=proxy,
                url=url
            ),
            params=args
        )
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()

    @staticmethod
    def sanitized_name(name):
        return name.replace(' ', '').lower()

    # champion-v1.2
    def _champion_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/champion/{end_url}'.format(
                version=api_versions['champion'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_all_champions(self, region=None, free_to_play=False):
        return self._champion_request('', region, freeToPlay=free_to_play)

    def get_all_free_champions(self, region=None, free_to_play=True):
        return self._champion_request('', region, freeToPlay=free_to_play)

    def get_champion(self, champion_id, region=None):
        return self._champion_request('{id}'.format(id=champion_id), region)

    # current-game-v1.0
    def get_current_game(self, summoner_id, platform_id=None, region=None):
        if platform_id is None:
            platform_id = platforms[self.default_region]
        return self._observer_mode_request(
            'consumer/getSpectatorGameInfo/{platform}/{summoner_id}'.format(
                platform=platform_id,
                summoner_id=summoner_id
            ),
            region
        )

    # featured-game-v1.0
    def get_featured_games(self, proxy=None):
        return self._observer_mode_request('featured', proxy)

    # game-v1.3
    def _game_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/game/{end_url}'.format(
                version=api_versions['game'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_recent_games(self, summoner_id, region=None):
        return self._game_request('by-summoner/{summoner_id}/recent'.format(summoner_id=summoner_id), region)

    # league-v2.5
    def _league_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/league/{end_url}'.format(
                version=api_versions['league'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_league(self, summoner_ids=None, team_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        if (summoner_ids is None) != (team_ids is None):
            if summoner_ids is not None:
                return self._league_request(
                    'by-summoner/{summoner_ids}'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                    region
                )
            else:
                return self._league_request(
                    'by-team/{team_ids}'.format(team_ids=','.join([str(t) for t in team_ids])),
                    region
                )

    def get_league_entry(self, summoner_ids=None, team_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        if (summoner_ids is None) != (team_ids is None):
            if summoner_ids is not None:
                return self._league_request(
                    'by-summoner/{summoner_ids}/entry'.format(
                        summoner_ids=','.join([str(s) for s in summoner_ids])
                    ),
                    region
                )
            else:
                return self._league_request(
                    'by-team/{team_ids}/entry'.format(team_ids=','.join([str(t) for t in team_ids])),
                    region
                )

    def get_challenger(self, region=None, queue=solo_queue):
        return self._league_request('challenger', region, type=queue)

    def get_master(self, region=None, queue=solo_queue):
        return self._league_request('master', region, type=queue)

    # lol-static-data-v1.2
    def _static_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/{end_url}'.format(
                version=api_versions['lol-static-data'],
                end_url=end_url
            ),
            region,
            static=True,
            **kwargs
        )

    def static_get_champion_list(self, region=None, locale=None, version=None, data_by_id=None, champ_data=None):
        return self._static_request(
            'champion',
            region,
            locale=locale,
            version=version,
            dataById=data_by_id,
            champData=champ_data
        )

    def static_get_champion(self, champ_id, region=None, locale=None, version=None, champ_data=None):
        return self._static_request(
            'champion/{id}'.format(id=champ_id),
            region,
            locale=locale,
            version=version,
            champData=champ_data
        )

    def static_get_item_list(self, region=None, locale=None, version=None, item_list_data=None):
        return self._static_request('item', region, locale=locale, version=version, itemListData=item_list_data)

    def static_get_item(self, item_id, region=None, locale=None, version=None, item_data=None):
        return self._static_request(
            'item/{id}'.format(id=item_id),
            region,
            locale=locale,
            version=version,
            itemData=item_data
        )

    def static_get_mastery_list(self, region=None, locale=None, version=None, mastery_list_data=None):
        return self._static_request(
            'mastery',
            region,
            locale=locale,
            version=version,
            masteryListData=mastery_list_data
        )

    def static_get_mastery(self, mastery_id, region=None, locale=None, version=None, mastery_data=None):
        return self._static_request(
            'mastery/{id}'.format(id=mastery_id),
            region,
            locale=locale,
            version=version,
            masteryData=mastery_data
        )

    def static_get_realm(self, region=None):
        return self._static_request('realm', region)

    def static_get_rune_list(self, region=None, locale=None, version=None, rune_list_data=None):
        return self._static_request('rune', region, locale=locale, version=version, runeListData=rune_list_data)

    def static_get_rune(self, rune_id, region=None, locale=None, version=None, rune_data=None):
        return self._static_request(
            'rune/{id}'.format(id=rune_id),
            region,
            locale=locale,
            version=version,
            runeData=rune_data
        )

    def static_get_summoner_spell_list(self, region=None, locale=None, version=None, data_by_id=None, spell_data=None):
        return self._static_request(
            'summoner-spell',
            region,
            locale=locale,
            version=version,
            dataById=data_by_id,
            spellData=spell_data
        )

    def static_get_summoner_spell(self, spell_id, region=None, locale=None, version=None, spell_data=None):
        return self._static_request(
            'summoner-spell/{id}'.format(id=spell_id),
            region,
            locale=locale,
            version=version,
            spellData=spell_data
        )

    def static_get_versions(self, region=None):
        return self._static_request('versions', region)

    # match-v2.2
    def _match_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/match/{end_url}'.format(
                version=api_versions['match'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_match(self, match_id, region=None, include_timeline=False):
        return self._match_request(
            '{match_id}'.format(match_id=match_id),
            region,
            includeTimeline=include_timeline
        )

    # lol-status-v1.0
    @staticmethod
    def get_server_status(region=None):
        if region is None:
            url = 'shards'
        else:
            url = 'shards/{region}'.format(region=region)
        r = requests.get('http://status.leagueoflegends.com/{url}'.format(url=url))
        raise_status(r)
        return r.json()

    # match history-v2.2
    def _match_history_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/matchhistory/{end_url}'.format(
                version=api_versions['matchhistory'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_match_history(self, summoner_id, region=None, champion_ids=None, ranked_queues=None, begin_index=None,
                          end_index=None):
        return self._match_history_request(
            '{summoner_id}'.format(summoner_id=summoner_id),
            region,
            championIds=champion_ids,
            rankedQueues=ranked_queues,
            beginIndex=begin_index,
            endIndex=end_index
        )

    # match list-v2.2
    def _match_list_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/matchlist/by-summoner/{end_url}'.format(
                version=api_versions['matchlist'],
                end_url=end_url,
            ),
            region,
            **kwargs
        )

    def get_match_list(self, summoner_id, region=None, champion_ids=None, ranked_queues=None, seasons=None,
                        begin_time=None, end_time=None, begin_index=None, end_index=None):
        return self._match_list_request(
            '{summoner_id}'.format(summoner_id=summoner_id),
            region,
            championsIds=champion_ids,
            rankedQueues=ranked_queues,
            seasons=seasons,
            beginTime=begin_time,
            endTime=end_time,
            beginIndex=begin_index,
            endIndex=end_index
        )

    # stats-v1.3
    def _stats_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/stats/{end_url}'.format(
                version=api_versions['stats'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_stat_summary(self, summoner_id, region=None, season=None):
        return self._stats_request(
            'by-summoner/{summoner_id}/summary'.format(summoner_id=summoner_id),
            region,
            season='SEASON{}'.format(season) if season is not None else None)

    def get_ranked_stats(self, summoner_id, region=None, season=None):
        return self._stats_request(
            'by-summoner/{summoner_id}/ranked'.format(summoner_id=summoner_id),

            region,
            season='SEASON{}'.format(season) if season is not None else None
        )

    # summoner-v1.4
    def _summoner_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/summoner/{end_url}'.format(
                version=api_versions['summoner'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_mastery_pages(self, summoner_ids, region=None):
        return self._summoner_request(
            '{summoner_ids}/masteries'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
            region
        )

    def get_rune_pages(self, summoner_ids, region=None):
        return self._summoner_request(
            '{summoner_ids}/runes'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
            region
        )

    def get_summoners(self, names=None, ids=None, region=None):
        if (names is None) != (ids is None):
            return self._summoner_request(
                'by-name/{summoner_names}'.format(
                    summoner_names=','.join([self.sanitized_name(n) for n in names])) if names is not None
                else '{summoner_ids}'.format(summoner_ids=','.join([str(i) for i in ids])),
                region
            )
        else:
            return None

    def get_summoner(self, name=None, _id=None, region=None):
        if (name is None) != (_id is None):
            if name is not None:
                name = self.sanitized_name(name)
                return self.get_summoners(names=[name, ], region=region)[name]
            else:
                return self.get_summoners(ids=[_id, ], region=region)[str(_id)]
        return None

    def get_summoner_name(self, summoner_ids, region=None):
        return self._summoner_request(
            '{summoner_ids}/name'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
            region
        )

    # team-v2.4
    def _team_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/team/{end_url}'.format(
                version=api_versions['team'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_teams_for_summoner(self, summoner_id, region=None):
        return self.get_teams_for_summoners([summoner_id, ], region=region)[str(summoner_id)]

    def get_teams_for_summoners(self, summoner_ids, region=None):
        return self._team_request(
            'by-summoner/{summoner_id}'.format(summoner_id=','.join([str(s) for s in summoner_ids])),
            region
        )

    def get_team(self, team_id, region=None):
        return self.get_teams([team_id, ], region=region)[str(team_id)]

    def get_teams(self, team_ids, region=None):
        return self._team_request('{team_ids}'.format(team_ids=','.join(str(t) for t in team_ids)), region)


#-------------Wololol-------------#
res = {
    "summonerInfo":{
        "summonerImg":"612",
        "summonerName":"Sad Jocker King",
        "summonerLeague":"Silver",
        "summonerDivision":"I",
        "summonerServer":"LAS",
        "summonerKills":"12.5",
        "summonerDeaths":"9.5",
        "summonerAssists":"3.1",
        "summonerKdaRatio":"3.66",
        "summonerWinrate":"55",
    },
    "mostPlayedChampInfo":{
        "mostPlayedChampId":"92",
        "mostPlayedChampName":"Riven",
        "mostPlayedChampMatchesCount":"129",
        "mostPlayedChampMatchesWinCount":"79",
        "mostPlayedChampMatchesLoseCount":"50",
        "mostPlayedChampKdaRatio":"3.66",
        "mostPlayedChampKills":"12.3",
        "mostPlayedChampDeaths":"5.1",
        "mostPlayedChampAssist":"6.6",
        "mostPlayedChampCs":"200.3",
        "mostPlayedChampGold":"17",
    },
    "profile":{
        "leagueSoloQName":"Paladines de Poppy",
        "leagueSoloQTier":"Gold",
        "leagueSoloQDivision":"V",
        "leagueSoloQLp":"93",
        "leagueTeamName":"Montaurfs de Orianna",
        "leagueTeamTier":"Silver",
        "leagueTeamDivision":"I",
        "leagueTeamLp":"82",
        "league3v3Name":"Patatas de la Tierra",
        "league3v3Tier":"Silver",
        "league3v3Division":"I",
        "league3v3Lp":"23",
    },
    "league":{
        "summonerLeagueTabName":"Montaurfs de Orianna",
        "summonerLeagueTabRank":"Silver",
        "summonerLeagueTabDivision":"I",
        "summonerLeagueTabPList":[
            {
            "summonerLeagueTabPListRank":"1",
            "summonerLeagueTabPListChange":"4",
            "summonerLeagueTabPListName":"Sad Jocker King",
            "summonerLeagueTabPListImg":"612",
            "summonerLeagueTabPListIsRecent":"1",
            "summonerLeagueTabPListIsOnFire":"1",
            "summonerLeagueTabPListWins":"70",
            "summonerLeagueTabPPromo":["1","1","0","N","N"],
            },
            {
            "summonerLeagueTabPListRank":"2",
            "summonerLeagueTabPListChange":"-3",
            "summonerLeagueTabPListName":"Manolito",
            "summonerLeagueTabPListImg":"612",
            "summonerLeagueTabPListIsRecent":"0",
            "summonerLeagueTabPListIsOnFire":"1",
            "summonerLeagueTabPListWins":"70",
            "summonerLeagueTabPPromo":["1","0","0","N","N"],
            },
            {
            "summonerLeagueTabPListRank":"3",
            "summonerLeagueTabPListChange":"13",
            "summonerLeagueTabPListName":"Groll",
            "summonerLeagueTabPListImg":"h92",
            "summonerLeagueTabPListIsRecent":"0",
            "summonerLeagueTabPListIsOnFire":"0",
            "summonerLeagueTabPListWins":"73",
            "summonerLeagueTabPPromo":["1","1","N","N","N"],

            },
        ],
        "summonerLeagueTabList":[
            {
            "summonerLeagueTabListRank":"4",
            "summonerLeagueTabListChange":"-2",
            "summonerLeagueTabListName":"Juancito",
            "summonerLeagueTabListImg":"612",
            "summonerLeagueTabListIsRecent":"1",
            "summonerLeagueTabListIsOnFire":"0",
            "summonerLeagueTabListWins":"78",
            "summonerLeagueTabListLP":"99",
            },
            {
            "summonerLeagueTabListRank":"5",
            "summonerLeagueTabListChange":"-3",
            "summonerLeagueTabListName":"Juancito2",
            "summonerLeagueTabListImg":"612",
            "summonerLeagueTabListIsRecent":"0",
            "summonerLeagueTabListIsOnFire":"1",
            "summonerLeagueTabListWins":"23",
            "summonerLeagueTabListLP":"98",
            },
            {
            "summonerLeagueTabListRank":"6",
            "summonerLeagueTabListChange":"5",
            "summonerLeagueTabListName":"Juancito3",
            "summonerLeagueTabListImg":"612",
            "summonerLeagueTabListIsRecent":"1",
            "summonerLeagueTabListIsOnFire":"0",
            "summonerLeagueTabListWins":"15",
            "summonerLeagueTabListLP":"94",
            },
            {
            "summonerLeagueTabListRank":"7",
            "summonerLeagueTabListChange":"8",
            "summonerLeagueTabListName":"Juancito4",
            "summonerLeagueTabListImg":"612",
            "summonerLeagueTabListIsRecent":"0",
            "summonerLeagueTabListIsOnFire":"1",
            "summonerLeagueTabListWins":"981",
            "summonerLeagueTabListLP":"25",
            },
        ]
    },
    "history":[
        {
            "isWin":"0",
            "champId":"92",
            "champName":"riven",
            "champLvl":"15",
            "spell1":"4",
            "spell2":"11",
            "gameSubType":"Normal 5 vs 5",
            "map":"La Grieta del Invocador",#la base de datos guarda el valor 11 que corresponde a este
            "timePlayed":"1213",
            "ipEarned":"123",
            "kills":"31",
            "deaths":"12",
            "assists":"13",
            "goldGained":"15",
            "creepScore":"212",
            "createDate":"13/8/2015",
            "createTime":"16:35 PM",
            "item1":"1004",
            "item2":"1011",
            "item3":"1006",
            "item4":"1018",
            "item5":"1026",
            "item6":"1006",
            "item7":"1026",
        },
        {
            "isWin":"1",
            "champId":"22",
            "champName":"ashe",
            "champLvl":"18",
            "spell1":"11",
            "spell2":"4",
            "gameSubType":"Normal 5 vs 5",
            "map":"La Grieta del Invocador",
            "timePlayed":"1713",
            "ipEarned":"255",
            "kills":"12",
            "deaths":"21",
            "assists":"21",
            "goldGained":"12",#si son 12552 devuelve unicamente 12552/1000 = 12
            "creepScore":"323",
            "createDate":"23/3/2015",
            "createTime":"8:23 AM",
            "item1":"1018",
            "item2":"1004",
            "item3":"1026",
            "item4":"1006",
            "item5":"1018",
            "item6":"1004",
            "item7":"1026",
        },
        {
            "isWin":"1",
            "champId":"92",
            "champName":"riven",
            "champLvl":"7",
            "spell1":"4",
            "spell2":"11",
            "gameSubType":"Normal 5 vs 5",
            "map":"La Grieta del Invocador",
            "timePlayed":"3210",
            "ipEarned":"64",
            "kills":"21",
            "deaths":"3",
            "assists":"23",
            "goldGained":"18",
            "creepScore":"122",
            "createDate":"15/8/2015",
            "createTime":"14:28 PM",
            "item1":"1026",
            "item2":"1018",
            "item3":"1004",
            "item4":"1006",
            "item5":"1004",
            "item6":"1018",
            "item7":"1026",
        },
    ],
    "runes":{
        "activePage":"AP Tanque",
        "pages":[
            ["Ashe",{
                        "5245":["Gran Quintaescencia de Daño de Ataque","3","7.55"],
                        "5244":["Gran Marca de Daño de Ataque","9","8.55"],
                        "5243":["Gran Sello de Armadura","9","9"],
                        "5242":["Gran Glifo de Velocidad de Ataque","9","5.73"]
                    }],
            ["Riven",{
                        "5242":["Gran Quintaescencia de Daño de Ataque","3","7.55"],
                        "5243":["Gran Marca de Daño de Ataque","9","8.55"],
                        "5244":["Gran Sello de Armadura","9","9"],
                    }],
            ["Lucian",{
                        "5245":["Gran Quintaescencia de Daño de Ataque","3","7.55"],
                        "5244":["Gran Glifo de Velocidad de Ataque","9","5.73"]
                    }],
            ["AP Tanque",{
                        "5243":["Gran Quintaescencia de Daño de Ataque","3","7.55"],
                        "5242":["Gran Marca de Daño de Ataque","9","8.55"],
                        "5245":["Gran Sello de Armadura","9","9"],
                        "5244":["Gran Glifo de Velocidad de Ataque","9","5.73"]
                    }],
            ["AD Teemo con Tiamat",{
                        "5243":["Gran Quintaescencia de Daño de Ataque","3","7.55"],
                        "5242":["Gran Sello de Armadura","9","9"],
                        "5245":["Gran Glifo de Velocidad de Ataque","9","5.73"]
                    }]
        ]
    },
    "masteries":{
        "activePage":"Tanque Jungla",
        "masteries":[
            ["Ashe",["18","0","12"]],
            ["Riven",["18","0","12"]],
            ["Sejuani",["0","18","12"]],
            ["Tanque Jungla",["12","18","0"]],
            ["Daño ADC",["3","4","23"]],
            ["Azir",["18","12","0"]],
            ["Lucian",["18","0","12"]],
            ["Teemo con Tiamat",["10","10","10"]],
            ["La maestria de pruebas de tu vieja",["13","7","10"]],
        ]
    }
}
def getApiSummoner(summoner = None, idSum = None, region = None):
    #Pedir toda la informacion a la api
    #Formatearla al diccionario y devolverla
    global res
    print str(res)
    return res

def getCacheSummoner(summoner = None, idSum = None, region = None):
    #Comprobar si el summoner esta en el cache
    #Si esta devolverlo
    #Si no devolver None
    global res
    print str(res)
    return res
