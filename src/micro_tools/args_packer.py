import _codecs
import _pickle


def args_key(function, args, kwargs):
    arguments = (args, kwargs)

    # NOTE: protocol=0 so it's ascii, this is crucial for py3k
    #       because shelve only works with proper strings.
    #       Otherwise, we'd get an exception because
    #       function.__name__ is str but dumps returns bytes.
    arguments_pickle = _codecs.encode(_pickle.dumps(arguments, protocol=0), "base64").decode()
    key = function.__name__ + arguments_pickle
    return key