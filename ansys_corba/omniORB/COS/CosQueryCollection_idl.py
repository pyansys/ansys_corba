# Python stubs generated by omniidl from /tmp/corba/omni/share/idl/omniORB/COS/CosQueryCollection.idl
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
# Start of module "CosQueryCollection"
#
__name__ = "CosQueryCollection"
_0_CosQueryCollection = omniORB.openModule("CosQueryCollection", r"/tmp/corba/omni/share/idl/omniORB/COS/CosQueryCollection.idl")
_0_CosQueryCollection__POA = omniORB.openModule("CosQueryCollection__POA", r"/tmp/corba/omni/share/idl/omniORB/COS/CosQueryCollection.idl")


# exception ElementInvalid
_0_CosQueryCollection.ElementInvalid = omniORB.newEmptyClass()
class ElementInvalid (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/ElementInvalid:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosQueryCollection.ElementInvalid = ElementInvalid
_0_CosQueryCollection._d_ElementInvalid  = (omniORB.tcInternal.tv_except, ElementInvalid, ElementInvalid._NP_RepositoryId, "ElementInvalid")
_0_CosQueryCollection._tc_ElementInvalid = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_ElementInvalid)
omniORB.registerType(ElementInvalid._NP_RepositoryId, _0_CosQueryCollection._d_ElementInvalid, _0_CosQueryCollection._tc_ElementInvalid)
del ElementInvalid

# exception IteratorInvalid
_0_CosQueryCollection.IteratorInvalid = omniORB.newEmptyClass()
class IteratorInvalid (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/IteratorInvalid:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosQueryCollection.IteratorInvalid = IteratorInvalid
_0_CosQueryCollection._d_IteratorInvalid  = (omniORB.tcInternal.tv_except, IteratorInvalid, IteratorInvalid._NP_RepositoryId, "IteratorInvalid")
_0_CosQueryCollection._tc_IteratorInvalid = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_IteratorInvalid)
omniORB.registerType(IteratorInvalid._NP_RepositoryId, _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection._tc_IteratorInvalid)
del IteratorInvalid

# exception PositionInvalid
_0_CosQueryCollection.PositionInvalid = omniORB.newEmptyClass()
class PositionInvalid (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/PositionInvalid:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosQueryCollection.PositionInvalid = PositionInvalid
_0_CosQueryCollection._d_PositionInvalid  = (omniORB.tcInternal.tv_except, PositionInvalid, PositionInvalid._NP_RepositoryId, "PositionInvalid")
_0_CosQueryCollection._tc_PositionInvalid = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_PositionInvalid)
omniORB.registerType(PositionInvalid._NP_RepositoryId, _0_CosQueryCollection._d_PositionInvalid, _0_CosQueryCollection._tc_PositionInvalid)
del PositionInvalid

