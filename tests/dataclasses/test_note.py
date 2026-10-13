"""Tests for legacy and nested Rejseplan note XML."""

from py_rejseplan.dataclasses.note import Notes


def test_notes_parse_legacy_note_format():
    notes = Notes.from_xml(
        """
        <Notes xmlns="http://hacon.de/hafas/proxy/hafas-proxy">
            <Note key="BE" type="A" priority="0" txtN="Low-floor train">
                Low-floor train
            </Note>
        </Notes>
        """
    )

    assert len(notes.note) == 1
    note = notes.note[0]
    assert note.key == "BE"
    assert note.priority == 0
    assert note.txtN == "Low-floor train"
    assert note.value is None
    assert note.children == []
    assert note.text == "Low-floor train"


def test_notes_parse_new_nested_note_format():
    notes = Notes.from_xml(
        """
        <Notes xmlns="http://hacon.de/hafas/proxy/hafas-proxy">
            <Note key="parent" type="A">
                <value>Parent note</value>
                <Note key="child" type="I">
                    <value>Child note</value>
                </Note>
            </Note>
        </Notes>
        """
    )

    assert len(notes.note) == 1
    parent = notes.note[0]
    assert parent.key == "parent"
    assert parent.txtN is None
    assert parent.value == "Parent note"
    assert parent.text == "Parent note"

    assert len(parent.children) == 1
    child = parent.children[0]
    assert child.key == "child"
    assert child.value == "Child note"
    assert child.text == "Child note"
    assert child.children == []
