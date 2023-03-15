import logging
from functools import reduce
from typing import Any, Final, Optional

from pyk.kore.prelude import INT, STRING, int_dv, string_dv
from pyk.kore.syntax import DV, App, Pattern, Sort, SortApp, String

_LOGGER: Final = logging.getLogger(__name__)


def gst_to_kore(gst_data: Any, schedule: str, mode: str, chainid: int) -> App:
    entries = (
        _config_map_entry('PGM', _json_to_kore(gst_data), SortApp('SortJSON')),
        _config_map_entry('SCHEDULE', _schedule_to_kore(schedule), SortApp('SortSchedule')),
        _config_map_entry('MODE', _mode_to_kore(mode), SortApp('SortMode')),
        _config_map_entry('CHAINID', _chainid_to_kore(chainid), SortApp('SortInt')),
    )
    return App(
        'LblinitGeneratedTopCell',
        (),
        (reduce(lambda x, y: App("Lbl'Unds'Map'Unds'", (), (x, y)), entries, App("Lbl'Stop'Map")),),
    )


def _config_map_entry(var: str, value: Pattern, sort: Sort) -> App:
    return App(
        "Lbl'UndsPipe'-'-GT-Unds'",
        (),
        (
            _sort_injection(SortApp('SortKConfigVar'), SortApp('SortKItem'), _k_config_var(var)),
            _sort_injection(sort, SortApp('SortKItem'), value),
        ),
    )


def _sort_injection(sort1: Sort, sort2: Sort, pattern: Pattern) -> App:
    return App('inj', (sort1, sort2), (pattern,))


def _k_config_var(_data: str) -> DV:
    return DV(SortApp('SortKConfigVar'), String(f'${_data}'))


def _json_to_kore(_data: Any, *, sort: Optional[Sort] = None) -> Pattern:
    if sort is None:
        sort = SortApp('SortJSON')

    if isinstance(_data, list):
        return App(
            'LblJSONList',
            (),
            (
                reduce(
                    lambda x, y: App('LblJSONs', (), (y, x)),
                    reversed([_json_to_kore(elem) for elem in _data]),
                    App("Lbl'Stop'List'LBraQuot'JSONs'QuotRBraUnds'JSONs"),
                ),
            ),
        )

    if isinstance(_data, dict):
        return App(
            'LblJSONObject',
            (),
            (
                reduce(
                    lambda x, y: App('LblJSONs', (), (App('LblJSONEntry', (), (y[0], y[1])), x)),
                    reversed(
                        [
                            (_json_to_kore(key, sort=SortApp('SortJSONKey')), _json_to_kore(value))
                            for key, value in _data.items()
                        ]
                    ),
                    App("Lbl'Stop'List'LBraQuot'JSONs'QuotRBraUnds'JSONs"),
                ),
            ),
        )

    if isinstance(_data, str):
        return _sort_injection(STRING, sort, string_dv(_data))

    if isinstance(_data, int):
        return _sort_injection(INT, sort, int_dv(_data))

    raise AssertionError()


def _schedule_to_kore(schedule: str) -> App:
    return App(f"Lbl{schedule}'Unds'EVM")


def _chainid_to_kore(chainid: int) -> DV:
    return int_dv(chainid)


def _mode_to_kore(mode: str) -> App:
    return App(f'Lbl{mode}')
