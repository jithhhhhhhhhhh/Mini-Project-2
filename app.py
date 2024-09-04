
import numpy as np
import os
from flask import Flask, app,request,render_template
# from keras import models
# from keras.models import load_model
# from keras_preprocessing import image
# from tensorflow.python.ops.gen_array_ops import concat
# from keras.applications.inception_v3 import preprocess_input
# import cv2


#Loading the model
# modeln=load_model("model_vgg16.h5")
# modeln=load_model("model_v3_vgg16.h5")
# modeln=load_model("Vgg-16-nail-disease.h5")

import requests
from flask import Flask, request, render_template, redirect, url_for



app=Flask(__name__)

#default home page or route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def inde1():
    return render_template('index.html')




@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/nailhome')
def nailhome():
    return render_template('nailhome.html')

@app.route('/nailpred')
def nailpred():
    return render_template('nailpred.html')
@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/drugreaction')
def drugreaction():
    return render_template('drugreaction.html')

@app.route('/acne')
def acne():
    return render_template('acne.html')

@app.route('/aids')
def aids():
    return render_template('aids.html')

@app.route('/alcoholichepatitis')
def alcoholichepatitis():
    return render_template('alcoholichepatitis.html')

@app.route('/allergy')
def allergy():
    return render_template('allergy.html')

@app.route('/arthritis')
def arthritis():
    return render_template('arthritis.html')

@app.route('/bppv')
def bppv():
    return render_template('bppv.html')

@app.route('/bronchialasthma')
def bronchialasthma():
    return render_template('bronchialasthma.html')

@app.route('/cervicalspondylosis')
def cervicalspondylosis():
    return render_template('cervicalspondylosis.html')


@app.route('/chickenpox')
def chickenpox():
    return render_template('chickenpox.html')

@app.route('/chroniccholestasis')
def chroniccholestasis():
    return render_template('chroniccholestasis.html')

@app.route('/commoncold')
def commoncold():
    return render_template('commoncold.html')

@app.route('/dengue')
def dengue():
    return render_template('dengue.html')


@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')


@app.route('/fungal')
def fungal():
    return render_template('fungal.html')


@app.route('/gastoenteritis')
def gastoenteritis():
    return render_template('gastoenteritis.html')


@app.route('/gerd')
def gerd():
    return render_template('gerd.html')



@app.route('/heartattack')
def heartattack():
    return render_template('heartattack.html')


@app.route('/hemorrhoids')
def hemorrhoids():
    return render_template('hemorrhoids.html')


@app.route('/hepatitisa')
def hepatitisa():
    return render_template('hepatitisa.html')


@app.route('/hepatitisb')
def hepatitisb():
    return render_template('hepatitisb.html')


@app.route('/hepatitisc')
def hepatitisc():
    return render_template('hepatitisc.html')


@app.route('/hepatitisd')
def hepatitisd():
    return render_template('hepatitisd.html')


@app.route('/hepatitise')
def hepatitise():
    return render_template('hepatitise.html')


@app.route('/hypertension')
def hypertension():
    return render_template('hypertension.html')


@app.route('/hyperthyroidism')
def hyperthyroidism():
    return render_template('hyperthyroidism.html')


@app.route('/hypoglycemia')
def hypoglycemia():
    return render_template('hypoglycemia.html')


@app.route('/hypothyrodism')
def hypothyrodism():
    return render_template('hypothyrodism.html')


@app.route('/ich')
def ich():
    return render_template('ich.html')


@app.route('/impetigo')
def impetigo():
    return render_template('impetigo.html')


@app.route('/jaundice')
def jaundice():
    return render_template('jaundice.html')


@app.route('/malaria')
def malaria():
    return render_template('malaria.html')


@app.route('/migraine')
def migraine():
    return render_template('migraine.html')


@app.route('/osteoarthristis')
def osteoarthristis():
    return render_template('osteoarthristis.html')

@app.route('/pneumonia')
def pneumonia():
    return render_template('pneumonia.html')

@app.route('/psoriasis')
def psoriasis():
    return render_template('psoriasis.html')

@app.route('/pud')
def pud():
    return render_template('pud.html')

@app.route('/tuberculosis')
def tuberculosis():
    return render_template('tuberculosis.html')

@app.route('/typhoid')
def typhoid():
    return render_template('typhoid.html')

@app.route('/uti')
def uti():
    return render_template('uti.html')

@app.route('/varicoseveins')
def varicoseveins():
    return render_template('varicoseveins.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')


""" Running our application """
if __name__ == "__main__":
    app.run(debug =True, port = 8080)