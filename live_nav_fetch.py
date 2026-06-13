"""
Module: live_nav_fetch.py
Description: Fetches live NAV data for mutual funds
             from an external API and saves to CSV.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import requests
import pandas as pd


def fetch_live_nav(fund_code):
    """
    Fetch the latest NAV for a given fund code from API.

    Args:
        fund_code (str): The mutual fund scheme code.

    Returns:
        dict: NAV data with date and value, or None if failed.
    """
    url = f"https://api.mfapi.in/mf/{fund_code}/latest"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [{}])[0]
        else:
            print(f"⚠️  API error for fund {fund_code}")
            return None
    except Exception as e:
        print(f"⚠️  Connection failed: {e}")
        return None


if __name__ == "__main__":
    result = fetch_live_nav("100016")
    if result:
        print(f"✅ Live NAV fetched: {result}")