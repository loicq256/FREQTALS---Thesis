#!/usr/bin/env python3
from freqt.src.be.intimals.freqt.structure.NodeFreqT import *


class ReadFile:

    """
     * create transaction from dictionary < pattern, supports>
     * argument 1: a dictionary <String, String>
     * argument 2: an list of list containing NodeFreqT elements
    """
    def createTransactionFromMap(self, inPatternsDict_dict, transListOfList_list):
        for elem in inPatternsDict_dict:
            tran_tmp_list = list()  # list of NodeFreqT
            self.str2node(elem, tran_tmp_list)
            transListOfList_list.append(tran_tmp_list)

    """
    * transform a string into node
    * argument 1: a string
    * argument 2: a list of node
    """
    def str2node(self, str, trans):
        length = len(str)
        size = 0
        buff = ""  # individual node
        tmp = list()  # a list of node

        ii = 0
        while ii < length:
            if str[ii] == '(' or str[ii] == ')':
                if len(buff) != 0:
                    if buff[0] == '*':
                        tmp.append(buff)
                    else:
                        label = buff.split("_")
                        tmp.append(label[0])
                    buff = ""
                    size += 1
                if str[ii] == ')':
                    tmp.append(')')
            else:
                if str[ii] == '\t' or str[ii] == ' ':
                    buff += "_"
                else:
                    # adding to find leaf node i.e. *X(120)
                    if str[ii] == '*':
                        bracket = 0
                        while bracket >= 0:
                            if str[ii] == '(':
                                bracket += 1
                            else:
                                if str[ii] == ')':
                                    bracket -= 1
                            if bracket == -1:
                                break
                            else:
                                buff += str[ii]
                                ii += 1
                        ii -= 1
                    else:
                        buff += str[ii]
            ii += 1
        if len(buff) != 0:
            print("buff: " + buff)
            raise Exception("ArithmeticException")
        # init a list of node
        sibling = [-1] * size
        for i in range(0, size):
            nodeTemp = NodeFreqT()
            nodeTemp.setNodeSibling(-1)
            nodeTemp.setNodeParent(-1)
            nodeTemp.setNodeChild(-1)
            trans.append(nodeTemp)
            sibling.append(-1)
        # create tree
        sr = list()
        id = 0
        for i in range(0, len(tmp)):
            if tmp[i] == ")":
                top = len(sr) - 1
                if top < 1:
                    continue
                child = sr[top]
                parent = sr[top-1]
                trans[child].setNodeParent(parent)
                if trans[parent].getNodeChild() == -1:
                    trans[parent].setNodeChild(child)
                if sibling[parent] != -1:
                    trans[sibling[parent]].setNodeSibling(child)
                sibling[parent] = child
                sr.pop(top)
            else:
                trans[id].setNodeLabel(tmp[i])
                sr.append(id)
                id += 1
