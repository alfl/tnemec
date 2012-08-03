"""Tests for cement.core.exc."""

from cement.core import exc
from cement.utils import test

class ExceptionTestCase(test.CementTestCase):
    @test.raises(exc.CementRuntimeError)
    def test_cement_runtime_error(self):
        try:
            raise exc.CementRuntimeError("CementRuntimeError Test")
        except exc.CementRuntimeError as e:
            self.eq(e.msg, "CementRuntimeError Test")
            self.eq(e.__str__(), "CementRuntimeError Test")
            raise
        
    @test.raises(exc.CementInterfaceError)
    def test_cement_interface_error(self):
        try:
            raise exc.CementInterfaceError("CementInterfaceError Test")
        except exc.CementInterfaceError as e:
            self.eq(e.msg, "CementInterfaceError Test")
            self.eq(e.__str__(), "CementInterfaceError Test")
            raise

    @test.raises(exc.CementSignalError)
    def test_cement_signal_error(self):
        try:
            import signal
            raise exc.CementSignalError(signal.SIGTERM, 5)
        except exc.CementSignalError as e:
            self.eq(e.signum, signal.SIGTERM)
            self.eq(e.frame, 5)
            raise
