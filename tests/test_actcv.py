import pytest
import pandas as pd

import .actcv as actcv

class TestActCV(object):

  def test_(self):
          expected_sales_data = pd.DataFrame(
            {
                "x": ["3", "4", "5", "6", "7", "8"],
                "y": ["3", "4", "5", "6", "7", "8"],
                "s": [-10, -2.4, 0, 3, 5.5, None]
            
            }
        )
        (
            observed_data,
            observed_data_grouped,
        ) = actcv.function(
            x, y, s
        )
        pd.testing.assert_frame_equal(
            observed_sales_data.reset_index(drop=True),
            expected_sales_data.reset_index(drop=True),
            check_dtype=False,
        )
