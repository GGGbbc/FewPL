# FewPL
### model
<p align="center">
  <img src="./fig/model.png" />
</p>

## 1. Environments

```
- python==3.8
- cuda==11.3
```

## 2. Dependencies

```
- numpy==1.18.0
- scikit-learn==0.22.1
- scipy==1.4.1
- tqdm==4.41.1
- transformers==4.0.0
- torch==1.10.0
- pandas==1.3.4
- scikit-learn==1.0.1
```

## 3. Dataset

Here we provide the processed I2B2-2010RE,DDI,ChemProt dataset

```
- Generate K-shot data   python generate_k_shot.py 

```

## 4. Data Augmentation Module

```
- Go to folder   cd DA 
- Augmentation using GPT API    ---python GPTDA.py
- Augmentation using Google Translate API   ---python TranDA.py
- Augmentation using SynonymAug    ---python SynonymDA.py
- Augmentation using RandomWordAug     ---python RandomWordAugDA.py

```


## 5. Training and Evaluate

```bash
- sh I2B2-2010RE_few.sh
- sh DDI_few.sh
- sh ChemProt_few.sh
