# 소스 코드는 대회 규정상 2021.06.15 이후 공개 가능

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
     - ground truth를 디코더의 다음 입력으로 넣어주는 기법
     - 노출 편향의 위험(학습과 추론 사이 불일치)
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
   - Inference 시 Greedy Best path 사용중인데, beam search  
   - jupyter nbviewer

## Day 6 - Day 8
 - Break

## Day 9 - 2021.06.01(화)
- focal loss, cosine focal loss 모듈 추가(loss.py) 
- ASTER에 focal loss(alpha=1, gamma=2, ignore_index=pad) 적용 후 학습중
- [https://github.com/Media-Smart/vedastr](https://github.com/Media-Smart/vedastr) 구현중
- beam search 구현중..

## Day 10 - 2021.06.02(수)
- focal loss 손절
- [https://github.com/lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR) 오픈소스 보기 + pretrained 가져오는 법 연구

## Day 11 - Day 14
 - Break

## Day 15 - 2021.06.07(월)
 - Vision Transformer 기반 모델 구현 중.. 
 - Small-SATRN 모델 분석 및 구현중

## Day16 - 2021.06.08(화)
 - Albumenatation Augmenation transform pipeline 적용 
   - https://github.com/bcaitech1/p4-fr-soccer/discussions/70
 - Vision Transformer 기반 모델 구현 성공
   - Teacher Forcing, Masking 적용하기
 - idea
   - 안 쓰고 있는 input 값들이 있다(source, tokens, level). 인풋으로 쓸 수 있지 않을까?
   - embedding을 operator, number, variable 등 카테고리를 나눠서 줄 수 있지 않을까?
   - Augmentation 적극 활용
   - ViT 모델은 Default Augmentation이 너무 과한 것 같다. input image 넣어서 Augmentation 체크하기
   - image augmentation, lr, scheduler 수정 
 
 ## Day17 - 2021.06.09(수)
 - ViT 추가 기능들 구현 중
   - Tacher Forcing (학습 후반부 갈수록 작아지게)
   - Masking 
 - idea
   - 평가 score는 sentence accuracy(문장 전체가 맞아야 함) -> loss에서 문장 전체가 맞지 않으면 penalty 주면 좋지 않을까?  
