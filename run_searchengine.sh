#!/bin/bash

# delete output directories
hadoop fs -rm -r /output/step1_output
hadoop fs -rm -r /output/step2_output
hadoop fs -rm -r /output/step3_output

# Input file path
input_path="/input/data.csv"

# Output directory paths
output_step1="/output/step1_output"
output_step2="/output/step2_output"
output_step3="/output/step3_output"

# Step 1: Run word enumeration and IDF job
echo "Running word enumeration and IDF job..."
mapred streaming -files MapReduce/word_enum_mapper.py,MapReduce/idf_reducer.py \
    -input $input_path \
    -output $output_step1 \
    -mapper "python3 word_enum_mapper.py" \
    -reducer "python3 idf_reducer.py"

# Step 2: Run TF job
echo "Running TF job..."
mapred streaming -files MapReduce/tf_mapper.py,MapReduce/tf_reducer.py \
    -input $input_path \
    -output $output_step2 \
    -mapper "python3 tf_mapper.py" \
    -reducer "python3 tf_reducer.py"

# Step 3: Run TF-IDF job
echo "Running TF-IDF job..."
mapred streaming -files MapReduce/tfidf_mapper.py,MapReduce/tfidf_reducer.py \
    -input $output_step1/part-00000,$output_step2/part-00000 \
    -output $output_step3 \
    -mapper "python3 tfidf_mapper.py" \
    -reducer "python3 tfidf_reducer.py" \

# display search results
echo "All MapReduce jobs completed successfully!"
echo ""
echo "Output"
hadoop fs -cat /output/step3_output/part-00000

# save to local file
hadoop fs -cat /output/step3_output/part-00000 > searchResults.txt