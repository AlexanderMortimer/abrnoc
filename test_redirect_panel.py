import pytest
from outputs import outputs_plans as op

def test_redirect():
    for region_id in op.plan(177):
        if region_id[1]==True:
            print(region_id)
            assert op.submit_plan(177,region_id[0]) == "https://mp"
        elif region_id[1] == False:
            print(region_id)
            assert op.submit_plan(177,region_id[1]) == "https://s"



