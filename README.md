# Thesis_Overview
Project code for Thesis Text Mining Master - Vrije Universiteit, Amsterdam The Netherlands. Directory created by Michiel van Nederpelt.

The project was focussed on Evaluating a transformer-based language model under increasingly challenging conditions for the task of offensive language detection.

Detecting offensive language online is a difficult task that even state-of-the-art models struggle with. As a method, we have introduced six different targeted perturbations in two test datasets from different domains which were then tested under both in-domain and cross-domain conditions.

By monitoring the Bidirectional Encoder Representations from Transformers model, more commonly referred to as BERT (Devlin, M. Chang, et al. 2018) performance under increasing challenging conditions, the ability of the model to perform in the “real world” is evaluated.

We follow four "phases" for increasing challenging conditions:
 - Moving from in-domain fine-tuning and testing, the most often used approach to test system performance
 - to fine-tuning on one dataset and testing the system on another, known as cross-domain testing. 
 - Phase one and three are then tested with the addition of perturbations in the test set. 
 

# Thesis report

Overleaf page thesis report: https://www.overleaf.com/project/62540ce232850d7f28306097#
 
# Resources
 
The code and links to resources used are here for reference: Much of the data required is (temporarily) available in the data folder. This will be taken offline after review. Links to the original data include:

HASOC 2019 task and description: https://dl.acm.org/doi/pdf/10.1145/3368567.3368584

SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval): https://aclanthology.org/S19-2010.pdf

HASOC dataset download: https://hasocfire.github.io/hasoc/2020/dataset.html

OLID dataset download: https://competitions.codalab.org/competitions/20011
 
# NOTE 
This paper and subsequent repositiory contains examples of language which may be offensive to some readers. They do not represent the views of the author.
