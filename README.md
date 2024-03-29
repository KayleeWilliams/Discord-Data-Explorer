# Discord Data Explorer

Discord Data Explorer provides users with an easy-to-use platform to visualise their data collected by Discord, built with [Nuxt.js 3](https://nuxt.com/blog/v3) and [Flask](https://flask.palletsprojects.com/en/2.2.x/).

## Installation

- Clone the repository.
- Install [Docker](https://docs.docker.com/get-docker/).
- Run `docker-compose up --build` in the root directory.

## Usage

- Navigate to `localhost:3000` in your browser.
- Upload your Discord Data Package (`.zip`) and wait for the data to be processed, which can take a few minutes, depending on your device. 

## How to get your Discord Data Package

Please check out this guide by Discord to learn how to get your Discord Data Package: https://support.discord.com/hc/en-us/articles/360004027692-Data-Export

## Example Output

![Example Output](demo.png)
## Some Data That is Visualised

- Top 5 messages sent to friends, servers, groups.
- Average Activity (Per Day, Per Week, Per Month).
- DMs to friends vs non friends.
- Total messages by channel.
- Total messages sent.
- Money spent.
- Predicted Age.
- Upsells viewed.
- Browsers used to access Discord.
- Total friends, servers, groups.
- Calls started.
- Times mentioned @everyone.
- Spotify listen alongs.
- Total screenshares.
- Total reactions.
- Times opened Discord.

## Additional Features

- Export data as a `.json` file.
- Export data as a `.png` image.
- Filter data by time periods & more.
- Toggle how to view data e.g. Text or Graph.
