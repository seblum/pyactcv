import pytest
import pandas as pd

from collections import namedtuple
from collections import OrderedDict

import actcv as cv

class TestActCV(object):

    def test_tuple_to_dict_general_output(self):
        Pandas = namedtuple('Pandas', ['Index', 'Sebastian', 'Tim', 'Alina', 'Max', 'Peter'])
        input_tuple = Pandas(0, 1, 2, 3, 4, 5)

        expected_output = OrderedDict([ ('Sebastian', 1), 
                                        ('Tim', 2), 
                                        ('Alina', 3), 
                                        ('Max', 4), 
                                        ('Peter', 5)])

        observed_output =  cv.ActCV.tuple_to_dict(input_tuple)

        pd.testing.assert_frame_equal(
            observed_sales_data.reset_index(drop=True),
            expected_sales_data.reset_index(drop=True),
            check_dtype=False,
        )