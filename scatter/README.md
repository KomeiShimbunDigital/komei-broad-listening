# Talk to the City (TttC)

<img width="400" alt="image" src="https://github.com/AIObjectives/talk-to-the-city-reports/assets/3934784/57cc6367-0808-40f0-980a-540530ff0866">
<img width="400" alt="image" src="https://github.com/AIObjectives/talk-to-the-city-reports/assets/3934784/aaf45844-5a19-41c8-8943-78866db9f666">

## Overview

TttC is an AI pipeline which takes a csv file of comments and generates html reports which:

- extract the key arguments made in the original comments
- arrange the arguments into clusters based on their semantic similarity
- generate labels and summaries for all the clusters
- provide interactive maps to explore the arguments in each cluster

TttC is able to ingest different types of data and produce reports in different languages.
For example:

- [Recursive Public](https://tttc.dev/recursive) is a report generated using data collected by the Pol.is tool. The input included votes and the maps let you filter arguments by level of consensus.
- [GenAI Taiwan](https://tttc.dev/genai) is a report which can be read either in English or Mandarin. The data came from a public consultation about generative AI conducted in Taiwan by the Collective Intelligence Project.

TttC is developed by the [AI Objectives Institute](http://aiobjectives.org), an non-profit research organization focused on AI alignment.

For more context, see also our blog post: [an open-source AI tool to scale deliberation](https://ai.objectives.institute/blog/talk-to-the-city-an-open-source-ai-tool-to-scale-deliberation).

## AI safety disclaimer

TttC is a research project aiming to explore the potential of generative AI to support public deliberation. LLMs are known to be biased and to produce unreliable results. We are actively working on ways to mitigate these issues but can not provide any guarantee at this stage. We do not recommend relying on the results of this pipeline alone to make impactful decisions without first verifying the results.

## How to generate reports

### Dependencies

This repository will allow you to generate TttC reports on your machine.

For this you will need:

- an OpenAI key
- a machine to run python and javascript
- your data in a csv file

We require Python 3.10+ for compatibility reasons. We recommend using pyenv for Python version management:

```bash
# Install Python 3.10 using pyenv
pyenv install 3.10.15
pyenv local 3.10.15

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

Note: The pipeline generates various temporary files (embeddings, clusters, etc.) in the outputs directory. These files are automatically ignored by git and can be safely deleted as they will be regenerated when needed.

You'll also need npm to installed the javascript dependencies:

```
cd next-app
npm install
```

You may also need to [install git lfs](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) to use the provided examples of csv files.

### Using a provided example

This repo comes with two examples of datasets and config files, including one called `example-polis` (using Polis data).

The easiest way to test that the pipeline is working fine on you machine is to run:

```
cd pipeline
export OPENAI_API_KEY = sk-...
python main.py configs/example-polis.json
```

This will use the data from `pipeline/inputs/example-polis.csv` and produce a report under `pipeline/outputs/example-polis/report`.

We also provide another example called `example-video` which may be helpful to test video-related features.

### Using your own data

You can copy your data in the pipeline input folder, after making sure that the necessary columns `comment-id` and `comment-body` are present.

```
cp ../my-data.csv pipeline/inputs/my-data.csv
```

You'll also need a config file to specify what you want to do.
The easiest way to get started is to copy the example config file and edit it:

```
cp pipeline/configs/example.json pipeline/configs/my-project.json
```

Among other things, you'll want to change the `input` field to point to your data file.

```
{
  "input": "my-data",
  ...
}
```

You can then run the pipeline as follows:

```
cd pipeline
export OPENAI_API_KEY=sk-...
python main.py configs/my-project.json
```

## Building and viewing the report

### Building the report

The report can be built using Next.js with the REPORT environment variable:

```bash
cd next-app
REPORT=<report-name> npm run build
```

For example, to build the example report:
```bash
REPORT=example-polis npm run build
```

The built report will be generated in `pipeline/outputs/<report-name>/report` directory.

### Viewing the generated report

There are two ways to view the generated report:

#### 1. Using Python's built-in HTTP server (Recommended)

The simplest way to view the report is using Python's built-in HTTP server:

```bash
cd pipeline/outputs/<report-name>/report
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

#### 2. Using Node.js http-server

Alternatively, you can use Node.js http-server from the project's top level directory:

```bash
npm install -g http-server
http-server -p 8080
```

Then open `http://localhost:8080/pipeline/outputs/<report-name>/report/` in your browser.

Replace "<report-name>" in the above commands with your project name (e.g., "example-polis", "my-project", etc.).

### Deploying the report

You can deploy your report using any static hosting service (e.g. Vercel).

(!) Note that the html file is loading assets using relative paths. You can deploy your report anywhere (on any path/route) but you might need to include a trailing slash at the end of your urls to make sure that relative paths are resolved correctly.


## Supported columns in the csv

Below is the list of required and optional columns supported by the pipeline for the input csv file:

```
{
// REQUIRED
'comment-id': string // unique identifier for the comment
'comment-body': string // main content of the comment

// OPTIONAL
'agree'?: number // number of upvotes
'disagree?': number // number of downvotes
'video?': string // link to a video
'interview?': string // name of interviewee
'timestamp?': string // timestamp in the video
}
```

## List of config parameters

Below is the list of parameters supported in the config files:

```
{
// REQUIRED
input: string // name of the input file (without .csv extension)
question: string // the main question asked to participants

// OPTIONAL
name?: string // short name of your project
intro?: string // short introduction to your project (markdown)
model?: string // model to use (unless overridden), defaults to "gpt-3.5-turbo"
extraction?: {
  model? string // model name for extraction step (overrides the global model)
  prompt_file?: string // name of the prompt file (without .json extension)
  prompt?: string // full content the prompt for extraction step
  limit?: number // maximal number of rows to process (default to 1000)
  workers?: number // maximal number of parallel workers (default to 1)
  properties?: string[] // list of properties to extract from the input file (default to []). extracted properties will be added to the output file.
   categories?: { 
    [key: string]: { // Name of the category group (e.g., "sentiment", "genre")
      [key: string]: string // Name and description of each category
    }
  } // Definition of categories to be assigned to comments. Keys are category group names, and values are objects describing each category. If categories are defined, LLM will be used for category classification.
  category_batch_size?: number // Number of comments to classify in one batch process (default is 5)

},
embedding?: {
  model?: string // model name for embedding step. supports "text-embedding-3-small" and "text-embedding-3-large". Defaults to "text-embedding-3-small"
},
clustering: {
  clusters?: number // number of clusters to generate (default to 8)
}
labelling: {
  model? string // model name for labelling step (overrides the global model)
  prompt_file?: string // name of the prompt file (without .json extension)
  prompt?: string // full content the prompt for labelling step
  sample_size?: number // number of arguments pulled per cluster to generate labels,
},
takeaways: {
  model? string // model name for takeaways step (overrides the global model)
  prompt_file?: string // name of the prompt file (without .json extension)
  prompt?: string // full content the prompt for takeaways step
  sample_size?: number // number of arguments pulled per cluster to generate labels,
},
translation: {
  model? string // model name for takeaways step (overrides the global model)
  prompt_file?: string // name of the prompt file (without .json extension)
  prompt?: string // full content the prompt for takeaways step
  languages?: string[] // list of languages to translated to (default to [])
  flags?: string[] // list of flags to use in the UI (default to [])
},
aggregation: {
  sampling_num?: number // number of arguments to sample for the report (default to 5000)
  hidden_parameters: {
    properties?: { [key: string]: string[] } // object specifying properties to hide in the UI
                                             // Keys represent categories (e.g., "source"), and values are arrays of specific attributes to hide.
  }
},
visualization: {
  replacements?: {replace: string, by: string}[] // list of text replacements to apply to the UI
}
}
```

## Generated outputs

After running the full pipeline successfully, you should find the following files:

```
outputs
└── my-project
    ├── args.csv // extracted arguments
    ├── clusters.csv // clusters of arguments
    ├── embeddings.pkl // embeddings
    ├── labels.csv // cluster labels
    ├── translations.json // translations (JSON)
    ├── status.json // status of the pipeline
    ├── result.json // all the generated data
    └── report // folder with html report and assets

```

Note that `result.json` contains a copy of all the generated data, including the contents of `args.csv`, `clusters.csv` and `labels.csv` and `translations.json`.
These files are only kep around for caching purposes, just in case you want to re-run the pipeline with slightly different parameters and don't need to recompute everything.


## Known Issues and Troubleshooting

### Environment Setup

#### Python Environment
- We recommend using Python 3.10+ with a virtual environment
- If you encounter OpenAI client configuration issues (e.g., proxy-related errors), check the `KNOWN_ISSUES.md` file for workarounds
- Make sure your environment variables (especially `OPENAI_API_KEY`) are properly set

#### Build and Serving Issues
- If `next start` fails to serve the built site, use Python's HTTP server as described in the "Viewing the generated report" section
- The build output directory changes based on the `REPORT` environment variable, always check `pipeline/outputs/<report-name>/report` for the latest build
- Large page sizes are expected due to embedded analysis results

For more detailed information about known issues and their workarounds, please refer to `KNOWN_ISSUES.md`.


## Credits

Earlier versions of this pipeline were developed in collaboration with [@Klingefjord](https://github.com/Klingefjord) and [@lightningorb](https://github.com/lightningorb). The example of data input file was provided by the Recursive Public team (Chatham House, vTaiwan, OpenAI).

## License

GNU Affero General Public License v3.0
