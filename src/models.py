import tensorflow as tf


def cnnModel(input_shape=(99, 40)):
    """
    Model consisting of 4 convolution blocks
    """

    model = tf.keras.models.Sequential()

    # Normalization layer
    model.add(tf.keras.layers.Reshape(input_shape=input_shape, target_shape=(99, 40, 1)))
    model.add(tf.keras.layers.BatchNormalization())

    filters = [16, 32, 64, 128]

    for num_filters in filters:
        # Conv a
        model.add(tf.keras.layers.Conv2D(
            num_filters,
            kernel_size=(3, 3),
            padding='same'
            )
        )
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))

        # Conv b
        model.add(tf.keras.layers.Conv2D(
            num_filters,
            kernel_size=(3, 3),
            padding='same'
            )
        )
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.Activation('relu'))

        # Pooling
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(tf.keras.layers.Dropout(0.2))

    # Classification layers
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Activation('relu'))
    # linear
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    # softmax
    model.add(tf.keras.layers.Dense(30, activation='softmax'))

    return model


def lstmModel(input_shape=(99, 40)):
    '''
    Long-Short-Term-Memory model
    '''

    model = tf.keras.models.Sequential()

    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=3, input_shape=input_shape),input_shape=input_shape))
    model.add(tf.keras.layers.Attention())
    # model.add(tf.keras.layers.Dense(5)) # needed layer? also dense value?
    model.add(tf.keras.layers.Activation('softmax'))

    return model