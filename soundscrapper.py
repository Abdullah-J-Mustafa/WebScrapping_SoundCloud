from selenium import webdriver
import requests
import bs4
import os

top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search/sounds?q="
artist_url = "http://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

#create selenium browser
browser = webdriver.Chrome("/home/dev/Downloads/chromedriver_linux64/chromedriver")
browser.get("https://soundcloud.com")

print()
print(">>> Welcome to the Python Soundcloud Scrapper!")
print(">>> Explore the Top / New & Hot Charts for all the Genres")
print(">>> Search for tracks, artists and mixes")
print()

while True:
  print(">>> Menu")
  print(">>> 1 - Search for a track")
  print(">>> 2 - Search for an artist")
  print(">>> 3 - Search for a mix")
  print(">>> 4 - Top Charts")
  print(">>> 5 - New & Hot Charts")
  print(">>> 0 - Exit")
  print()

  choice = int(input(">>> Input your choice: "))
  if choice == 0:
    browser.quit()
    break
  print()

  # Search for a track
  if choice == 1:
    name = input("Name of the track: ")
    print()
    "%20".join(name.split(" "))
    browser.get(track_url + name)
    continue

  # Search for an Artist
  if choice == 2:
    name = input("Name of the artist: ")
    print()
    "%20".join(name.split(" "))
    browser.get(artist_url + name)
    continue

  # Search for a Mix
  if choice == 3:
    name = input("Name of the mix: ")
    print()
    "%20".join(name.split(" "))
    browser.get(track_url + name + mix_url_end)
    continue

  # Get Top 50 tracks for a genre
  if choice == 4:
    request = requests.get(top_url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    while True:
      print(">>> Genres Available: ")
      print()
      genres = soup.select("a[href*=genre]")[2:]
      genre_links = []

      # print out all the available genres
      for index, genre in enumerate(genres):
        print(str(index) + ": " + genre.text)
        genre_links.append(genre.get("href"))

      print()
      choice = input(">>> Your choice(press 'x' to go back to the main menu): ")

      if choice == "x":
        break
      else:
        choice = int(choice)

      url = "http://soundcloud.com" + genre_links[choice]
      request = requests.get(url)
      soup = bs4.BeautifulSoup(request.text, "lxml")
      tracks = soup.select("h2")[3:]
      track_names = []
      track_links = []

      for index, track in enumerate(tracks):
        track_names.append(track.text)
        track_links.append(track.a.get("href"))
        print(str(index+1) + ": " + track.text)
        print()

      while True:
        choice = input(">>> Your choice(press 'x' to reselect a new genre): ")

        if choice == "x":
          break
        else:
          choice = int(choice) - 1

        print("Now playing: " + track_names[choice])
        print()

        browser.get("http:soundcloud.com" + track_links[choice])

  if choice == 5:
    request = requests.get(new_url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    while True:
      print(">>> Genres Available: ")
      print()
      genres = soup.select("a[href*=genre]")[2:]
      genre_links = []

      # print out all the available genres
      for index, genre in enumerate(genres):
        print(str(index) + ": " + genre.text)
        genre_links.append(genre.get("href"))

      print()
      choice = input(">>> Your choice(press 'x' to go back to the main menu): ")

      if choice == "x":
        break
      else:
        choice = int(choice)

      url = "http://soundcloud.com" + genre_links[choice]
      request = requests.get(url)
      soup = bs4.BeautifulSoup(request.text, "lxml")
      tracks = soup.select("h2")[3:]
      track_names = []
      track_links = []

      for index, track in enumerate(tracks):
        track_names.append(track.text)
        track_links.append(track.a.get("href"))
        print(str(index+1) + ": " + track.text)
        print()

      while True:
        choice = input(">>> Your choice(press 'x' to reselect a new genre): ")

        if choice == "x":
          break
        else:
          choice = int(choice) - 1

        print("Now playing: " + track_names[choice])
        print()

        browser.get("http:soundcloud.com" + track_links[choice])

print()
print("Goodbye!")
print()
