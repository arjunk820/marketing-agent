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
    # TODO: Add 2-3 more mock venues for variety
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
}


def get_mock_venue_data(venue_name: str) -> dict:
    """Return mock venue data. Falls back to 'default' if venue not found."""
    # TODO: Look up venue_name in MOCK_VENUES, fall back to "default"
    pass


def get_mock_scene_data(city: str) -> dict:
    """Return mock scene data for a city."""
    # TODO: Look up city in MOCK_SCENE_DATA, fall back to "New York"
    pass
