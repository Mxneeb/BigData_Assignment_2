# Search Engine Implimentation using Hadoop MapReduce with Python

A **Search Engine** utilizing **Apache Hadoop MapReduce Technology** on a dataset in **comma-separated values (CSV)** format containing around 5 million Wikipedia articles provided by Wikimedia.

## Dataset

Download:  
[Wikipedia Dataset](https://drive.google.com/file/d/1lGVGqzF5CNWaoV-zoz8_mlThvHwMgcsP/view)

## Dependencies

The following libraries are required for the preprocessing of this data and to create a sample dataset:

- `pandas`
- `nltk`
- `string`
- `time`
- `tqdm`
- `numpy`
- `os`
- `tempfile`
- `nltk.corpus` (stopwords)
- `nltk.tokenize` (word_tokenize)

To install the necessary libraries, use the following:

```bash
pip install pandas nltk tqdm numpy
```

## Preprocessing Data

The preprocessing of data is done as follows:

1. **Loading and Selecting Relevant Columns**:  
   The dataset is loaded, and only relevant columns are selected for processing.

2. **Text Cleaning**:  
   The text is converted to lowercase, tokenized, and stopwords, punctuation, and special characters are removed while ensuring no empty strings remain.

3. **Chunking**:  
   The dataset is divided into manageable chunks, which are processed separately and saved temporarily.

4. **Merging Chunks**:  
   Once all chunks are processed, they are merged into a single dataset for further operations.

5. **Efficiency**:  
   The process is optimized for memory and time efficiency. The total preprocessing time is tracked and printed at the end.

6. **Temporary File Cleanup**:  
   Temporary files created during processing are cleaned up at the end to save space.

This systematic approach is essential for handling large datasets efficiently, especially when generating reports.

## Create Sample Dataset

The code processes the CSV file containing textual data, performing the following operations:
- Identifying and removing duplicates
- Concatenating text by groups
- Exporting the results, optimizing data for report generation.

## Indexing

The indexing process includes the following steps:

1. **Vocabulary Creation**:  
   Create a vocabulary using the code in the `vocab` folder, which follows the map-reduce paradigm.

2. **Term Frequency (TF)**:  
   The `tf` folder contains Python files that calculate Term Frequency for each word in the articles using MapReduce.

3. **Document Frequency (DF)**:  
   The `df` folder uses a map-reduce process to generate the Document Frequency for the dataset.

4. **Inverse Document Frequency (IDF)**:  
   The `score` folder contains the code to calculate the Inverse Document Frequency (IDF) scores for each article, utilizing the output from the TF and DF mappers and reducers.

## Vector Space Model Creation

After computing TF, DF, and IDF, the resulting arrays are converted into a **Vector Space Model (VSM)**. This is done using the code in the `vsm` folder.

## Running on Hadoop

To run the MapReduce jobs on Hadoop, follow these steps:

1. **Install Hadoop and Python**:
   Ensure that you have **Hadoop** and **Python 3.x** installed and properly configured on your system.

2. **Upload Input Data to HDFS**:
   Upload your input data to the Hadoop Distributed File System (HDFS).

3. **Compile MapReduce Code**:
   Compile your MapReduce code into a JAR file.

4. **Submit MapReduce Job**:
   Use the Hadoop command line interface to submit your MapReduce job, specifying the input and output paths and the JAR file containing your code.

   Example command to run the MapReduce job:

   ```bash
   hadoop jar /path/to/hadoop-streaming.jar \
   -input /path/to/input \
   -output /path/to/output \
   -mapper mapper.py \
   -reducer reducer.py
   ```

## Conclusion

This project demonstrates how to build a scalable search engine using Hadoop and Python. The map-reduce paradigm is used to efficiently process large datasets, while the preprocessing steps ensure the data is clean and ready for indexing. The result is a search engine capable of generating accurate reports and conducting efficient searches on large datasets.

