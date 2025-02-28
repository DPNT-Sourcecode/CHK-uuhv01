

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
#     This challenge is part of the warmup and will introduce you to the concept of penalties.

# Like this challenge, the official challenge will contain multiple rounds with multiple changing requirements.
# The purpose is to solve all the rounds as fast as possible. The timer does not stop between rounds.

# Deploying an implementation that is incomplete or has bugs will make your customers very unhappy and you will incur some costs. This is simulated with penalties.
# When your implementation fails in production, you will receive a penalty of 10 minutes and some feedback.

# Sometimes the requirements are poorly defined. Getting feedback from your users might be the only way to move forward.

# The requirement for this round is to say hello to the world. (I know, it's not well defined.)


# In order to complete the round you need to implement the following method:
#      hello(String) -> String

# Where:
#  - param[0] = a String. Ignore for now.
#  - @return = a String containing a message
#  - The message should be "Hello, World!".
    msg = f'Hello, {friend_name}!'
    print(msg)
    return msg