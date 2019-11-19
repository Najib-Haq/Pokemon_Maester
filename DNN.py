import tensorflow as tf
import numpy as np


#define default parameters
learning_rate = 0.01
training_steps = 1000
batch_size = 10000
display_step = 100
epochs = 10

nodes_hidden1 = 128
# concatenated = 128+128 = 256
nodes_hidden3 = 128
nodes_hidden4 = 64


class Neural_Net:
    def __init__(self, num_features, num_classes, nodes_hidden1 = nodes_hidden1, nodes_hidden3 = nodes_hidden3,
                 nodes_hidden4 = nodes_hidden4, learning_rate = learning_rate):
        random_normal = tf.initializers.RandomNormal()
        self.num_features = num_features
        self.num_classes = num_classes
        self.learning_rate = learning_rate

        self.weights = {
            'h11': tf.Variable(random_normal([num_features, nodes_hidden1])),
            'h12': tf.Variable(random_normal([num_features, nodes_hidden1])),
            'h3' : tf.Variable(random_normal([2*nodes_hidden1, nodes_hidden3])),
            'h4' : tf.Variable(random_normal([nodes_hidden3, nodes_hidden4])),
            'out': tf.Variable(random_normal([nodes_hidden4, num_classes]))
        }

        self.biases = {
            'b11': tf.Variable(tf.zeros([nodes_hidden1])),
            'b12': tf.Variable(tf.zeros([nodes_hidden1])),
            'b3' : tf.Variable(tf.zeros([nodes_hidden3])),
            'b4' : tf.Variable(tf.zeros([nodes_hidden4])),
            'out': tf.Variable(tf.zeros([num_classes]))
        }

        self.optimizer = tf.optimizers.SGD(learning_rate)

    def model(self, x1, x2):
        layer_11 = tf.add(tf.matmul(x1, self.weights['h11']), self.biases['b11'])
        layer_11 = tf.nn.sigmoid(layer_11)
        # print(tf.shape(layer_11))
        layer_12 = tf.add(tf.matmul(x2, self.weights['h12']), self.biases['b12'])
        layer_12 = tf.nn.sigmoid(layer_12)
        # print(tf.shape(layer_12))
        layer_2 = tf.concat([layer_11, layer_12], 1)
        # print(tf.shape(layer_2))
        layer_3 = tf.add(tf.matmul(layer_2, self.weights['h3']), self.biases['b3'])
        layer_3 = tf.nn.sigmoid(layer_3)
        # print(tf.shape(layer_3))
        layer_4 = tf.add(tf.matmul(layer_3, self.weights['h4']), self.biases['b4'])
        layer_4 = tf.nn.sigmoid(layer_4)
        # print(tf.shape(layer_4))
        out_layer = tf.add(tf.matmul(layer_4, self.weights['out']), self.biases['out'])
        return tf.nn.softmax(out_layer)



    def cross_entropy(self, y_pred, y_true):
        y_true = tf.one_hot(y_true, depth = 2)
        # Clip prediction values to avoid log(0) error.
        y_pred = tf.clip_by_value(y_pred, 1e-9, 1.)
        return tf.reduce_mean(-tf.reduce_sum(y_true * tf.math.log(y_pred)))

    def accuracy(self, y_pred, y_true):
        # Predicted class is the index of highest score in prediction vector (i.e. argmax).
        correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
        return tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)

    # Optimization process.
    def run_optimization(self, x1, x2, y):
        # Wrap computation inside a GradientTape for automatic differentiation.
        with tf.GradientTape() as g:
            pred = self.model(x1,x2)
            loss = self.cross_entropy(pred, y)
            accuracy = self.accuracy(pred, y)

        # Variables to update, i.e. trainable variables.
        trainable_variables = list(self.weights.values()) + list(self.biases.values())

        # Compute gradients.
        gradients = g.gradient(loss, trainable_variables)

        # Update W and b following gradients.
        self.optimizer.apply_gradients(zip(gradients, trainable_variables))

        return pred, loss, accuracy

    def get_batches(self,df_pok, df_combat, index_start, index_end):
        x1 = []
        x2 = []
        y = []
        for i in range(index_start, index_end):
            try:
                x1.append(list(df_pok.iloc[df_combat['First_pokemon'].iloc[i] - 1])[1:])
                x2.append(list(df_pok.iloc[df_combat['Second_pokemon'].iloc[i] - 1])[1:])
                y.append(df_combat['Winner_index'].iloc[i])
            except:
                print(i)

        return np.array(x1, dtype=np.float32), np.array(x2, dtype=np.float32), np.array(y, dtype=np.int32)


    def train(self, df_pok, df_combat, epochs=epochs, batch_size = batch_size):
        length = len(df_combat)
        for epoch in range(1,epochs+1):
            print("In epoch is : "+str(epoch))
            df_combat = df_combat.sample(frac = 1)
            for step in range(0, length-1, batch_size):
                batch_x1, batch_x2, batch_y = self.get_batches(df_pok, df_combat, step, step+batch_size)
                # print("Step : " + str(step)+" weight b11 : ", end=" ")
                # tf.print(self.biases['b11'])
                pred, loss, accuracy = self.run_optimization(batch_x1, batch_x2, batch_y)

                print("step: %i, loss: %f, accuracy: %f" % (step, loss, accuracy))






if __name__ == '__main__':
    '''
    lets say : data is = 10, 5, 5  #first_pokemon, second_pokemon, winner
    and 10: 20, 15, 50, 85, 0  #speed, attack, defense, total, legendary
    and 5:  60, 20, 30, 110, 1
    x1 = np.array([[20, 15, 50, 85, 0],
                   [30, 10, 15, 20, 1]], dtype=np.float32)
    x2 = np.array([[60, 20, 30, 110, 1],
                   [10, 5, 13, 20, 0]], dtype=np.float32)
    y = [1, 0]
    
    '''

    x1 = np.array([[20, 15, 50, 85, 0]], dtype=np.float32)
    x2 = np.array([[60, 20, 30, 110, 1]], dtype=np.float32)
    y = [0,1]

    nn = Neural_Net(5,2)
    nn.train(x1,x2,y)















