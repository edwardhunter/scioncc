#!/usr/bin/env python

__author__ = 'Michael Meisinger'
__license__ = 'Apache 2.0'

from pyon.ion.state import StateRepository
from pyon.util.unit_test import IonUnitTestCase
from unittest import SkipTest
from nose.plugins.attrib import attr


@attr('UNIT', group='datastore')
class TestState(IonUnitTestCase):

    def test_state(self):
        state_repo = StateRepository.get_instance()
        state_repo1 = StateRepository.get_instance()
        self.assertEquals(state_repo, state_repo1)

        state1 = {'key':'value1'}
        state_repo.put_state("id1", state1)

        state2 = state_repo.get_state("id1")
        self.assertEquals(state1, state2)

        state3 = {'key':'value2', 'key2': {}}
        state_repo.put_state("id1", state3)

        state4 = state_repo.get_state("id1")
        self.assertEquals(state3, state4)