# enum ValueType
_0_CosQueryCollection.TypeBoolean = omniORB.EnumItem("TypeBoolean", 0)
_0_CosQueryCollection.TypeChar = omniORB.EnumItem("TypeChar", 1)
_0_CosQueryCollection.TypeOctet = omniORB.EnumItem("TypeOctet", 2)
_0_CosQueryCollection.TypeShort = omniORB.EnumItem("TypeShort", 3)
_0_CosQueryCollection.TypeUShort = omniORB.EnumItem("TypeUShort", 4)
_0_CosQueryCollection.TypeLong = omniORB.EnumItem("TypeLong", 5)
_0_CosQueryCollection.TypeULong = omniORB.EnumItem("TypeULong", 6)
_0_CosQueryCollection.TypeFloat = omniORB.EnumItem("TypeFloat", 7)
_0_CosQueryCollection.TypeDouble = omniORB.EnumItem("TypeDouble", 8)
_0_CosQueryCollection.TypeString = omniORB.EnumItem("TypeString", 9)
_0_CosQueryCollection.TypeObject = omniORB.EnumItem("TypeObject", 10)
_0_CosQueryCollection.TypeAny = omniORB.EnumItem("TypeAny", 11)
_0_CosQueryCollection.TypeSmallInt = omniORB.EnumItem("TypeSmallInt", 12)
_0_CosQueryCollection.TypeInteger = omniORB.EnumItem("TypeInteger", 13)
_0_CosQueryCollection.TypeReal = omniORB.EnumItem("TypeReal", 14)
_0_CosQueryCollection.TypeDoublePrecision = omniORB.EnumItem("TypeDoublePrecision", 15)
_0_CosQueryCollection.TypeCharacter = omniORB.EnumItem("TypeCharacter", 16)
_0_CosQueryCollection.TypeDecimal = omniORB.EnumItem("TypeDecimal", 17)
_0_CosQueryCollection.TypeNumeric = omniORB.EnumItem("TypeNumeric", 18)
_0_CosQueryCollection.ValueType = omniORB.Enum("IDL:omg.org/CosQueryCollection/ValueType:1.0", (_0_CosQueryCollection.TypeBoolean, _0_CosQueryCollection.TypeChar, _0_CosQueryCollection.TypeOctet, _0_CosQueryCollection.TypeShort, _0_CosQueryCollection.TypeUShort, _0_CosQueryCollection.TypeLong, _0_CosQueryCollection.TypeULong, _0_CosQueryCollection.TypeFloat, _0_CosQueryCollection.TypeDouble, _0_CosQueryCollection.TypeString, _0_CosQueryCollection.TypeObject, _0_CosQueryCollection.TypeAny, _0_CosQueryCollection.TypeSmallInt, _0_CosQueryCollection.TypeInteger, _0_CosQueryCollection.TypeReal, _0_CosQueryCollection.TypeDoublePrecision, _0_CosQueryCollection.TypeCharacter, _0_CosQueryCollection.TypeDecimal, _0_CosQueryCollection.TypeNumeric,))

_0_CosQueryCollection._d_ValueType  = (omniORB.tcInternal.tv_enum, _0_CosQueryCollection.ValueType._NP_RepositoryId, "ValueType", _0_CosQueryCollection.ValueType._items)
_0_CosQueryCollection._tc_ValueType = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_ValueType)
omniORB.registerType(_0_CosQueryCollection.ValueType._NP_RepositoryId, _0_CosQueryCollection._d_ValueType, _0_CosQueryCollection._tc_ValueType)

# struct Decimal
_0_CosQueryCollection.Decimal = omniORB.newEmptyClass()
class Decimal (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/Decimal:1.0"

    def __init__(self, precision, scale, value):
        self.precision = precision
        self.scale = scale
        self.value = value

_0_CosQueryCollection.Decimal = Decimal
_0_CosQueryCollection._d_Decimal  = (omniORB.tcInternal.tv_struct, Decimal, Decimal._NP_RepositoryId, "Decimal", "precision", omniORB.tcInternal.tv_long, "scale", omniORB.tcInternal.tv_long, "value", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_octet, 0))
_0_CosQueryCollection._tc_Decimal = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_Decimal)
omniORB.registerType(Decimal._NP_RepositoryId, _0_CosQueryCollection._d_Decimal, _0_CosQueryCollection._tc_Decimal)
del Decimal

# union Value
_0_CosQueryCollection.Value = omniORB.newEmptyClass()
class Value (omniORB.Union):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/Value:1.0"

_0_CosQueryCollection.Value = Value

