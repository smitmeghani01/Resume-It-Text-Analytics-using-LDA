a=$(aws s3 cp $1 fable/tmp/)
file_name=$(ls fable/tmp/)
idx=0
file_path=fable/tmp/${file_name[$idx]}
source fable/env/bin/activate && python3 fable/main.py --type lda $file_path --model_name soft_engg; rm $file_path
