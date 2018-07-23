# Python stubs generated by omniidl from /tmp/corba/omni/share/idl/omniORB/COS/CosEventComm.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "CosEventComm"
#
__name__ = "CosEventComm"
_0_CosEventComm = omniORB.openModule("CosEventComm", r"/tmp/corba/omni/share/idl/omniORB/COS/CosEventComm.idl")
_0_CosEventComm__POA = omniORB.openModule("CosEventComm__POA", r"/tmp/corba/omni/share/idl/omniORB/COS/CosEventComm.idl")


# exception Disconnected
_0_CosEventComm.Disconnected = omniORB.newEmptyClass()
class Disconnected (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosEventComm/Disconnected:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosEventComm.Disconnected = Disconnected
_0_CosEventComm._d_Disconnected  = (omniORB.tcInternal.tv_except, Disconnected, Disconnected._NP_RepositoryId, "Disconnected")
_0_CosEventComm._tc_Disconnected = omniORB.tcInternal.createTypeCode(_0_CosEventComm._d_Disconnected)
omniORB.registerType(Disconnected._NP_RepositoryId, _0_CosEventComm._d_Disconnected, _0_CosEventComm._tc_Disconnected)
del Disconnected

# interface PushConsumer
_0_CosEventComm._d_PushConsumer = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosEventComm/PushConsumer:1.0", "PushConsumer")
omniORB.typeMapping["IDL:omg.org/CosEventComm/PushConsumer:1.0"] = _0_CosEventComm._d_PushConsumer
_0_CosEventComm.PushConsumer = omniORB.newEmptyClass()
class PushConsumer :
    _NP_RepositoryId = _0_CosEventComm._d_PushConsumer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosEventComm.PushConsumer = PushConsumer
_0_CosEventComm._tc_PushConsumer = omniORB.tcInternal.createTypeCode(_0_CosEventComm._d_PushConsumer)
omniORB.registerType(PushConsumer._NP_RepositoryId, _0_CosEventComm._d_PushConsumer, _0_CosEventComm._tc_PushConsumer)

# PushConsumer operations and attributes
PushConsumer._d_push = ((omniORB.tcInternal.tv_any, ), (), {_0_CosEventComm.Disconnected._NP_RepositoryId: _0_CosEventComm._d_Disconnected})
PushConsumer._d_disconnect_push_consumer = ((), (), None)

# PushConsumer object reference
class _objref_PushConsumer (CORBA.Object):
    _NP_RepositoryId = PushConsumer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def push(self, *args):
        return self._obj.invoke("push", _0_CosEventComm.PushConsumer._d_push, args)

    def disconnect_push_consumer(self, *args):
        return self._obj.invoke("disconnect_push_consumer", _0_CosEventComm.PushConsumer._d_disconnect_push_consumer, args)

omniORB.registerObjref(PushConsumer._NP_RepositoryId, _objref_PushConsumer)
_0_CosEventComm._objref_PushConsumer = _objref_PushConsumer
del PushConsumer, _objref_PushConsumer

# PushConsumer skeleton
__name__ = "CosEventComm__POA"
class PushConsumer (PortableServer.Servant):
    _NP_RepositoryId = _0_CosEventComm.PushConsumer._NP_RepositoryId


    _omni_op_d = {"push": _0_CosEventComm.PushConsumer._d_push, "disconnect_push_consumer": _0_CosEventComm.PushConsumer._d_disconnect_push_consumer}

PushConsumer._omni_skeleton = PushConsumer
_0_CosEventComm__POA.PushConsumer = PushConsumer
omniORB.registerSkeleton(PushConsumer._NP_RepositoryId, PushConsumer)
del PushConsumer
__name__ = "CosEventComm"

# interface PushSupplier
_0_CosEventComm._d_PushSupplier = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosEventComm/PushSupplier:1.0", "PushSupplier")
omniORB.typeMapping["IDL:omg.org/CosEventComm/PushSupplier:1.0"] = _0_CosEventComm._d_PushSupplier
_0_CosEventComm.PushSupplier = omniORB.newEmptyClass()
class PushSupplier :
    _NP_RepositoryId = _0_CosEventComm._d_PushSupplier[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosEventComm.PushSupplier = PushSupplier
_0_CosEventComm._tc_PushSupplier = omniORB.tcInternal.createTypeCode(_0_CosEventComm._d_PushSupplier)
omniORB.registerType(PushSupplier._NP_RepositoryId, _0_CosEventComm._d_PushSupplier, _0_CosEventComm._tc_PushSupplier)

# PushSupplier operations and attributes
PushSupplier._d_disconnect_push_supplier = ((), (), None)

# PushSupplier object reference
class _objref_PushSupplier (CORBA.Object):
    _NP_RepositoryId = PushSupplier._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def disconnect_push_supplier(self, *args):
        return self._obj.invoke("disconnect_push_supplier", _0_CosEventComm.PushSupplier._d_disconnect_push_supplier, args)

omniORB.registerObjref(PushSupplier._NP_RepositoryId, _objref_PushSupplier)
_0_CosEventComm._objref_PushSupplier = _objref_PushSupplier
del PushSupplier, _objref_PushSupplier

# PushSupplier skeleton
__name__ = "CosEventComm__POA"
class PushSupplier (PortableServer.Servant):
    _NP_RepositoryId = _0_CosEventComm.PushSupplier._NP_RepositoryId


    _omni_op_d = {"disconnect_push_supplier": _0_CosEventComm.PushSupplier._d_disconnect_push_supplier}

PushSupplier._omni_skeleton = PushSupplier
_0_CosEventComm__POA.PushSupplier = PushSupplier
omniORB.registerSkeleton(PushSupplier._NP_RepositoryId, PushSupplier)
del PushSupplier
__name__ = "CosEventComm"

# interface PullSupplier
_0_CosEventComm._d_PullSupplier = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosEventComm/PullSupplier:1.0", "PullSupplier")
omniORB.typeMapping["IDL:omg.org/CosEventComm/PullSupplier:1.0"] = _0_CosEventComm._d_PullSupplier
_0_CosEventComm.PullSupplier = omniORB.newEmptyClass()
class PullSupplier :
    _NP_RepositoryId = _0_CosEventComm._d_PullSupplier[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosEventComm.PullSupplier = PullSupplier
_0_CosEventComm._tc_PullSupplier = omniORB.tcInternal.createTypeCode(_0_CosEventComm._d_PullSupplier)
omniORB.registerType(PullSupplier._NP_RepositoryId, _0_CosEventComm._d_PullSupplier, _0_CosEventComm._tc_PullSupplier)

# PullSupplier operations and attributes
PullSupplier._d_pull = ((), (omniORB.tcInternal.tv_any, ), {_0_CosEventComm.Disconnected._NP_RepositoryId: _0_CosEventComm._d_Disconnected})
PullSupplier._d_try_pull = ((), (omniORB.tcInternal.tv_any, omniORB.tcInternal.tv_boolean), {_0_CosEventComm.Disconnected._NP_RepositoryId: _0_CosEventComm._d_Disconnected})
PullSupplier._d_disconnect_pull_supplier = ((), (), None)

# PullSupplier object reference
class _objref_PullSupplier (CORBA.Object):
    _NP_RepositoryId = PullSupplier._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def pull(self, *args):
        return self._obj.invoke("pull", _0_CosEventComm.PullSupplier._d_pull, args)

    def try_pull(self, *args):
        return self._obj.invoke("try_pull", _0_CosEventComm.PullSupplier._d_try_pull, args)

    def disconnect_pull_supplier(self, *args):
        return self._obj.invoke("disconnect_pull_supplier", _0_CosEventComm.PullSupplier._d_disconnect_pull_supplier, args)

omniORB.registerObjref(PullSupplier._NP_RepositoryId, _objref_PullSupplier)
_0_CosEventComm._objref_PullSupplier = _objref_PullSupplier
del PullSupplier, _objref_PullSupplier

# PullSupplier skeleton
__name__ = "CosEventComm__POA"
class PullSupplier (PortableServer.Servant):
    _NP_RepositoryId = _0_CosEventComm.PullSupplier._NP_RepositoryId


    _omni_op_d = {"pull": _0_CosEventComm.PullSupplier._d_pull, "try_pull": _0_CosEventComm.PullSupplier._d_try_pull, "disconnect_pull_supplier": _0_CosEventComm.PullSupplier._d_disconnect_pull_supplier}

PullSupplier._omni_skeleton = PullSupplier
_0_CosEventComm__POA.PullSupplier = PullSupplier
omniORB.registerSkeleton(PullSupplier._NP_RepositoryId, PullSupplier)
del PullSupplier
__name__ = "CosEventComm"

# interface PullConsumer
_0_CosEventComm._d_PullConsumer = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosEventComm/PullConsumer:1.0", "PullConsumer")
omniORB.typeMapping["IDL:omg.org/CosEventComm/PullConsumer:1.0"] = _0_CosEventComm._d_PullConsumer
_0_CosEventComm.PullConsumer = omniORB.newEmptyClass()
class PullConsumer :
    _NP_RepositoryId = _0_CosEventComm._d_PullConsumer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosEventComm.PullConsumer = PullConsumer
_0_CosEventComm._tc_PullConsumer = omniORB.tcInternal.createTypeCode(_0_CosEventComm._d_PullConsumer)
omniORB.registerType(PullConsumer._NP_RepositoryId, _0_CosEventComm._d_PullConsumer, _0_CosEventComm._tc_PullConsumer)

# PullConsumer operations and attributes
PullConsumer._d_disconnect_pull_consumer = ((), (), None)

# PullConsumer object reference
class _objref_PullConsumer (CORBA.Object):
    _NP_RepositoryId = PullConsumer._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def disconnect_pull_consumer(self, *args):
        return self._obj.invoke("disconnect_pull_consumer", _0_CosEventComm.PullConsumer._d_disconnect_pull_consumer, args)

omniORB.registerObjref(PullConsumer._NP_RepositoryId, _objref_PullConsumer)
_0_CosEventComm._objref_PullConsumer = _objref_PullConsumer
del PullConsumer, _objref_PullConsumer

# PullConsumer skeleton
__name__ = "CosEventComm__POA"
class PullConsumer (PortableServer.Servant):
    _NP_RepositoryId = _0_CosEventComm.PullConsumer._NP_RepositoryId


    _omni_op_d = {"disconnect_pull_consumer": _0_CosEventComm.PullConsumer._d_disconnect_pull_consumer}

PullConsumer._omni_skeleton = PullConsumer
_0_CosEventComm__POA.PullConsumer = PullConsumer
omniORB.registerSkeleton(PullConsumer._NP_RepositoryId, PullConsumer)
del PullConsumer
__name__ = "CosEventComm"

#
# End of module "CosEventComm"
#
__name__ = "CosEventComm_idl"

_exported_modules = ( "CosEventComm", )

# The end.
