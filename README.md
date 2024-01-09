# Easy Auto-ETL 
This repository demonstrates a simple ETL (Extract, Transform, Load) pipeline on OpenAQ data, fetching and updating Seattle's air quality metrics on an hourly basis.

[XetData](https://github.com/apps/xetdata) adds large file support to this repo, allowing us to run an automated data processing task using GitHub Actions and store the results back to the repo — no extra databases, orchestrators, or storage needed.

The key benefits of this approach:
- Save your processed data directly in Git, no need to manage separate storage accounts or API keys
- The entire pipeline is run entirely in GitHub Actions
- Your data and code are tracked side-by-side for guaranteed lock-step development

## Method 

There are three main pillars in our approach.

- **Trigger** - The ETL process is a CRON job triggered every hour in GitHub Actions. See `.github/workflows/xet-enabled-action.yml`.
- **Pipeline** - The ETL pipeline code is executed directly within GitHub Actions to pull and process the data. See `src/pipeline.py`.
- **Data Storage in GitHub** - The processed output is saved and committed as a CSV file in the `data` directory of the repo.

That's it. 

Navigate to [the commit history of the processed data](https://github.com/xetdata/easy-etl/commits/main/data/air_data.csv) to see the hourly updates and click on the comments to easily browse to XetData file views. [Install the Git-Xet client](https://xethub.com/assets/docs/getting-started/install) if you want to clone and customize this repository. Data will update on every clone and pull. 

## Try it for yourself!

What's more exciting than getting started with your own data? Luckily, we've created a [templated version of this repo here](https://github.com/xetdata/easy-etl-template). Follow the instructions there to setup your own ETL pipeline with just a few steps.

## Thanks
This example is an adapted version of [this project](https://github.com/beltran-oscar/ETL-pipeline-ML), so if you like this demo, please go there and show the project some love too.
