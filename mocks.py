import tweepy

TWITTER_SEARCH = {
    "statuses": [
        {
            "created_at": "Sun Feb 25 18:11:01 +0000 2018",
            "id": 967824267948773377,
            "id_str": "967824267948773377",
            "text": "FINALLY, IT'S CONFIRMED!\n\nThe National Aeronautics and Space Administration has confirmed the discovery of a planet that exists around three stars, named KOI-5Ab, after 11 years.",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/FjPEWnh804",
                        "expanded_url": "https://twitter.com/i/web/status/967824267948773377",
                        "display_url": "twitter.com/i/web/status/9…",
                        "indices": [
                            117,
                            140
                        ]
                    }
                ]
            },
            "metadata": {
                "result_type": "popular",
                "iso_language_code": "en"
            },
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 11348282,
                "id_str": "11348282",
                "name": "NASA",
                "screen_name": "NASA",
                "location": "",
                "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                "url": "https://t.co/TcEE6NS8nD",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/TcEE6NS8nD",
                                "expanded_url": "http://www.nasa.gov",
                                "display_url": "nasa.gov",
                                "indices": [
                                    0,
                                    23
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 28605561,
                "friends_count": 270,
                "listed_count": 90405,
                "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                "favourites_count": 2960,
                "utc_offset": -18000,
                "time_zone": "Eastern Time (US & Canada)",
                "geo_enabled": False,
                "verified": True,
                "statuses_count": 50713,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                "profile_link_color": "205BA7",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "F3F2F2",
                "profile_text_color": "000000",
                "profile_use_background_image": True,
                "has_extended_profile": True,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "regular"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 988,
            "favorite_count": 3875,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "en"
        },
        {
            "created_at": "Sun Feb 25 19:31:07 +0000 2018",
            "id": 967844427480911872,
            "id_str": "967844427480911872",
            "text": "NASA knows that #artists are uniquely able to convey the beauty of space and the meaningfulness of exploration. They commission artwork and fund artists in residence, granting special access to launches, astronauts, clean rooms, and more.",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/29dZgga54m",
                        "expanded_url": "https://twitter.com/i/web/status/967844427480911872",
                        "display_url": "twitter.com/i/web/status/9…",
                        "indices": [
                            117,
                            140
                        ]
                    }
                ]
            },
            "metadata": {
                "result_type": "popular",
                "iso_language_code": "en"
            },
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 11348282,
                "id_str": "11348282",
                "name": "NASA",
                "screen_name": "NASA",
                "location": "",
                "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                "url": "https://t.co/TcEE6NS8nD",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/TcEE6NS8nD",
                                "expanded_url": "http://www.nasa.gov",
                                "display_url": "nasa.gov",
                                "indices": [
                                    0,
                                    23
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 28605561,
                "friends_count": 270,
                "listed_count": 90405,
                "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                "favourites_count": 2960,
                "utc_offset": -18000,
                "time_zone": "Eastern Time (US & Canada)",
                "geo_enabled": False,
                "verified": True,
                "statuses_count": 50713,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                "profile_link_color": "205BA7",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "F3F2F2",
                "profile_text_color": "000000",
                "profile_use_background_image": True,
                "has_extended_profile": True,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "regular"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 2654,
            "favorite_count": 7962,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "en"
        },
        {
            "created_at": "Mon Feb 26 19:21:43 +0000 2018",
            "id": 968204446625869827,
            "id_str": "968204446625869827",
            "text": "On Thurs., Jan. 14 at 1pm ET, climate researchers from \n@NASAGISS\n & \n@NOAA\n will release their annual assessment of global temperatures & discuss the major climate trends of 2020. How to listen to this live update from the \n@ametsoc\n annual meeting: https://go.nasa.gov/3i8s6qz",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/SUX30Y45mr",
                        "expanded_url": "https://twitter.com/i/web/status/968204446625869827",
                        "display_url": "twitter.com/i/web/status/9…",
                        "indices": [
                            117,
                            140
                        ]
                    }
                ]
            },
            "metadata": {
                "result_type": "popular",
                "iso_language_code": "en"
            },
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 11348282,
                "id_str": "11348282",
                "name": "NASA",
                "screen_name": "NASA",
                "location": "",
                "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                "url": "https://t.co/TcEE6NS8nD",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/TcEE6NS8nD",
                                "expanded_url": "http://www.nasa.gov",
                                "display_url": "nasa.gov",
                                "indices": [
                                    0,
                                    23
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 28605561,
                "friends_count": 270,
                "listed_count": 90405,
                "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                "favourites_count": 2960,
                "utc_offset": -18000,
                "time_zone": "Eastern Time (US & Canada)",
                "geo_enabled": False,
                "verified": True,
                "statuses_count": 50713,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                "profile_link_color": "205BA7",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "F3F2F2",
                "profile_text_color": "000000",
                "profile_use_background_image": True,
                "has_extended_profile": True,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "regular"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 729,
            "favorite_count": 2777,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "en"
        },
        {
            "created_at": "Mon Feb 26 06:42:50 +0000 2018",
            "id": 968013469743288321,
            "id_str": "968013469743288321",
            "text": "Due to weather in the splashdown area, \n@SpaceX\n's updated cargo Dragon will not be departing the \n@Space_Station\n today.\n\nA new undocking date and time is currently being evaluated.",
            "truncated": True,
            "entities": {
                "hashtags": [],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/2CYoPV6Aqx",
                        "expanded_url": "https://twitter.com/i/web/status/968013469743288321",
                        "display_url": "twitter.com/i/web/status/9…",
                        "indices": [
                            117,
                            140
                        ]
                    }
                ]
            },
            "metadata": {
                "result_type": "popular",
                "iso_language_code": "ja"
            },
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 842625693733203968,
                "id_str": "842625693733203968",
                "name": "金井 宣茂",
                "screen_name": "Astro_Kanai",
                "location": "",
                "description": "宇宙飛行士。2017年12月19日から国際宇宙ステーションに長期滞在中。 応援いただいているフォロワーのみなさまと一緒に、宇宙滞在を楽しみたいと思います！",
                "url": "https://t.co/rWU6cxY9iL",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "https://t.co/rWU6cxY9iL",
                                "expanded_url": "https://ameblo.jp/astro-kanai/",
                                "display_url": "ameblo.jp/astro-kanai/",
                                "indices": [
                                    0,
                                    23
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 51512,
                "friends_count": 59,
                "listed_count": 655,
                "created_at": "Fri Mar 17 06:36:35 +0000 2017",
                "favourites_count": 7075,
                "utc_offset": 32400,
                "time_zone": "Tokyo",
                "geo_enabled": False,
                "verified": True,
                "statuses_count": 1035,
                "lang": "ja",
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/842625693733203968/1492509582",
                "profile_link_color": "E81C4F",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "000000",
                "profile_text_color": "000000",
                "profile_use_background_image": False,
                "has_extended_profile": True,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "none"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 226,
            "favorite_count": 1356,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "ja"
        },
        {
            "created_at": "Mon Feb 26 01:07:05 +0000 2018",
            "id": 967928974960545793,
            "id_str": "967928974960545793",
            "text": "Congratulations to #Olympics athletes who won gold! Neutron stars like the one at the heart of the Crab Nebula may… https://t.co/vz4SnPupe2",
            "truncated": True,
            "entities": {
                "hashtags": [
                    {
                        "text": "Olympics",
                        "indices": [
                            19,
                            28
                        ]
                    }
                ],
                "symbols": [],
                "user_mentions": [],
                "urls": [
                    {
                        "url": "https://t.co/vz4SnPupe2",
                        "expanded_url": "https://twitter.com/i/web/status/967928974960545793",
                        "display_url": "twitter.com/i/web/status/9…",
                        "indices": [
                            116,
                            139
                        ]
                    }
                ]
            },
            "metadata": {
                "result_type": "popular",
                "iso_language_code": "en"
            },
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user": {
                "id": 19802879,
                "id_str": "19802879",
                "name": "NASA JPL",
                "screen_name": "NASAJPL",
                "location": "Pasadena, Calif.",
                "description": "NASA Jet Propulsion Laboratory manages many of NASA's robotic missions exploring Earth, the solar system and our universe. Tweets from JPL's News Office.",
                "url": "http://t.co/gcM9d1YLUB",
                "entities": {
                    "url": {
                        "urls": [
                            {
                                "url": "http://t.co/gcM9d1YLUB",
                                "expanded_url": "http://www.jpl.nasa.gov",
                                "display_url": "jpl.nasa.gov",
                                "indices": [
                                    0,
                                    22
                                ]
                            }
                        ]
                    },
                    "description": {
                        "urls": []
                    }
                },
                "protected": False,
                "followers_count": 2566921,
                "friends_count": 379,
                "listed_count": 15065,
                "created_at": "Sat Jan 31 03:19:43 +0000 2009",
                "favourites_count": 1281,
                "utc_offset": -32400,
                "time_zone": "Alaska",
                "geo_enabled": False,
                "verified": True,
                "statuses_count": 6328,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "is_translation_enabled": False,
                "profile_background_color": "0B090B",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                "profile_background_tile": False,
                "profile_image_url": "http://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19802879/1398298134",
                "profile_link_color": "0D1787",
                "profile_sidebar_border_color": "100F0E",
                "profile_sidebar_fill_color": "74A6CD",
                "profile_text_color": "0C0C0D",
                "profile_use_background_image": True,
                "has_extended_profile": False,
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None,
                "translator_type": "none"
            },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "retweet_count": 325,
            "favorite_count": 1280,
            "favorited": False,
            "retweeted": False,
            "possibly_sensitive": False,
            "lang": "en"
        }
    ],
    "search_metadata": {
        "completed_in": 0.057,
        "max_id": 0,
        "max_id_str": "0",
        "next_results": "?max_id=967574182522482687&q=nasa&include_entities=1&result_type=popular",
        "query": "nasa",
        "count": 3,
        "since_id": 0,
        "since_id_str": "0"
    }
}


class APIMock:
    def search(self, q):
        return TWITTER_SEARCH


class AuthMock:
    def set_access_token(self, *args):
        pass


tweepy.OAuthHandler = lambda *args: AuthMock()
tweepy.set_access_token = lambda *args: None

tweepy.API = lambda *args: APIMock()
