import pytest
#import pandas as pd

from collections import namedtuple
from collections import OrderedDict

import actcv

class TestActCV(object):

    def test_tuple_to_dict_general_output(self):
        Pandas = namedtuple('Pandas', [ 'Index', 
                                        'Sebastian', 
                                        'Tim', 
                                        'Alina', 
                                        'Max', 
                                        'Peter'])
        input_tuple = Pandas(0, 1, 2, 3, 4, 5)

        expected_output = OrderedDict([ ('Sebastian', 1), 
                                        ('Tim', 2), 
                                        ('Alina', 3), 
                                        ('Max', 4), 
                                        ('Peter', 5)])
        observed_output =  actcv.ActCV.tuple_to_dict(self, input_tuple)

        assert observed_output == expected_output