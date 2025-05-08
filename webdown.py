import requests
import argparse

def down_file(raw_link, o_file):

    try:
        res = requests.get(raw_link)
        
        if res.status_code == 200:
            with open(o_file, "w") as file:
                file.write(res.text)
                
        return print(f"\nSaved as {o_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Down files from raw or web pages.",
        epilog="""Note: It is EXTREMELY IMPORTANT that the URL of the raw file is ONLY THE CONTENT OF THE FILE, if there is anything else in it it will be corrupted when the file is executed. It can also be used to download web pages.\n
    e. g. python3 rawdown.py -u https://raw.site.com/raw/file.sh -o raw_file.sh
        rawdown -u https://raw.site.com/raw/file.sh -o raw_file.sh
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("-u", "--url", help="Raw URL or URL page.", required=True)
    parser.add_argument("-o", "--output", help="Name file for save.", required=True)

    args = parser.parse_args()
    down_file(args.url, args.output)

if __name__ == "__main__":
    main()
