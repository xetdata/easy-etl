# Easy Auto-ETL 
This repository demonstrates an simple ETL (Extract, Transform, Load) Pipeline using GitHub actions powered with XetData. This is a new take on a standard data engineering practice using GitHub.

Using the power of XetData, we are able to implement an automated data processing task using the basic tools available to GitHub users. Since XetData adds efficient and scalable data management directly into your GitHub repo, you are able to check your data files into your repo without fear. This saves you the headache of having to store and sync your data separately from your code.

The key benefits of this approach:
- Save your processed data directly in git, no need to manage a separate account or API keys
- The entire pipeline is run entirely in GitHub actions
- Your data is in git, just clone or mount the repo and the data is on hand right with your code

## Method 

There are three main pillars in our approach.

- **Trigger** The ETL process is a CRON job triggered every hour in GitHub Actions.
- **Pipeline** The ETL pipeline code is executed directly within GitHub Actions to pull and process the data.
- **Data Storage in GitHub** The processed output is saved and committed as a CSV file in the `data` directory of the repo.

That's it. 

The updated data is available everytime you clone or pull. Take a look at `.github/workflows/xet-enabled-action.yml` to see the setup of the pipeline. Check out `src/pipeline.py` if you are interested to see how we extract, transform, and load the data.

You can [install our client](https://xethub.com/assets/docs/getting-started/install) and clone this repo. You'll be able to explore the cleaned data at `data/air_data.csv`. To view directly in GitHub, you'll need to install [our browser extension](https://xethub.com/assets/docs/github-app#browser-extension) and navigate to `data/air_data.csv` to see a link to view the file.

## Your Data Pipeline

What's more exciting to get started with your own data. Luckily, we've structured this repository as a reusable template.

Here's how to get started:
1. Fork this repo.
2. Create a new repo in GitHub. Selecting your forked repo as a template. 
3. Follow the instructions at [XetData integration for GitHub](https://github.com/apps/xetdata) and install the app to your new repo
4. Edit `src/pipeline.py` and replace the code in `extract()` with your own ETL code.
5. Make sure to save your requirements with `pip freeze > requirements.txt`
6. Commit and push your changes.

At the 21st minute of the next hour, your ETL pipeline will be run. Couldn't be easier!

## Thanks
This example is an adapted version of [this project](https://github.com/beltran-oscar/ETL-pipeline-ML), so if you like this demo, please go there and show the project some love too.
