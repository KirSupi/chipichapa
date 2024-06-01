from tracemalloc import Snapshot


# PATTERN Command
class Command(object):
    _snapshot_before: Snapshot = None
    _snapshot_after: Snapshot = None

    def __init__(self, snapshot: Snapshot):
        self._snapshot_before = snapshot

    def do(self) -> Snapshot:
        if self._snapshot_after is not None:
            return self._snapshot_after

        self._snapshot_after = Snapshot()
        return self._snapshot_after

    def undo(self) -> Snapshot:
        return self._snapshot_before
