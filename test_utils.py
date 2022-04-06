import pytest
from utils.utils import *
@pytest.fixture
def example_employees_data():
    return ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
              'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00;\n',
              'MOE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
              'HOMER=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n',
              'LENNY=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
              'CARL=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
              ]


@pytest.fixture
def example_schedule_data():
    return ['MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
            'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00;\n',
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n',
            'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00;\n',
             'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']

def test_extract_names(example_employees_data):

  assert extract_names(example_employees_data) == ["RENE","ASTRID","MOE","HOMER","LENNY","CARL"]



def test_extract_schedule_day(example_schedule_data):
  assert extract_schedule_day(example_schedule_data) ==  [['MO', 'TU', 'TH', 'SA', 'SU'],
                                                            ['MO', 'TH', 'SU'],
                                                            ['MO', 'TU', 'TH', 'SA', 'SU'],
                                                            ['MO', 'TU', 'TH', 'SA', 'SU'],
                                                            ['MO', 'TU', 'TH', 'SA', 'SU'],
                                                            ['MO', 'TU', 'TH', 'SA', 'SU']]


def test_extract_schedule_hours(example_schedule_data):
  assert extract_schedule_hours(example_schedule_data) == [['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00'],
                                                          ['10:00-12:00', '12:00-14:00', '20:00-21:00'],
                                                          ['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00'],
                                                          ['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00'],
                                                          ['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00'],
                                                          ['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00']]