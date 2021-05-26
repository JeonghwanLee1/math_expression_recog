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
   - Text Localization, Recognition
 
 - NLP 부족한 개념들 학습
   - Teacher Forcing
   - loss function for Sequence to Sequence model
 
 - Baseline code 
 
 
