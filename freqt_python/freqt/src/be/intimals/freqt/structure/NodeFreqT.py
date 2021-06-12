#!/usr/bin/env python3
class NodeFreqT:

    __node_label = ""  # String
    __node_label_int = -1  # Integer
    __lineNr = ""  # String
    __parent = -1  # Integer
    __child = -1  # Integer
    __sibling = -1  # Integer
    __degree = -1  # Integer
    __ordered = False # boolean
    # additional information in new singleTree
    __level = -1  # Integer
    __parentExt = -1  # Integer
    __childExt = -1  # Integer
    __siblingExt = -1  # Integer

    def nodeFreqtInit(self, _parent, _child, _sibling, _degree, _ordered):
        self.__node_label = ""
        self.__node_label_int = -1
        self.__lineNr = ""
        self.__parent = _parent
        self.__child = _child
        self.__sibling = _sibling
        self.__degree = _degree
        self.__ordered = _ordered
        # additional information in new singleTree
        self.__level = -1
        self.__parentExt = -1
        self.__childExt = -1
        self.__siblingExt = -1

    def setNode_label_int(self, node_label_int):
        self.__node_label_int = node_label_int

    def getNode_label_int(self):
        return self.__node_label_int

    # additional information for building single large tree
    def setNodeLevel(self, s):
        self.__level = s

    def setNodeSiblingExt(self, s):
        self.__siblingExt = s

    def setNodeChildExt(self, s):
        self.__childExt = s

    def setNodeParentExt(self, s):
        self.__parentExt = s

    def getNodeLevel(self):
        return self.__level

    def getNodeSiblingExt(self):
        return self.__siblingExt

    def getNodeChildExt(self):
        return self.__childExt

    def getNodeParentExt(self):
        return self.__parentExt

    def setNodeLabel(self, s):
        self.__node_label = s

    def setLineNr(self, s):
        self.__lineNr = s

    def setNodeSibling(self, s):
        self.__sibling = s

    def setNodeChild(self, s):
        self.__child = s

    def setNodeParent(self, s):
        self.__parent = s

    def setNodeDegree(self, s):
        self.__degree = s

    def setNodeOrdered (self, s):
        self.__ordered = s

    def getNodeLabel(self):
        return self.__node_label

    def getLineNr(self):
        return self.__lineNr

    def getNodeSibling(self):
        return self.__sibling

    def getNodeChild(self):
        return self.__child

    def getNodeParent(self):
        return self.__parent

    def getNodeDegree(self):
        return self.__degree

    def getNodeOrdered(self):
        return self.__ordered
