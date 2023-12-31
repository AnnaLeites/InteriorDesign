# -*- coding: utf-8 -*-
"""interior_design_renovation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mbZS2x3KIDWGM9L41UTtpvewuMQ_R8dN

## Setting everything up
"""

#!pip install tensorflow
#!pip install tensorflow_hub

import tensorflow as tf
import tensorflow_hub as hub
import numpy
from google.colab.patches import cv2_imshow

#vgg19_url = "https://tfhub.dev/google/tf2-preview/vgg19/feature_vector/2"
#vgg19_model = hub.load(vgg19_url)

model = tf.keras.applications.vgg19.VGG19(
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    input_shape=(224, 224, 3),
)

"""## Uploading pictures

Upload pictures of your apartment that needs a new design here:
"""

from google.colab import files
uploaded_r = files.upload()

"""Upload interior design that you like here:"""

from google.colab import files
uploaded_d = files.upload()

"""## Pre-processing of the images"""

#1
style_image = tf.keras.preprocessing.image.load_img("fancy.jpg", target_size=(224, 224))
style_image = tf.keras.preprocessing.image.img_to_array(style_image)
style_image = tf.keras.applications.vgg19.preprocess_input(style_image)
#2
# style_image_2 = tf.keras.preprocessing.image.load_img('despic2.jpg', target_size=(224, 224))
# style_image_2 = tf.keras.preprocessing.image.img_to_array(style_image_2)
# style_image_2 = tf.keras.applications.vgg19.preprocess_input(style_image_2)

#1
old_apartment_image = tf.keras.preprocessing.image.load_img("nf.jpg", target_size=(224, 224))
old_apartment_image = tf.keras.preprocessing.image.img_to_array(old_apartment_image)
old_apartment_image = tf.keras.applications.vgg19.preprocess_input(old_apartment_image)
# #2
# old_apartment_image_2 = tf.keras.preprocessing.image.load_img('apic2.jpg', target_size=(224, 224))
# old_apartment_image_2 = tf.keras.preprocessing.image.img_to_array(old_apartment_image_2)
# old_apartment_image_2 = tf.keras.applications.vgg19.preprocess_input(old_apartment_image_2)
# #3
# old_apartment_image_3 = tf.keras.preprocessing.image.load_img('apic3.jpg', target_size=(224, 224))
# old_apartment_image_3 = tf.keras.preprocessing.image.img_to_array(old_apartment_image_3)
# old_apartment_image_3 = tf.keras.applications.vgg19.preprocess_input(old_apartment_image_3)

combined_images = tf.stack([style_image, old_apartment_image], axis=0)
features = model(combined_images)
style_features = features[0]
content_features = features[1]

"""## Style transferring"""

def get_content_loss(content, generated):
    return tf.reduce_mean(tf.square(content - generated))

def get_style_loss(style, generated):
    return tf.reduce_mean(tf.square(style - generated))
loss_style = get_style_loss(style_features, content_features)

def total_variation_loss(image):
    x_deltas, y_deltas = image[:, :-1, :, :] - image[:, 1:, :, :], image[:, :, :-1, :] - image[:, :, 1:, :]
    return tf.reduce_sum(tf.abs(x_deltas)) + tf.reduce_sum(tf.abs(y_deltas))

def get_total_loss(style_loss, content_loss, total_variation_weight=1e-9):
    return style_loss + content_loss + total_variation_weight * total_variation_loss(generated_image)

optimizer = tf.optimizers.Adam(learning_rate=0.002)

num_iterations = 100000

# #style_features = model(style_image_1, style_image_2)
# style_features = model(style_image_1)
# content_features_1 = model(old_apartment_image_1)
# content_features_2 = model(old_apartment_image_2)
# content_features_3 = model(old_apartment_image_3)

initial_image = tf.reshape(old_apartment_image, (1, 224, 224, 3))
#generated_image = tf.Variable(tf.random.uniform(shape=(1, 224, 224, 3), minval=0, maxval=255), trainable=True)
generated_image = tf.Variable(initial_image, trainable=True)


generated_features = model(generated_image)

for i in range(num_iterations):
    with tf.GradientTape() as tape:
        loss_content = get_content_loss(content_features, generated_features)
        loss_style = get_style_loss(style_features, generated_features)
        total_loss = get_total_loss(loss_style, loss_content)

    gradients = tape.gradient(total_loss, generated_image)
    optimizer.apply_gradients([(gradients, generated_image)])

    generated_image.assign(tf.clip_by_value(generated_image, 0, 255))

# content_weight = 1e3
# style_weight = 1e-2

# def get_content_loss(content, target):
#     return tf.reduce_mean(tf.square(content - target))

# def gram_matrix(input_tensor):
#     result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
#     input_shape = tf.shape(input_tensor)
#     num_locations = tf.cast(input_shape[1]*input_shape[2], tf.float32)
#     return result / num_locations

# def get_style_loss(style, generated):
#     style_loss = tf.constant(0.0, dtype=tf.float32)
#     for style_feat, generated_feat in zip(style, generated):
#         gram_style = tf.linalg.einsum('bijc,bijd->bcd', style_feat, style_feat)
#         gram_generated = tf.linalg.einsum('bijc,bijd->bcd', generated_feat, generated_feat)
#         style_loss += tf.reduce_mean(tf.square(gram_style - gram_generated))
#     return style_loss

# generated_image_1 = tf.Variable(old_apartment_image_1, trainable=True)
# generated_image_2 = tf.Variable(old_apartment_image_2, trainable=True)
# generated_image_3 = tf.Variable(old_apartment_image_3, trainable=True)

# optimizer = tf.optimizers.Adam(learning_rate=0.02)

# num_iterations = 1000

# for i in range(num_iterations):
#     with tf.GradientTape() as tape:
#         generated_features_1 = model(generated_image_1)
#         loss_content = get_content_loss(content_features_1, generated_features_1)
#         loss_style = get_style_loss(style_features, generated_features_1)

#         total_loss = content_weight * loss_content + style_weight * loss_style

#     gradients = tape.gradient(total_loss, generated_image_1)
#     optimizer.apply_gradients([(gradients, generated_image_1)])

#     generated_image_1.assign(tf.clip_by_value(generated_image_1, 0, 255))

# tf.keras.preprocessing.image.save_img('generated_image_1.jpg', generated_image_1.numpy())
# cv2_imshow('generated_image_1.jpg')

generated_image = tf.cast(generated_image, tf.uint8)  # Convert to uint8 format
tf.keras.preprocessing.image.save_img('generated_image.jpg', generated_image[0])