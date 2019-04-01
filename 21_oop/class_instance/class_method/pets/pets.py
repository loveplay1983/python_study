class Pets:
    """
    The following code will cause problem when calling about()
    method since python interpreter cannot distinguish which 
    class instance is about to call.
     
    The correct version can be done by classmethod
    """
    name = 'Pets name'

    @staticmethod
    def about():
        print('This is {}'.format(Pets.name))

    @classmethod
    def info(cls):
        print('This is {}'.format(cls.name))


class Dogs(Pets):
    
    name = 'Doggy'

class Cats(Pets):

    name = 'Catty'




