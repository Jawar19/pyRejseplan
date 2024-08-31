"""Testcases for getters and setters in departure board
"""

def test_use_bus_getter(t_departureboard):
    """Test use bus property getter

    Arguments:
        t_departureboard -- Fixture
    """
    assert t_departureboard.use_bus, "Default value for use_bus not True"

def test_use_bus_setter(t_departureboard):
    """Test use bus property setter

    Arguments:
        t_departureboard -- Fixture
    """
    t_departureboard.use_bus = False
    assert not t_departureboard.use_bus, "use_bus property not working"

def test_use_train_getter(t_departureboard):
    """Test use train property getter

    Arguments:
        t_departureboard -- Fixture
    """
    assert t_departureboard.use_train, "Default value for use_bus not True"

def test_use_train_setter(t_departureboard):
    """Test use train property setter

    Arguments:
        t_departureboard -- Fixture
    """
    t_departureboard.use_train = False
    assert not t_departureboard.use_train, "use_bus property not working"

def test_use_metro_getter(t_departureboard):
    """Test use metro property getter

    Arguments:
        t_departureboard -- Fixture
    """
    assert t_departureboard.use_metro, "Default value for use_bus not True"

def test_use_metro_setter(t_departureboard):
    """Test use metro property setter

    Arguments:
        t_departureboard -- Fixture
    """
    t_departureboard.use_metro = False
    assert not t_departureboard.use_metro, "use_bus property not working"

def test_add_stopid(t_departureboard):
    """Test add stop id functionality

    Arguments:
        t_departureboard -- Fixture
    """
    stopids_to_add = [111,222,333,444]
    t_departureboard.add_stop_ids(stopids_to_add)

    assert t_departureboard.stop_ids == stopids_to_add

def test_remove_stopid(t_departureboard):
    """Test add stop id functionality

    Arguments:
        t_departureboard -- Fixture
    """
    stopids_to_add = [111,222,333,444]
    stopids_to_remove = [222, 444]
    t_departureboard.add_stop_ids(stopids_to_add)
    t_departureboard.remove_stop_ids(stopids_to_remove)
    assert len(t_departureboard.stop_ids) == 2, "Stop ID list wrong length"
    assert t_departureboard.stop_ids == [111,333], "Incorrect deletion"

def test_clear_stopid(t_departureboard, key):
    """Test add stop id functionality

    Arguments:
        t_departureboard -- Fixture
    """
    stopids_to_add = [111,222,333,444]
    t_departureboard.add_stop_ids(stopids_to_add)
    t_departureboard.clear_stop_ids()

    assert len(t_departureboard.stop_ids) == 0, "Stop ID list wrong length"
    assert not t_departureboard.stop_ids, "Incorrect deletion"
