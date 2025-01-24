# Hadoop-Based Search Engine

## Overview

This project implements a search engine powered by a Hadoop-based backend, designed to handle large datasets efficiently using MapReduce. The search engine preprocesses a dataset, indexes data, and assigns unique IDs to words, enabling optimized searches. The backend processes the data in a distributed manner using Hadoop's MapReduce framework, while Python is used for the initial data cleaning and preparation.

## Dataset

The dataset contains articles with the following relevant fields:
- **SECTION_TEXT**: The content of each article.
- **ARTICLE_ID**: A unique identifier for each article.

For indexing, the dataset is preprocessed to retain only these fields, ensuring that the search engine focuses on the most important information for indexing and search queries.

## Methodology

### 1. Data Preprocessing

Data preprocessing is performed using Python (Jupyter Notebook). Key steps include:
- **Stop Word Removal**: Common words are removed to minimize noise in the data.
- **Duplicate Removal**: Duplicates are eliminated to maintain unique entries.
- **Punctuation and Special Character Removal**: Text is standardized for consistency.
- **Handling Missing Values**: Rows with missing data are dropped.
- **Column Filtering**: Only `SECTION_TEXT` and `ARTICLE_ID` are retained for further processing.
- **Text Formatting**:
  - A dictionary of all sentences is created.
  - A vocabulary of unique words is built.
  - Each word is assigned a unique identifier for indexing.

The preprocessing logic is available in the [DataCleaner.ipynb](./DataCleaner.ipynb) file.

### 2. Hadoop MapReduce Implementation

The MapReduce pipeline consists of two main components: the **Mapper** and the **Reducer**.

#### Mapper
The mapper processes the preprocessed dataset line by line and outputs the cleaned sentences. The mapper is implemented in [mapper.py](./mapper.py).

```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    var = line.strip()  
    print(var)
```

#### Reducer
The reducer processes the output of the mapper. It:
- Creates a dictionary of sentences.
- Builds a vocabulary of unique words.
- Assigns unique IDs to each word.

The reducer logic is implemented in [reducer.py](./reducer.py).

```python
#!/usr/bin/env python3
import sys

# Defining a dictionary to save sentences
MyDICT = {}
TempUserID_ = 0

# Running loop to process the dataset
for line in sys.stdin:
    MyDICT[TempUserID_] = line.strip()
    TempUserID_ += 1

# Creating a vocabulary of unique words
WORD_ARRAY = set()

for Sentence in MyDICT.values():
    WORD_ARRAY.update(Sentence.split())

# Sorting and assigning unique IDs to words
WORD_ARRAY = sorted(list(WORD_ARRAY))
i_WORD_ARRAY = list(enumerate(WORD_ARRAY))
```

### Workflow

The workflow of the project is as follows:

1. **Preprocessing**:
   - Clean and format the dataset.
   - Generate sanitized data for input to the MapReduce job.

2. **MapReduce Pipeline**:
   - **Mapper**: Processes the input sentences line by line.
   - **Reducer**: Builds a dictionary of sentences, creates a vocabulary, and assigns unique IDs to words.

3. **Output**:
   - Indexed vocabulary of unique words.
   - Word-to-ID mappings for optimized searching.

### Execution

To run this project, follow the steps below:

1. **Preprocess the Dataset**:
   - Use the `DataCleaner.ipynb` notebook to clean and prepare the dataset. Ensure the dataset is in the appropriate format with `SECTION_TEXT` and `ARTICLE_ID` fields.

2. **Run the Mapper**:
   - Execute the `mapper.py` script to process the cleaned sentences from the preprocessed dataset.

3. **Run the Reducer**:
   - Use the `reducer.py` script to generate the word index and unique IDs for the words in the dataset.

4. **Verify Output**:
   - Check the output for word-to-ID mappings and the indexed vocabulary.

### Conclusion

This project demonstrates how to build a scalable search engine using Hadoop and Python. The use of MapReduce allows for efficient distributed processing of large datasets, while the preprocessing step ensures the data is clean and optimized for indexing. The result is a search engine capable of fast and accurate searching by leveraging a unique ID-based vocabulary.

## Requirements

- Python 3.x
- Hadoop 2.x or later
- Jupyter Notebook (for preprocessing)

## Running on Hadoop Cluster

To run the MapReduce job on a Hadoop cluster, follow these additional steps:
1. **Package your scripts**: Ensure that `mapper.py` and `reducer.py` are available in the Hadoop environment.
2. **Run the Hadoop job**:
   ```bash
   hadoop jar /path/to/hadoop-streaming.jar -input /path/to/input -output /path/to/output -mapper mapper.py -reducer reducer.py
   ```

Feel free to reach out for any issues or suggestions!
```

You can copy and paste this into a `README.md` file for your project! Let me know if you need further adjustments!
