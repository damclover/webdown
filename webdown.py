#!/usr/bin/env python3

import requests
import argparse

def down_file(raw_link, o_file):
    try:
        res = requests.get(raw_link)
        if res.status_code == 200:
            with open(o_file, "w") as file:
                file.write(res.text)
            print(f"\n[✓] Saved as {o_file}")
        else:
            print(f"[!] HTTP {res.status_code}: Failed to download.")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Download files from raw links or web pages.",
        epilog="""\
Note: The URL must point directly to raw content.
Example:
    webdown https://raw.site.com/raw/file.sh raw_file.sh
    python3 webdown.py https://raw.site.com/raw/file.sh raw_file.sh
    """,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("url", help="Raw URL or web page URL.")
    parser.add_argument("output", help="Name of the file to save.")

    args = parser.parse_args()
    down_file(args.url, args.output)

if __name__ == "__main__":
    main()
