#!/usr/bin/env python

"""
You are building stories into an app. Your inputs are an object with the
structure { username, postedAt }, and a date in the future. Each story lives
for 24 hours. Write a function that outputs the stories that are visible for
the inputted time.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Story:
    username: str
    posted_at: datetime


def visible_stories(stories, view_date):
    return [s for s in stories if s.posted_at <= view_date < s.posted_at + timedelta(1)]


def test_example():
    stories = [
        Story("fred", datetime(2021, 1, 25, 12)),
        Story("fred", datetime(2021, 1, 25, 12, 30)),
        Story("fred", datetime(2021, 1, 22, 12)),
        Story("fred", datetime(2021, 1, 27, 12)),
    ]
    assert visible_stories(stories, datetime(2021, 1, 26, 12, 15)) == [stories[1]]
