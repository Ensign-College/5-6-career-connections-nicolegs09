import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def get_chapter_summary(book, chapter):
    url = f"{base_url}{book.lower()}/{chapter}"
    response = requests.get(url)
    data = response.json()
    return data['chapter']['summary']

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    while True:
        book = input("Which book of the Book of Mormon would you like? ").strip()
        chapter = input(f"Which chapter of {book} are you interested in? ").strip()

        summary = get_chapter_summary(book, chapter)

        print(f"Summary of {book} chapter {chapter}:")
        print(f"--{summary}")

        choice = input("Would you like to view another (Y/N)? ").strip().upper()
        if choice != 'Y':
            break

    print("Thank you for using Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()
