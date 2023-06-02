import os
import shutil
from pathlib import Path

# Install SpaCy Dependencies
os.system('python3 -m spacy download en_core_web_lg')
os.system('python3 -m spacy download en_core_web_sm')

# Install nltk Dependencies
TRAIN_DIRECTORY = os.path.join(os.getcwd(), "train/")

for i in range(0,20):
  os.system(
    "aws s3 sync s3://myinterviewtrainer/user_company_profiles/resumes/000/{idx:03d}/ {dest}".format(
      idx = i,
      dest = TRAIN_DIRECTORY
    )
  )

TRAIN_DIRECTORY = os.path.join(os.getcwd(), "train/")
resumes = list(Path(TRAIN_DIRECTORY).rglob("*.pdf"))
idx = 1

for resume in resumes:
  file_name = resume.resolve()
  os.rename(file_name, "{dir}{idx}.pdf".format(idx=idx, dir=TRAIN_DIRECTORY))
  idx += 1

# Delete empty folders
objects = os.listdir(TRAIN_DIRECTORY)
for _object in objects:
  if os.path.isdir(TRAIN_DIRECTORY + _object):
    shutil.rmtree(TRAIN_DIRECTORY + _object)
