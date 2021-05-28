# TimeLine
## Day 1 - 2021.05.24(월)
 - Open Source Survey
   - https://github.com/lukas-blecher/LaTeX-OCR
   - vision transformer 기반 model
   - 추가 train data 찾음
   - latex to image process 발견(추후 GAN 등을 통해 Image Augemtation에 활용 가능 할 것으로 보임)
 - EDA 진행
   - 데이터 형태, sequence length, image size 및 outlier 확인
 - Background 복습
   - Instance Segmentation, Object Detection의 Task, Models 복습

## Day 2 - 2021.05.25(화)
 - 학습 set fold 분리
   - stratified k-fold를 위한 class(수식의 난이도 0-4, 손글씨 여부 0-1 총 10) balanced fold dataset 생성 
 - Text Recognition SOTA 모델 조사
   - https://paperswithcode.com/sota/scene-text-recognition-on-icdar2015
   - https://github.com/Media-Smart/vedastr 오픈 소스 분석 시작(small-SATRN 모델)
 
## Day 3 - 2021.05.26(수)
 - https://github.com/Media-Smart/vedastr 오픈 소스 분석 계속 진행

 - 필요 개념 학습
   - [Text Localization](https://github.com/JeonghwanLee1/AI-study/blob/main/DL/text_localization.md), [Recognition](https://github.com/JeonghwanLee1/AI-study/blob/main/DL/text_recognition.md)
 
 - NLP 부족한 개념들 학습
   - Teacher Forcing
   - loss function for Sequence to Sequence model
 
 - Baseline code 
 
## Day 4 - 2021.05.27(목)
 - ASTER 모델 논문 및 코드 구조 분석
 - Baseline code에 Wandb 분석 코드 추가(https://github.com/bcaitech1/p4-fr-soccer/pull/22)
 - Wandb Team Project + Slack 연동
 - SATRN 모델 학습 시작

## Day 5 - 2021.05.28(금)
 - Wandb Debug
   - step 제대로 안 찍히는 현상 등
   - https://github.com/bcaitech1/p4-fr-soccer/pull/25
   - https://github.com/bcaitech1/p4-fr-soccer/pull/29
 - SATRN 모델 구조 파악 및 논문 학습
 - pretrain recog model research 
 - idea
   - source, level 정보를 사용하지 않는다 => input에 넣을 수 있지 않을까? 혹은 모델 따로 개발
 - Baseline 꿀팁
   - dataset.py에서 collate 사용 이유 : transformer 등에 사용(데이터 형태가 일반 모델과 다름 + 자연어처리에서 padding을 배치당 맥스 랭스로 줄 때 등 사용
   - iterable에서 하나만 갖고 오고 싶을 때 next(iter())
   - 
