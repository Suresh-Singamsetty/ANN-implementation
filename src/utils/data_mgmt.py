import tensorflow as tf

def get_data(validation_datasize):
	mnist = tf.keras.datasets.mnist
	(X_train, y_train), (X_val,y_val), (X_test,y_test)

	X_valid, X_train = X_train_full[:validation_datasize]/255. ,X_train_full[5000:]/255.
	y_valid, y_train = y_train_full[:validation_datasize] ,y_train_full[validation_datasize:]

	X_test = X_test / 255.

	return (X_train, y_train), (X_val,y_val), (X_test,y_test)
