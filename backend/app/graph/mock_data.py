MOCK_VENUES = {
    "default": {
        "name": "The Velvet Room",
        "type": "nightclub",
        "capacity": 350,
        "neighborhood": "Lower East Side",
        "known_for": "Intimate dance floor, premium sound system, craft cocktails",
        "typical_audience": "25-35 professionals, music enthusiasts",
        "instagram_followers": 12000,
        "past_events": ["House Fridays", "R&B Therapy", "Sunset Sessions"],
    },
    "greenlight_social": {
        "name": "Greenlight Social",
        "type": "nightclub",
        "capacity": 3000,
        "neighborhood": "Downtown",
        "known_for": "multiple rooms/vibes, drinks flowing, crowded dance floor",
        "typical_audience": "general club goers",
        "instagram_followers": 50000,
        "past_events": ["Sunset Sessions", "Ruby Room Thursdays"],
    },
    "palomino": {
        "name": "Palomino",
        "type": "nightclub",
        "capacity": 1000,
        "neighborhood": "Downtown",
        "known_for": "EDM music, crowded dance floor, bottle service",
        "typical_audience": "general club goers",
        "instagram_followers": 20000,
        "past_events": [],
    }
}

MOCK_SCENE_DATA = {
    "New York": {
        "trending_genres": ["Afrobeats", "Jersey Club", "R&B"],
        "competing_events_this_week": [
            {"name": "Soulection Night", "venue": "Elsewhere", "day": "Friday"},
            {"name": "Vinyl Vibes", "venue": "Good Room", "day": "Saturday"},
        ],
        "local_influencers": ["@nikitenights", "@dancefloornyc"],
        "avg_cover_price": "$20-35",
    },
    # TODO: Add 1-2 more cities
    "Dallas": {
        "trending_genres": ["House", "Hip Hop", "R&B"],
        "competing_events_this_week": [
            {"name": "Your Mom", "venue": "Hideaway", "day": "Friday"},
            {"name": "Vinyl Vibes Deluxe", "venue": "Barcadia", "day": "Saturday"},
        ],
        "local_influencers": ["@june", "@december"],
        "avg_cover_price": "$5-10",
    }
}


def get_mock_venue_data(venue_name: str) -> dict:
    """Return mock venue data. Falls back to 'default' if venue not found."""
    return MOCK_VENUES.get(venue_name, MOCK_VENUES["default"])

    


def get_mock_scene_data(city: str) -> dict:
    """Return mock scene data for a city."""
    return MOCK_SCENE_DATA.get(city, MOCK_SCENE_DATA["New York"])
