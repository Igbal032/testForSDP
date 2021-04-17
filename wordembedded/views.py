from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from .models import wordembedded
from flask import Flask, render_template, request, redirect
#Import Module 
import os 
from nltk.tokenize import sent_tokenize, word_tokenize 
import gensim 
from gensim.models import Word2Vec
from gensim.models import FastText   
from bpemb import BPEmb
from transformers import BertTokenizer
#SENTENCE EMBEDDING
#Creating Doc2Vec Model
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


def home(request): 
    return render(request,"index.html",{"resultSim":"empty","result":"empty","resultEncode":"empty","resultDoc2Vector":"empty","resultSenEmSim":"empty"})