Value._m_to_d = {"b": _0_CosQueryCollection.TypeBoolean, "c": _0_CosQueryCollection.TypeChar, "o": _0_CosQueryCollection.TypeOctet, "s": _0_CosQueryCollection.TypeShort, "us": _0_CosQueryCollection.TypeUShort, "l": _0_CosQueryCollection.TypeLong, "ul": _0_CosQueryCollection.TypeULong, "f": _0_CosQueryCollection.TypeFloat, "d": _0_CosQueryCollection.TypeDouble, "str": _0_CosQueryCollection.TypeString, "obj": _0_CosQueryCollection.TypeObject, "a": _0_CosQueryCollection.TypeAny, "si": _0_CosQueryCollection.TypeSmallInt, "i": _0_CosQueryCollection.TypeInteger, "r": _0_CosQueryCollection.TypeReal, "dp": _0_CosQueryCollection.TypeDoublePrecision, "ch": _0_CosQueryCollection.TypeCharacter, "dec": _0_CosQueryCollection.TypeDecimal, "n": _0_CosQueryCollection.TypeNumeric}
Value._d_to_m = {_0_CosQueryCollection.TypeBoolean: "b", _0_CosQueryCollection.TypeChar: "c", _0_CosQueryCollection.TypeOctet: "o", _0_CosQueryCollection.TypeShort: "s", _0_CosQueryCollection.TypeUShort: "us", _0_CosQueryCollection.TypeLong: "l", _0_CosQueryCollection.TypeULong: "ul", _0_CosQueryCollection.TypeFloat: "f", _0_CosQueryCollection.TypeDouble: "d", _0_CosQueryCollection.TypeString: "str", _0_CosQueryCollection.TypeObject: "obj", _0_CosQueryCollection.TypeAny: "a", _0_CosQueryCollection.TypeSmallInt: "si", _0_CosQueryCollection.TypeInteger: "i", _0_CosQueryCollection.TypeReal: "r", _0_CosQueryCollection.TypeDoublePrecision: "dp", _0_CosQueryCollection.TypeCharacter: "ch", _0_CosQueryCollection.TypeDecimal: "dec", _0_CosQueryCollection.TypeNumeric: "n"}
Value._def_m  = None
Value._def_d  = None

_0_CosQueryCollection._m_Value  = ((_0_CosQueryCollection.TypeBoolean, "b", omniORB.tcInternal.tv_boolean), (_0_CosQueryCollection.TypeChar, "c", omniORB.tcInternal.tv_char), (_0_CosQueryCollection.TypeOctet, "o", omniORB.tcInternal.tv_octet), (_0_CosQueryCollection.TypeShort, "s", omniORB.tcInternal.tv_short), (_0_CosQueryCollection.TypeUShort, "us", omniORB.tcInternal.tv_ushort), (_0_CosQueryCollection.TypeLong, "l", omniORB.tcInternal.tv_long), (_0_CosQueryCollection.TypeULong, "ul", omniORB.tcInternal.tv_ulong), (_0_CosQueryCollection.TypeFloat, "f", omniORB.tcInternal.tv_float), (_0_CosQueryCollection.TypeDouble, "d", omniORB.tcInternal.tv_double), (_0_CosQueryCollection.TypeString, "str", (omniORB.tcInternal.tv_string,0)), (_0_CosQueryCollection.TypeObject, "obj", omniORB.typeMapping["IDL:omg.org/CORBA/Object:1.0"]), (_0_CosQueryCollection.TypeAny, "a", omniORB.tcInternal.tv_any), (_0_CosQueryCollection.TypeSmallInt, "si", omniORB.tcInternal.tv_short), (_0_CosQueryCollection.TypeInteger, "i", omniORB.tcInternal.tv_long), (_0_CosQueryCollection.TypeReal, "r", omniORB.tcInternal.tv_float), (_0_CosQueryCollection.TypeDoublePrecision, "dp", omniORB.tcInternal.tv_double), (_0_CosQueryCollection.TypeCharacter, "ch", (omniORB.tcInternal.tv_string,0)), (_0_CosQueryCollection.TypeDecimal, "dec", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Decimal:1.0"]), (_0_CosQueryCollection.TypeNumeric, "n", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Decimal:1.0"]),)
_0_CosQueryCollection._d_Value  = (omniORB.tcInternal.tv_union, Value, Value._NP_RepositoryId, "Value", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/ValueType:1.0"], -1, _0_CosQueryCollection._m_Value, None, {_0_CosQueryCollection.TypeBoolean: _0_CosQueryCollection._m_Value[0], _0_CosQueryCollection.TypeChar: _0_CosQueryCollection._m_Value[1], _0_CosQueryCollection.TypeOctet: _0_CosQueryCollection._m_Value[2], _0_CosQueryCollection.TypeShort: _0_CosQueryCollection._m_Value[3], _0_CosQueryCollection.TypeUShort: _0_CosQueryCollection._m_Value[4], _0_CosQueryCollection.TypeLong: _0_CosQueryCollection._m_Value[5], _0_CosQueryCollection.TypeULong: _0_CosQueryCollection._m_Value[6], _0_CosQueryCollection.TypeFloat: _0_CosQueryCollection._m_Value[7], _0_CosQueryCollection.TypeDouble: _0_CosQueryCollection._m_Value[8], _0_CosQueryCollection.TypeString: _0_CosQueryCollection._m_Value[9], _0_CosQueryCollection.TypeObject: _0_CosQueryCollection._m_Value[10], _0_CosQueryCollection.TypeAny: _0_CosQueryCollection._m_Value[11], _0_CosQueryCollection.TypeSmallInt: _0_CosQueryCollection._m_Value[12], _0_CosQueryCollection.TypeInteger: _0_CosQueryCollection._m_Value[13], _0_CosQueryCollection.TypeReal: _0_CosQueryCollection._m_Value[14], _0_CosQueryCollection.TypeDoublePrecision: _0_CosQueryCollection._m_Value[15], _0_CosQueryCollection.TypeCharacter: _0_CosQueryCollection._m_Value[16], _0_CosQueryCollection.TypeDecimal: _0_CosQueryCollection._m_Value[17], _0_CosQueryCollection.TypeNumeric: _0_CosQueryCollection._m_Value[18]})
_0_CosQueryCollection._tc_Value = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_Value)
omniORB.registerType(Value._NP_RepositoryId, _0_CosQueryCollection._d_Value, _0_CosQueryCollection._tc_Value)
del Value

