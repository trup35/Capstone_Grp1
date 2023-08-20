# AI Based Generative QA System - GPT2 variant

Deplyoded application : https://huggingface.co/spaces/SilentLearner/AIML_Gradio

## Problem Statement
This work centers around generative AI systems and encompasses two distinct objectives within this domain. The initial objective involves generating email subjects using a well-prepared dataset, and subsequently engaging in hands-on fine-tuning utilizing a GPT model. Through this process of mastering the implementation of GPT model fine-tuning for subject line generation, a novel dataset will be curated for the subsequent task. The second task involves training a Question-Answering (QA) model, which can then be deployed for testing its proficiency in responding to novel AIML queries.

### 1. Email Subject Line Generation
In contrast to frequently addressed challenges in domains such as news summarization or headline generation, which share conceptual similarity with this task, the unique focus of task 1 lies in creating succinct and concise email subject summaries. This task entails the identification of the most pertinent sentences within the email content and condensing the conveyed message into a brief set of words. On an implementation level, this project provides a platform to experiment with NLP generative models, specifically any preferred GPT-2 variant. Additionally, participants will delve into the assessment of text generation using diverse metrics.

### 2. Question Answering on AIML Queries
Building upon the acquired knowledge of model finetuning and assessment from the initial task, the focal point of this task is centered around accomplishing the core objective of the second task: developing a domain-specific variant of the GPT model capable of addressing queries specific to the AIML course. While pretrained models exhibit proficiency in generating relevant text outputs for general and open-ended textual prompts, their capacity to produce refined outputs within specialized domains is limited. To address this, the conventional approach involves refining the model using a task-specific dataset to enhance its domain expertise. In this context, participants will collaborate to construct an innovative and contextually pertinent dataset tailored to the task at hand. Subsequent to the finetuning process, the performance of the model will be evaluated in relation to novel and related inquiries.


## Datasets Description

### 1. The Annotated Enron Subject Line Corpus
The dataset designated as the Annotated Enron Subject Line Corpus, available at https://github.com/ryanzhumich/AESLC, has been earmarked for utilization in the inaugural task. It encompasses a curated subset of meticulously cleaned, filtered, and non-duplicated emails extracted from the comprehensive Enron Email Corpus, housing communication within the email inboxes of Enron Corporation employees.
Notably, the evaluation split of this dataset, encompassing both development and test subsets, features three subject lines meticulously annotated by human evaluators. This provision of multiple potential references enhances the efficacy of evaluating the generated subject lines. This approach acknowledges the challenge inherent in identifying a single, distinct, and fitting subject line for each email.
Furthermore, several dataset statistics provide valuable insights:
Train / dev / test split sizes: 14,436 / 1,960 / 1,906 emails respectively.
On average, an email contains 75 words.
On average, a subject line comprises 4 words.

### 2. AIML QA Corpus
The dataset presented here is the result of a meticulous collaborative effort involving seven distinct capstone project teams. Each of these teams has painstakingly annotated an approximate total of 120 questions, each complemented by two answers of notably high quality. The annotation process adhered to the following guidelines:
Questions were limited to 23 words or 150 characters.
Answers were constrained to 35 words or 230 characters.
Slight flexibility was allowed within these limits to accommodate the intricacies of question-answer pairs. In aggregate, the compiled dataset comprises a grand total of 1316 question-answer pairs earmarked for training purposes. Additionally, 80 pairs have been set aside for validation, while a further 120 pairs have been reserved for rigorous testing.

### Prompts

For Task 1, our objective entails generating an email subject based on the content of the email body. To effectively train the model, both the body and subject of the email must be introduced as inputs to the model in a cohesive manner. During inference, however, the model shall be provided solely with the email body, and it is anticipated to generate a subject followed by the body. Consequently, we define the following formats for training and inference prompts:

Training Prompt: '\<body>' Body of email '\<subject>' Subject of email.

Inference Prompt: '\<body>' Body of email '\<subject>'.

For Task 2, the goal revolves around generating answers to questions while utilizing domain-specific questions as inputs. During model training, it is essential to furnish the model with question and answer pairs as inputs. Inference, on the other hand, involves supplying the model with solely the question as input, anticipating the model to generate an answer followed by the question prompt. Thus, we establish the ensuing formats for training and inference prompts:

Training Prompt: '\<question>' Question '\<answer>' Answer.

Inference Prompt: '\<question>' Question '\<answer>'.


