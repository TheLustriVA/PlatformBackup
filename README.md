# Platform Backup

Platform Backup provides a modern Python-based backup solution for customer-facing web services. It is designed to be easy to use and easy to extend.

![PB header](https://i.imgur.com/mu70AQX.png)

## 👋 Welcome

Soundgasm has been a little sick recently so, without asking anyone, I've decided to archive as much of it as I can.

## ToDo list

- [ ] Reach out to the creator of soundgasm.net for their take on the situation
- [X] Code up a quick python scraper to grab a full dataset from gwasi.com
- [X] Use that scrape to begin building a partial dataset of soundgasm users
- [ ] Create a set of unit tests
- [ ] Use the Reddit API to extend the dataset with more information
- [ ] Use that dataset to start backing up metadata to GitHub/GoogleSheets/Datasette
- [ ] Use the crawler to backup audios to Google Drive.

### Minor to-do tasks

- [ ] Test switching scraper to use httpx instead of requests-html
- [ ] Change scraping algorithm to be faster and impact soundgasm's server/s less
- [ ] Upload example environment variable files
- [ ] Rename the scraper to be more generic

### Potential future work

- [ ] Refactor the scraper to publish a full release on PyPI

## Audio owners

If you want access to an archive of your content, please submit an issue and we'll start sending out .zip files with everything in them.

If you don't want your content archived, please submit an issue and I'll make sure your audios come off any lists we build.

## Contributors

I'm a hobbyist coder and devops guy at best, so if you want to help build test units, create better features, make the code faster, or just add some raw compute to the task, by all means fork the repo and send in PRs.

## Ethical considerations

There are cases where creators have explicitly stated that they do not with their content to be uploaded elsewhere - that will be honoured. If we get yours by accident, please let us know and we'll pull down our copies ASAP.

The actual content will not be hosted on GitHub as the EULA prohibits certain content outside of certain contexts. We'll be using a publicly visible Google Drive so that contributors can save content without giving up personal details. If you're a creator and want your backups kept out of public reach, please create an issue and we'll lock it away.