# typedef ... Null
class Null:
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/Null:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosQueryCollection.Null = Null
_0_CosQueryCollection._d_Null  = omniORB.tcInternal.tv_boolean
_0_CosQueryCollection._ad_Null = (omniORB.tcInternal.tv_alias, Null._NP_RepositoryId, "Null", omniORB.tcInternal.tv_boolean)
_0_CosQueryCollection._tc_Null = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._ad_Null)
omniORB.registerType(Null._NP_RepositoryId, _0_CosQueryCollection._ad_Null, _0_CosQueryCollection._tc_Null)
del Null

# union FieldValue
_0_CosQueryCollection.FieldValue = omniORB.newEmptyClass()
class FieldValue (omniORB.Union):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/FieldValue:1.0"

_0_CosQueryCollection.FieldValue = FieldValue

FieldValue._m_to_d = {"v": 0}
FieldValue._d_to_m = {0: "v"}
FieldValue._def_m  = None
FieldValue._def_d  = None

_0_CosQueryCollection._m_FieldValue  = ((0, "v", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Value:1.0"]),)
_0_CosQueryCollection._d_FieldValue  = (omniORB.tcInternal.tv_union, FieldValue, FieldValue._NP_RepositoryId, "FieldValue", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Null:1.0"], -1, _0_CosQueryCollection._m_FieldValue, None, {0: _0_CosQueryCollection._m_FieldValue[0]})
_0_CosQueryCollection._tc_FieldValue = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_FieldValue)
omniORB.registerType(FieldValue._NP_RepositoryId, _0_CosQueryCollection._d_FieldValue, _0_CosQueryCollection._tc_FieldValue)
del FieldValue

# typedef ... Record
class Record:
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/Record:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosQueryCollection.Record = Record
_0_CosQueryCollection._d_Record  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/FieldValue:1.0"], 0)
_0_CosQueryCollection._ad_Record = (omniORB.tcInternal.tv_alias, Record._NP_RepositoryId, "Record", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/FieldValue:1.0"], 0))
_0_CosQueryCollection._tc_Record = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._ad_Record)
omniORB.registerType(Record._NP_RepositoryId, _0_CosQueryCollection._ad_Record, _0_CosQueryCollection._tc_Record)
del Record

# typedef ... Istring
class Istring:
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/Istring:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosQueryCollection.Istring = Istring
_0_CosQueryCollection._d_Istring  = (omniORB.tcInternal.tv_string,0)
_0_CosQueryCollection._ad_Istring = (omniORB.tcInternal.tv_alias, Istring._NP_RepositoryId, "Istring", (omniORB.tcInternal.tv_string,0))
_0_CosQueryCollection._tc_Istring = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._ad_Istring)
omniORB.registerType(Istring._NP_RepositoryId, _0_CosQueryCollection._ad_Istring, _0_CosQueryCollection._tc_Istring)
del Istring

# struct NVPair
_0_CosQueryCollection.NVPair = omniORB.newEmptyClass()
class NVPair (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/NVPair:1.0"

    def __init__(self, name, value):
        self.name = name
        self.value = value

_0_CosQueryCollection.NVPair = NVPair
_0_CosQueryCollection._d_NVPair  = (omniORB.tcInternal.tv_struct, NVPair, NVPair._NP_RepositoryId, "NVPair", "name", omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Istring:1.0"], "value", omniORB.tcInternal.tv_any)
_0_CosQueryCollection._tc_NVPair = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_NVPair)
omniORB.registerType(NVPair._NP_RepositoryId, _0_CosQueryCollection._d_NVPair, _0_CosQueryCollection._tc_NVPair)
del NVPair

# typedef ... ParameterList
class ParameterList:
    _NP_RepositoryId = "IDL:omg.org/CosQueryCollection/ParameterList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosQueryCollection.ParameterList = ParameterList
_0_CosQueryCollection._d_ParameterList  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/NVPair:1.0"], 0)
_0_CosQueryCollection._ad_ParameterList = (omniORB.tcInternal.tv_alias, ParameterList._NP_RepositoryId, "ParameterList", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/NVPair:1.0"], 0))
_0_CosQueryCollection._tc_ParameterList = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._ad_ParameterList)
omniORB.registerType(ParameterList._NP_RepositoryId, _0_CosQueryCollection._ad_ParameterList, _0_CosQueryCollection._tc_ParameterList)
del ParameterList

# forward interface Collection;
_0_CosQueryCollection._d_Collection = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosQueryCollection/Collection:1.0", "Collection")
omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Collection:1.0"] = _0_CosQueryCollection._d_Collection

# forward interface Iterator;
_0_CosQueryCollection._d_Iterator = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosQueryCollection/Iterator:1.0", "Iterator")
omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"] = _0_CosQueryCollection._d_Iterator

# interface CollectionFactory
_0_CosQueryCollection._d_CollectionFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosQueryCollection/CollectionFactory:1.0", "CollectionFactory")
omniORB.typeMapping["IDL:omg.org/CosQueryCollection/CollectionFactory:1.0"] = _0_CosQueryCollection._d_CollectionFactory
_0_CosQueryCollection.CollectionFactory = omniORB.newEmptyClass()
class CollectionFactory :
    _NP_RepositoryId = _0_CosQueryCollection._d_CollectionFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosQueryCollection.CollectionFactory = CollectionFactory
_0_CosQueryCollection._tc_CollectionFactory = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_CollectionFactory)
omniORB.registerType(CollectionFactory._NP_RepositoryId, _0_CosQueryCollection._d_CollectionFactory, _0_CosQueryCollection._tc_CollectionFactory)

# CollectionFactory operations and attributes
CollectionFactory._d_create = ((omniORB.typeMapping["IDL:omg.org/CosQueryCollection/ParameterList:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Collection:1.0"], ), None)

# CollectionFactory object reference
class _objref_CollectionFactory (CORBA.Object):
    _NP_RepositoryId = CollectionFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create(self, *args):
        return self._obj.invoke("create", _0_CosQueryCollection.CollectionFactory._d_create, args)

omniORB.registerObjref(CollectionFactory._NP_RepositoryId, _objref_CollectionFactory)
_0_CosQueryCollection._objref_CollectionFactory = _objref_CollectionFactory
del CollectionFactory, _objref_CollectionFactory

# CollectionFactory skeleton
__name__ = "CosQueryCollection__POA"
class CollectionFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosQueryCollection.CollectionFactory._NP_RepositoryId


    _omni_op_d = {"create": _0_CosQueryCollection.CollectionFactory._d_create}

CollectionFactory._omni_skeleton = CollectionFactory
_0_CosQueryCollection__POA.CollectionFactory = CollectionFactory
omniORB.registerSkeleton(CollectionFactory._NP_RepositoryId, CollectionFactory)
del CollectionFactory
__name__ = "CosQueryCollection"

# interface Collection
_0_CosQueryCollection._d_Collection = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosQueryCollection/Collection:1.0", "Collection")
omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Collection:1.0"] = _0_CosQueryCollection._d_Collection
_0_CosQueryCollection.Collection = omniORB.newEmptyClass()
class Collection :
    _NP_RepositoryId = _0_CosQueryCollection._d_Collection[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosQueryCollection.Collection = Collection
_0_CosQueryCollection._tc_Collection = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_Collection)
omniORB.registerType(Collection._NP_RepositoryId, _0_CosQueryCollection._d_Collection, _0_CosQueryCollection._tc_Collection)

# Collection operations and attributes
Collection._d__get_cardinality = ((),(omniORB.tcInternal.tv_long,),None)
Collection._d_add_element = ((omniORB.tcInternal.tv_any, ), (), {_0_CosQueryCollection.ElementInvalid._NP_RepositoryId: _0_CosQueryCollection._d_ElementInvalid})
Collection._d_add_all_elements = ((omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Collection:1.0"], ), (), {_0_CosQueryCollection.ElementInvalid._NP_RepositoryId: _0_CosQueryCollection._d_ElementInvalid})
Collection._d_insert_element_at = ((omniORB.tcInternal.tv_any, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"]), (), {_0_CosQueryCollection.IteratorInvalid._NP_RepositoryId: _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection.ElementInvalid._NP_RepositoryId: _0_CosQueryCollection._d_ElementInvalid})
Collection._d_replace_element_at = ((omniORB.tcInternal.tv_any, omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"]), (), {_0_CosQueryCollection.IteratorInvalid._NP_RepositoryId: _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection.PositionInvalid._NP_RepositoryId: _0_CosQueryCollection._d_PositionInvalid, _0_CosQueryCollection.ElementInvalid._NP_RepositoryId: _0_CosQueryCollection._d_ElementInvalid})
Collection._d_remove_element_at = ((omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"], ), (), {_0_CosQueryCollection.IteratorInvalid._NP_RepositoryId: _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection.PositionInvalid._NP_RepositoryId: _0_CosQueryCollection._d_PositionInvalid})
Collection._d_remove_all_elements = ((), (), None)
Collection._d_retrieve_element_at = ((omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"], ), (omniORB.tcInternal.tv_any, ), {_0_CosQueryCollection.IteratorInvalid._NP_RepositoryId: _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection.PositionInvalid._NP_RepositoryId: _0_CosQueryCollection._d_PositionInvalid})
Collection._d_create_iterator = ((), (omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"], ), None)

# Collection object reference
class _objref_Collection (CORBA.Object):
    _NP_RepositoryId = Collection._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_cardinality(self, *args):
        return self._obj.invoke("_get_cardinality", _0_CosQueryCollection.Collection._d__get_cardinality, args)

    cardinality = property(_get_cardinality)


    def add_element(self, *args):
        return self._obj.invoke("add_element", _0_CosQueryCollection.Collection._d_add_element, args)

    def add_all_elements(self, *args):
        return self._obj.invoke("add_all_elements", _0_CosQueryCollection.Collection._d_add_all_elements, args)

    def insert_element_at(self, *args):
        return self._obj.invoke("insert_element_at", _0_CosQueryCollection.Collection._d_insert_element_at, args)

    def replace_element_at(self, *args):
        return self._obj.invoke("replace_element_at", _0_CosQueryCollection.Collection._d_replace_element_at, args)

    def remove_element_at(self, *args):
        return self._obj.invoke("remove_element_at", _0_CosQueryCollection.Collection._d_remove_element_at, args)

    def remove_all_elements(self, *args):
        return self._obj.invoke("remove_all_elements", _0_CosQueryCollection.Collection._d_remove_all_elements, args)

    def retrieve_element_at(self, *args):
        return self._obj.invoke("retrieve_element_at", _0_CosQueryCollection.Collection._d_retrieve_element_at, args)

    def create_iterator(self, *args):
        return self._obj.invoke("create_iterator", _0_CosQueryCollection.Collection._d_create_iterator, args)

omniORB.registerObjref(Collection._NP_RepositoryId, _objref_Collection)
_0_CosQueryCollection._objref_Collection = _objref_Collection
del Collection, _objref_Collection

# Collection skeleton
__name__ = "CosQueryCollection__POA"
class Collection (PortableServer.Servant):
    _NP_RepositoryId = _0_CosQueryCollection.Collection._NP_RepositoryId


    _omni_op_d = {"_get_cardinality": _0_CosQueryCollection.Collection._d__get_cardinality, "add_element": _0_CosQueryCollection.Collection._d_add_element, "add_all_elements": _0_CosQueryCollection.Collection._d_add_all_elements, "insert_element_at": _0_CosQueryCollection.Collection._d_insert_element_at, "replace_element_at": _0_CosQueryCollection.Collection._d_replace_element_at, "remove_element_at": _0_CosQueryCollection.Collection._d_remove_element_at, "remove_all_elements": _0_CosQueryCollection.Collection._d_remove_all_elements, "retrieve_element_at": _0_CosQueryCollection.Collection._d_retrieve_element_at, "create_iterator": _0_CosQueryCollection.Collection._d_create_iterator}

Collection._omni_skeleton = Collection
_0_CosQueryCollection__POA.Collection = Collection
omniORB.registerSkeleton(Collection._NP_RepositoryId, Collection)
del Collection
__name__ = "CosQueryCollection"

# interface Iterator
_0_CosQueryCollection._d_Iterator = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosQueryCollection/Iterator:1.0", "Iterator")
omniORB.typeMapping["IDL:omg.org/CosQueryCollection/Iterator:1.0"] = _0_CosQueryCollection._d_Iterator
_0_CosQueryCollection.Iterator = omniORB.newEmptyClass()
class Iterator :
    _NP_RepositoryId = _0_CosQueryCollection._d_Iterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosQueryCollection.Iterator = Iterator
_0_CosQueryCollection._tc_Iterator = omniORB.tcInternal.createTypeCode(_0_CosQueryCollection._d_Iterator)
omniORB.registerType(Iterator._NP_RepositoryId, _0_CosQueryCollection._d_Iterator, _0_CosQueryCollection._tc_Iterator)

# Iterator operations and attributes
Iterator._d_next = ((), (omniORB.tcInternal.tv_any, ), {_0_CosQueryCollection.IteratorInvalid._NP_RepositoryId: _0_CosQueryCollection._d_IteratorInvalid, _0_CosQueryCollection.PositionInvalid._NP_RepositoryId: _0_CosQueryCollection._d_PositionInvalid})
Iterator._d_reset = ((), (), None)
Iterator._d_more = ((), (omniORB.tcInternal.tv_boolean, ), None)

# Iterator object reference
class _objref_Iterator (CORBA.Object):
    _NP_RepositoryId = Iterator._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next(self, *args):
        return self._obj.invoke("next", _0_CosQueryCollection.Iterator._d_next, args)

    def reset(self, *args):
        return self._obj.invoke("reset", _0_CosQueryCollection.Iterator._d_reset, args)

    def more(self, *args):
        return self._obj.invoke("more", _0_CosQueryCollection.Iterator._d_more, args)

omniORB.registerObjref(Iterator._NP_RepositoryId, _objref_Iterator)
_0_CosQueryCollection._objref_Iterator = _objref_Iterator
del Iterator, _objref_Iterator

# Iterator skeleton
__name__ = "CosQueryCollection__POA"
class Iterator (PortableServer.Servant):
    _NP_RepositoryId = _0_CosQueryCollection.Iterator._NP_RepositoryId


    _omni_op_d = {"next": _0_CosQueryCollection.Iterator._d_next, "reset": _0_CosQueryCollection.Iterator._d_reset, "more": _0_CosQueryCollection.Iterator._d_more}

Iterator._omni_skeleton = Iterator
_0_CosQueryCollection__POA.Iterator = Iterator
omniORB.registerSkeleton(Iterator._NP_RepositoryId, Iterator)
del Iterator
__name__ = "CosQueryCollection"

#
# End of module "CosQueryCollection"
#
__name__ = "CosQueryCollection_idl"

_exported_modules = ( "CosQueryCollection", )

# The end.
