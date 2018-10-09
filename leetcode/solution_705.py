#!/usr/bin/env python

import unittest

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = None

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.arr[key] == key

class MyHashSet2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.arr = [None] * self.size

    def _hash(self, key):
        return id(key) % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        nodes = self.arr[self._hash(key)]
        if nodes is not None:
            for node in nodes:
                if node == key:
                    return
            nodes.append(key)
        else:
            self.arr[self._hash(key)] = [key]

    def _get(self, key):
        nodes = self.arr[self._hash(key)]
        if nodes is not None:
            for node in nodes:
                if node == key:
                    return node

        return -1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        node = self._get(key)
        return node != -1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        nodes = self.arr[self._hash(key)]

        if nodes is None:
            return

        i = 0

        while i < len(nodes):
            if nodes[i] == key:
                del nodes[i]
                break
            i += 1

class TestSolution(unittest.TestCase):

    def test_MyHashSet(self):
        hashMap = MyHashSet()
        op = ["contains","remove","contains","add","remove","add","contains","add","add","add","remove","contains","remove","add","contains","remove","contains","remove","remove","contains","add","contains","contains","remove","remove","remove","add","add","add","contains","remove","contains","remove","add","add","add","contains","add","add","add","add","add","contains","add","add","remove","add","add","add","contains","add","add","add","add","add","add","remove","remove","add","add","add","add","add","add","remove","contains","add","contains","remove","remove","remove","add","add","contains","add","remove","add","contains","remove","add","contains","remove","contains","add","add","contains","contains","add","add","add","contains","remove","add","add","remove","remove","remove","remove","add","add","add","contains","add","add","add","add","add","contains","add","add","remove","remove","add","contains","add","add","add","add","add","contains","add","remove","add","remove","add","contains","contains","remove","add","add","add","remove","contains","add","add","contains","add","contains","add","contains","remove","add","contains","add","add","add","add","add","add","remove","add","add","remove","contains","add","remove","remove","add","contains","add","add","add","remove","add","add","add","add","contains","contains","add","add","add","add","add","contains","contains","remove","add","add","remove","remove","contains","contains","add","add","add","add","add","add","add","add","add","contains","add","remove","add","remove","contains","remove","remove","remove","contains","remove","add","contains","add","add","add","remove","add","contains","contains","contains","remove","add","contains","remove","add","add","add","contains","add","add","add","add","add","remove","add","add","remove","add","remove","remove","add","add","add","contains","add","contains","remove","contains","contains","add","add","add","add","contains","add","add","add","add","contains","add","add","add","contains","add","remove","add","add","add","add","contains","remove","contains","add","remove","add","add","add","add","add","add","remove","remove","remove","remove","add","remove","remove","remove","add","add","add","add","add","add","contains","add","remove","add","add","contains","add","add","add","add","add","add","contains","add","add","add","contains","add","remove","add","add","contains","contains","add","add","remove","add","remove","contains","add","contains","add","add","add","remove","add","add","contains","contains","add","remove","contains","add","contains","add","remove","contains","add","add","contains","add","add","contains","contains","contains","remove","add","contains","add","remove","add","add","contains","add","contains","add","add","add","add","add","contains","remove","add","remove","add","contains","contains","add","add","add","add","add","contains","remove","add","add","add","add","contains","remove","remove","remove","add","contains","remove","remove","contains","remove","contains","remove","add","contains","remove","add","contains","remove","add","remove","add","add","add","add","remove","add","add","add","add","add","add","contains","remove","contains","add","add","contains","remove","add","remove","contains","add","contains","remove","add","contains","contains","contains","add","contains","contains","contains","add","remove","add","add","remove","add","remove","add","contains","contains","add","add","remove","add","add","remove","contains","add","add","add","remove","contains","contains","remove","add","remove","contains","add","add","add","add","contains","add","contains","contains","contains","add","add","add","remove","add","add","add","contains","add","add","contains","contains","add","add","add","add","remove","add","add","remove","contains","add","add","remove","add","add","add","contains","contains","contains","add","add","add","add","add","add","remove","add","add","remove","add","add","contains","add","remove","add","remove","remove","remove","remove","remove","contains","add","remove","add","remove","remove","add","contains","add","add","add","add","contains","contains","add","add","add","add","add","contains","add","add","remove","add","remove","add","contains","add","add","remove","add","add","add","add","add","add","add","remove","add","contains","add","remove","contains","add","remove","add","add","add","add","remove","add","add","remove","add","add","remove","add","remove","contains","add","add","contains","add","remove","add","add","add","remove","remove","remove","add","contains","remove","add","add","add","add","add","add","remove","remove","remove","remove","add","add","add","add","add","add","remove","add","add","add","add","add","add","add","add","add","contains","contains","add","remove","add","add","add","add","remove","add","remove","remove","contains","add","contains","add","add","add","remove","add","contains","add","add","add","add","remove","add","contains","remove","add","remove","add","add","add","add","contains","contains","contains","add","add","remove","add","remove","remove","add","add","contains","contains","add","remove","contains","add","add","add","remove","contains","add","remove","add","add","contains","add","remove","add","remove","add","add","add","add","add","contains","add","remove","remove","add","add","remove","add","add","add","contains","remove","add","add","remove","add","add","add","add","add","contains","add","contains","remove","add","add","remove","add","add","add","remove","add","add","add","remove","add","add","remove","contains","remove","contains","remove","add","add","add","add","add","contains","contains","add","add","remove","add","remove","contains","remove","add","remove","add","add","add","add","add","contains","contains","add","add","add","add","contains","add","contains","add","add","add","remove","remove","contains","remove","add","remove","add","add","contains","remove","remove","remove","remove","remove","contains","contains","add","contains","add","contains","add","add","remove","add","add","add","add","add","add","remove","add","add","contains","add","remove","contains","remove","add","add","add","add","remove","contains","contains","add","contains","contains","add","add","contains","add","remove","remove","add","add","add","contains","add","add","add","add","remove","add","add","contains","contains","contains","remove","remove","add","add","add","add","remove","remove","add","remove","add","contains","add","add","add","add","contains","add","add","contains","contains","add","add","remove","add","contains","add","add","add","remove","remove","add","add","remove","contains","contains","add","contains","contains","remove","remove","remove","add","add","remove","remove","remove","add","contains","contains","add","add","contains","add","add","add","add","add","add","contains","add","add","remove","contains","add","add","remove","add","add","contains","contains","add","add","add","add","remove","add","add","remove","add","add","add","contains","add","add","contains","add","remove","remove","remove","add","remove","add","contains","remove","remove","remove","contains","add","add","remove","add","add","contains","add","add","contains","remove","add","add","add","add","contains","remove","add","contains","contains","contains","add","contains","contains","add","add","add","contains","contains","add","add","contains","add","add","contains","remove","remove","remove","remove","contains","add","add","contains","add","add","add","remove","add","add","remove","remove","add","contains","add","contains","remove","add","contains","contains","add","add","add","add","add","contains","remove","add","remove","add","add","add","contains","remove","add","add","contains","contains","add"]
        val = [[88],[130],[3],[952],[767],[206],[268],[658],[918],[709],[965],[558],[645],[667],[206],[404],[918],[139],[686],[71],[453],[918],[321],[597],[923],[296],[213],[203],[521],[213],[55],[418],[920],[616],[676],[825],[667],[304],[782],[3],[422],[131],[114],[641],[9],[992],[347],[850],[930],[304],[184],[58],[183],[198],[491],[322],[295],[484],[97],[298],[362],[210],[329],[177],[546],[3],[468],[724],[41],[804],[959],[339],[258],[453],[618],[94],[834],[97],[317],[589],[357],[430],[571],[477],[486],[203],[491],[626],[924],[267],[846],[333],[794],[238],[406],[397],[120],[939],[30],[452],[865],[422],[825],[246],[364],[17],[558],[183],[966],[935],[765],[741],[496],[422],[33],[66],[490],[629],[693],[697],[155],[29],[683],[667],[106],[66],[258],[134],[417],[97],[57],[790],[86],[69],[966],[364],[824],[258],[596],[422],[873],[25],[386],[334],[700],[794],[773],[203],[106],[861],[433],[253],[130],[616],[6],[535],[215],[770],[258],[947],[117],[633],[708],[117],[191],[490],[36],[117],[210],[522],[630],[951],[772],[831],[25],[988],[648],[980],[440],[729],[351],[273],[596],[770],[645],[320],[344],[57],[814],[985],[449],[475],[17],[317],[390],[896],[779],[770],[724],[496],[751],[91],[432],[557],[98],[22],[635],[774],[203],[876],[57],[106],[544],[153],[618],[433],[614],[166],[724],[910],[834],[42],[369],[348],[668],[450],[473],[390],[278],[993],[705],[673],[518],[927],[859],[447],[563],[971],[443],[611],[69],[831],[611],[4],[723],[230],[814],[786],[75],[568],[223],[533],[311],[163],[822],[714],[789],[566],[741],[594],[646],[460],[709],[805],[317],[617],[504],[39],[808],[190],[888],[709],[388],[607],[689],[237],[764],[445],[661],[677],[280],[935],[154],[165],[806],[791],[20],[667],[796],[184],[731],[286],[203],[975],[499],[97],[184],[934],[698],[743],[43],[613],[174],[258],[853],[278],[558],[520],[185],[521],[652],[0],[941],[617],[671],[831],[701],[741],[962],[848],[756],[653],[121],[696],[38],[853],[974],[461],[794],[380],[9],[763],[746],[246],[747],[15],[934],[593],[498],[825],[558],[196],[309],[146],[166],[39],[909],[797],[749],[824],[891],[43],[79],[798],[481],[611],[206],[148],[370],[96],[742],[463],[723],[641],[179],[497],[770],[987],[391],[749],[566],[603],[779],[483],[836],[499],[107],[451],[998],[668],[974],[317],[976],[673],[320],[772],[623],[64],[454],[714],[224],[6],[51],[634],[249],[460],[725],[980],[578],[712],[380],[319],[225],[782],[927],[255],[927],[28],[149],[454],[948],[875],[566],[978],[451],[70],[511],[258],[516],[758],[197],[185],[524],[243],[367],[976],[441],[942],[629],[942],[936],[325],[949],[999],[399],[286],[155],[992],[766],[884],[793],[328],[855],[493],[400],[771],[739],[157],[646],[166],[648],[566],[395],[42],[524],[597],[909],[492],[658],[932],[496],[369],[822],[930],[66],[655],[340],[866],[571],[929],[340],[577],[788],[319],[563],[675],[320],[521],[538],[40],[515],[556],[979],[894],[20],[389],[286],[814],[170],[555],[169],[32],[593],[476],[113],[535],[423],[29],[413],[171],[780],[73],[177],[866],[951],[268],[562],[720],[260],[691],[793],[834],[948],[60],[98],[516],[864],[624],[162],[156],[237],[234],[832],[871],[606],[840],[498],[191],[55],[14],[815],[590],[17],[225],[974],[883],[280],[490],[736],[851],[4],[857],[92],[105],[400],[63],[781],[192],[437],[300],[3],[271],[270],[460],[677],[272],[511],[885],[200],[560],[911],[47],[105],[445],[306],[94],[654],[663],[32],[624],[536],[584],[469],[840],[675],[200],[805],[848],[453],[771],[713],[81],[465],[156],[396],[554],[144],[406],[152],[110],[752],[419],[440],[669],[950],[691],[534],[37],[128],[859],[625],[527],[152],[230],[333],[836],[473],[322],[654],[329],[213],[462],[722],[404],[652],[821],[573],[839],[637],[495],[678],[161],[105],[567],[731],[683],[711],[908],[458],[501],[657],[491],[565],[328],[356],[374],[532],[739],[869],[811],[596],[155],[412],[217],[539],[618],[782],[942],[286],[542],[936],[519],[67],[4],[614],[925],[379],[883],[570],[278],[971],[388],[43],[72],[206],[529],[738],[248],[112],[919],[585],[30],[338],[826],[154],[864],[381],[787],[488],[533],[116],[10],[77],[119],[720],[275],[59],[657],[70],[398],[749],[988],[5],[304],[390],[807],[166],[441],[924],[355],[821],[648],[168],[433],[573],[300],[678],[741],[386],[808],[172],[343],[202],[8],[663],[150],[816],[611],[907],[432],[988],[630],[694],[22],[32],[115],[300],[926],[852],[925],[92],[175],[619],[471],[357],[300],[572],[954],[612],[998],[133],[351],[279],[234],[632],[936],[947],[524],[277],[757],[856],[916],[57],[187],[757],[495],[854],[808],[515],[551],[464],[795],[454],[860],[424],[692],[633],[998],[184],[710],[41],[753],[535],[558],[613],[390],[697],[460],[676],[905],[533],[544],[848],[749],[703],[8],[803],[149],[551],[816],[3],[908],[930],[733],[695],[781],[868],[165],[16],[211],[190],[422],[363],[684],[994],[788],[146],[789],[844],[804],[503],[167],[69],[771],[323],[323],[953],[687],[304],[458],[761],[378],[486],[654],[386],[364],[555],[823],[560],[606],[167],[781],[624],[867],[807],[243],[721],[296],[517],[11],[52],[203],[392],[519],[764],[306],[648],[390],[606],[905],[980],[54],[450],[905],[535],[590],[553],[600],[586],[648],[205],[70],[711],[648],[0],[212],[456],[636],[890],[770],[812],[589],[463],[154],[451],[209],[243],[715],[164],[698],[156],[996],[395],[905],[66],[90],[98],[482],[416],[474],[637],[197],[979],[494],[789],[831],[189],[205],[711],[340],[63],[323],[372],[570],[266],[848],[728],[472],[764],[489],[803],[814],[533],[257],[569],[136],[360],[264],[522],[919],[701],[707],[924],[901],[276],[870],[180],[534],[916],[843],[183],[432],[550],[347],[211],[930],[858],[851],[577],[257],[157],[259],[329],[915],[253],[96],[416],[883],[138],[856],[4],[109],[755],[901],[487],[103],[422],[647],[451],[200],[820],[42],[616],[459],[562],[954],[656],[950],[141],[290],[407],[808],[58],[574],[840],[622],[832],[857],[723],[267],[14],[215],[860],[862],[630],[133],[724],[595],[51],[588],[180],[546],[842],[635],[930],[787],[334],[534],[391],[765]]
        null, false, true = 'null', 'false', 'true'
        expected = [false,null,false,null,null,null,false,null,null,null,null,false,null,null,true,null,true,null,null,false,null,true,false,null,null,null,null,null,null,true,null,false,null,null,null,null,true,null,null,null,null,null,false,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,false,null,null,null,null,null,true,null,null,null,true,null,null,false,null,false,null,null,true,true,null,null,null,false,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,true,null,null,null,null,null,true,null,null,null,null,null,false,null,null,null,null,null,true,true,null,null,null,null,null,false,null,null,true,null,true,null,true,null,null,false,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,true,null,null,null,null,null,null,null,null,true,true,null,null,null,null,null,true,false,null,null,null,null,null,false,true,null,null,null,null,null,null,null,null,null,true,null,null,null,null,true,null,null,null,false,null,null,false,null,null,null,null,null,true,true,false,null,null,true,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,false,null,true,true,null,null,null,null,true,null,null,null,null,false,null,null,null,false,null,null,null,null,null,null,true,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,false,null,null,null,true,null,null,null,null,false,true,null,null,null,null,null,true,null,true,null,null,null,null,null,null,false,true,null,null,true,null,true,null,null,true,null,null,true,null,null,true,true,false,null,null,true,null,null,null,null,true,null,true,null,null,null,null,null,false,null,null,null,null,true,true,null,null,null,null,null,true,null,null,null,null,null,true,null,null,null,null,true,null,null,false,null,true,null,null,false,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,false,null,null,false,null,null,null,false,null,true,null,null,false,false,false,null,false,false,false,null,null,null,null,null,null,null,null,true,true,null,null,null,null,null,null,false,null,null,null,null,true,true,null,null,null,true,null,null,null,null,true,null,false,true,true,null,null,null,null,null,null,null,false,null,null,true,false,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,false,false,true,null,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,false,null,null,null,null,true,true,null,null,null,null,null,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,null,false,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,true,null,null,null,null,null,null,null,null,null,null,true,null,false,null,null,null,null,null,true,null,null,null,null,null,null,true,null,null,null,null,null,null,null,false,false,true,null,null,null,null,null,null,null,null,false,true,null,null,false,null,null,null,null,false,null,null,null,null,false,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,true,null,true,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,true,null,null,null,null,null,null,true,false,null,null,null,null,null,false,null,null,null,null,null,null,null,null,true,true,null,null,null,null,true,null,true,null,null,null,null,null,false,null,null,null,null,null,true,null,null,null,null,null,true,true,null,false,null,true,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,false,null,null,null,null,null,null,true,true,null,false,false,null,null,true,null,null,null,null,null,null,false,null,null,null,null,null,null,null,true,true,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,false,null,null,false,true,null,null,null,null,true,null,null,null,null,null,null,null,null,true,false,null,true,true,null,null,null,null,null,null,null,null,null,true,false,null,null,false,null,null,null,null,null,null,true,null,null,null,false,null,null,null,null,null,true,true,null,null,null,null,null,null,null,null,null,null,null,false,null,null,true,null,null,null,null,null,null,null,true,null,null,null,true,null,null,null,null,null,true,null,null,true,null,null,null,null,null,true,null,null,false,false,true,null,true,true,null,null,null,true,false,null,null,true,null,null,true,null,null,null,null,true,null,null,true,null,null,null,null,null,null,null,null,null,true,null,true,null,null,true,true,null,null,null,null,null,true,null,null,null,null,null,null,true,null,null,null,true,true,null]
        actual = []

        for operation,value in zip(op, val):
            if operation == "contains":
                actual.append(true if getattr(hashMap, operation)(*value) else false)
            elif operation in ["remove", "add"]:
                getattr(hashMap, operation)(*value)
                actual.append(null)

        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
