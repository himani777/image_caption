
'''
Author: Igor Lapshun
This is a deep-learning course final project.
Implementation followed by: http://arxiv.org/pdf/1511.06361v5.pdf
Note: This is based on Keras v1.0.3 framework with several modified engine
files - since the library is very buggy.
Enjoy!

'''

#This is the configurations/ meta parameters for this model
# (currently set to optimal upon cross valiation).
config = {
    'model_cnn':'/home/igor/PycharmProjects/GRU/models/vgg19_weights.h5',
    'data': '/home/igor/PycharmProjects/GRU/data/coco',
    'save_dir': 'anypath',
    'dim_cnn': 4096,
    'optimizer': 'adam',
    'batch_size': 128,
    'epoch': 300,
    'output_dim': 1024,
    'dim_word': 300,
    'lrate': 0.05,
    'max_cap_length' : 50,
    'cnn' : '10crop',
    'margin': 0.05
}


if __name__ == '__main__':
    import trainer
    trainer.trainer(config)
