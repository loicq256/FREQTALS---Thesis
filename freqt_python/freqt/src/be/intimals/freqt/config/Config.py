#!/usr/bin/env python3

import sys
import traceback
from pyjavaproperties import Properties


class Config:
    __path = ""
    __prop = None

    def config(self, configPath):
        try:
            self.__path = configPath
            self.__prop = Properties()
            self.__prop.load(open(configPath))
        except:
            e = sys.exc_info()[0]
            print(e)
            trace = traceback.format_exc()
            print(trace)
            raise

    def get2Class(self):
        if self.__prop.getProperty("2Class") is not None and self.__prop.getProperty("2Class").lower() == "true":
            return True
        return False

    def getDSScore(self):
        try:
            return float(self.__prop.getProperty("minDSScore"))
        except:
            e = sys.exc_info()[0]
            print(e)
            raise

    def keepHighestScore(self):
        if self.__prop.getProperty("keepHighestScore") is not None and self.__prop.getProperty("keepHighestScore").lower() == "true":
            return True
        return False

    def getNumPatterns(self):
        return int(self.__prop.getProperty("numPatterns"))

    def getInputFiles1(self):
        if self.__prop.getProperty("inputPath1") is None:
            return ""
        return self.__prop.getProperty("inputPath1")

    def getInputFiles2(self):
        if self.__prop.getProperty("inputPath2") is None:
            return ""
        return self.__prop.getProperty("inputPath2")

    def getOutputMatches(self):
        if self.__prop.getProperty("outputMatches") is None:
            return ""
        return self.__prop.getProperty("outputMatches")

    def getOutputClusters(self):
        if self.__prop.getProperty("outputClusters") is None:
            return ""
        return self.__prop.getProperty("outputClusters")

    def getOutputClustersTemp(self):
        if self.__prop.getProperty("outputClustersTemp") is None:
            return ""
        return self.__prop.getProperty("outputClustersTemp")

    def getOutputCommonPatterns(self):
        if self.__prop.getProperty("outputCommonPatterns") is None:
            return ""
        return self.__prop.getProperty("outputCommonPatterns")

    def getOutputCommonMatches(self):
        if self.__prop.getProperty("outputCommonMatches") is None:
            return ""
        return self.__prop.getProperty("outputCommonMatches")

    def getOutputCommonClusters(self):
        if self.__prop.getProperty("outputCommonClusters") is None:
            return ""
        return self.__prop.getProperty("outputCommonClusters")

    def getOutputMatches1(self):
        if self.__prop.getProperty("outputMatches1") is None:
            return ""
        return self.__prop.getProperty("outputMatches1")

    def getOutputClusters1(self):
        if self.__prop.getProperty("outputClusters1") is None:
            return ""
        return self.__prop.getProperty("outputClusters1")

    def getOutputMatches2(self):
        if self.__prop.getProperty("outputMatches2") is None:
            return
        return self.__prop.getProperty("outputMatches2")

    def getOutputClusters2(self):
        if self.__prop.getProperty("outputClusters2") is None:
            return ""
        return self.__prop.getProperty("outputClusters2")

    def getWeighted(self):
        if self.__prop.getProperty("weighted") is not None and self.__prop.getProperty("weighted").lower() == "true":
            return True
        return False

    #######

    def getTwoStep(self):
        if self.__prop.getProperty("twoStep") is not None and self.__prop.getProperty("twoStep") == "true":
            return True
        return False

    def getFilter(self):
        if self.__prop.getProperty("filter") is not None and self.__prop.getProperty("filter") == "true":
            return True
        return False

    def getAbstractLeafs(self):
        if self.__prop.getProperty("abstractLeafs") is not None and self.__prop.getProperty("abstractLeafs") == "true":
            return True
        return False

    def getTimeout(self):
        if self.__prop.getProperty("timeout") is None:
            return sys.maxsize
        return float(self.__prop.getProperty("timeout"))

    def getProp(self):
        return self.__prop

    def buildGrammar(self):
        if self.__prop.getProperty("buildGrammar") is not None and self.__prop.getProperty("buildGrammar") == "true":
            return True
        return False

    def getGrammarFile(self):
        return self.__prop.getProperty("grammarFile")

    def getRootLabelFile(self):
        return self.__prop.getProperty("rootLabelFile")

    def getWhiteLabelFile(self):
        return self.__prop.getProperty("whiteLabelFile")

    def getXmlCharacterFile(self):
        return self.__prop.getProperty("xmlCharacterFile")

    def getInputFiles(self):
        return self.__prop.getProperty("inputPath")

    def getOutputFile(self):
        if self.__prop.getProperty("outputPath") is None:
            return ""
        return self.__prop.getProperty("outputPath")

    def getMinSupport(self):
        return int(self.__prop.getProperty("minSupport"))

    def getMinNode(self):
        return int(self.__prop.getProperty("minNode"))

    def getMaxNode(self):
        return int(self.__prop.getProperty("maxNode"))

    def getMinLeaf(self):
        return int(self.__prop.getProperty("minLeaf"))

    def getMaxLeaf(self):
        return int(self.__prop.getProperty("maxLeaf"))

    def postProcess(self):
        if self.__prop.getProperty("pos") is not None and self.__prop.getProperty("pos").lower() == "true":
            return True
        return False

    """
     * Returns a list of minimum-support values (only used when executing multiple Freq-T runs in parallel)
     * @return
    """
    def getMinSupportList(self):
        msList = self.__prop.getProperty("minSupportList")
        result = list()
        splitList = msList.split(",")
        for elem in splitList:
            result.append(int(elem))
        return result

    """
     * Returns a list of input folders (only used when executing multiple Freq-T runs in parallel)
     * @return
    """
    def getInputFilesList(self):
        ifList = self.__prop.getProperty("inFilesList")
        return ifList.split(",")
