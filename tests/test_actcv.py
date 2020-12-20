import pytest
import pandas as pd

import .actcv as actcv

class TestActCV(object):

  def test_tuple_to_dict(self):
        input_tuple = Pandas(Index=0, Sebastian=1, Tim=2, Alina=3, Max=4, Peter=5)

        expected_output = OrderedDict([('Sebastian', 1), ('Tim', 2), ('Alina', 3), ('Max', 4), ('Peter', 5)])
        
        observed_output = actcv.tuple_to_dict(input_tuple)

        pd.testing.assert_frame_equal(
            observed_sales_data.reset_index(drop=True),
            expected_sales_data.reset_index(drop=True),
            check_dtype=False,
        )


  def test_set_states(self):
        input_tuple = Pandas(Index=0, Sebastian=1, Tim=2, Alina=3, Max=4, Peter=5)

        expected_output = OrderedDict([('Sebastian', 1), ('Tim', 2), ('Alina', 3), ('Max', 4), ('Peter', 5)])
        
        observed_offsetdict, observed_statedict = actcv.set_states(data)

        pd.testing.assert_frame_equal(
            observed_sales_data.reset_index(drop=True),
            expected_sales_data.reset_index(drop=True),
            check_dtype=False,
        )