

class DFA(object):

    def __init__(self):
        super(DFA, self).__init__()
        self.states = list()
        self.paths = list()
        self.sStates = list()
        self.fStates = list()
        self.alphabet = list()

    def setStates(self, states, paths, sStates, fStates, alphabet):
        self.states = states
        self.paths = paths
        self.sStates = sStates
        self.fStates = fStates
        self.alphabet = alphabet

    def accept(self, string):
        exp = list(string)
        reached = list()
        paths = self.paths
        for s in self.sStates:
            flag = True
            for op in exp:
                if paths[s].has_key(op):
                    s = paths[s][op]
                else:
                    flag = False
            if flag & (s in self.fStates):
                reached.append(s)
        if len(reached):
            return True
        else:
            return False

    def minStates(self):
        paths = self.paths
        sStates = set(self.sStates)
        fStates = set(self.fStates)
        states = set(paths.keys())
        nfStates = states - fStates
        partition = list()
        partition.append(nfStates)
        partition.append(fStates)
        flag = True
        # partition process start
        while flag:
            flag = False
            newpartition = list()
            for i in range(len(partition)):
                part = dict()
                for s in partition[i]:
                    part[s] = self.getPart(s, partition)
                mapping = list()
                newpart = list()
                for s in partition[i]:
                    if part[s] not in mapping:
                        mapping.append(part[s])
                        newpart.append(set())
                for s in partition[i]:
                    for j in range(len(mapping)):
                        if part[s]==mapping[j]:
                            newpart[j].add(s)
                if len(newpart)>1:
                    flag = True
                newpartition.extend(newpart)
            partition = newpartition

        # partition process end
        newstates = [list(part)[0] for part in partition]
        category = {list(part)[0]:list(part)[1:] for part in partition}
        newpaths = dict()
        alphabet = self.alphabet
        for state in newstates:
            newpaths[state] = dict()
            for a in alphabet:
                b = paths[state][a]
                if b in newstates:
                    newpaths[state][a] = b
                else:
                    for key in category.keys():
                        if b in category[key]:
                            newpaths[state][a] = key
                            break
        newfStates = set()
        newsStates = set()
        for state in newstates:
            if state in fStates:
                newfStates.add(state)
        for state in newstates:
            if state in sStates:
                newsStates.add(state)
        self.setStates(newstates, newpaths, newsStates, newfStates, alphabet)


    def getPart(self, state, partition):
        paths = self.paths
        alphabet = self.alphabet
        result = list()
        for a in alphabet:
            dist = paths[state][a]
            for i in range(len(partition)):
                if dist in partition[i]:
                    result.append(i)
                    break
        return result

    def show(self):
        print 'states:', self.states
        print 'sStates:', self.sStates
        print 'fStates:', self.fStates
        print 'paths:'
        keys = self.paths.keys()
        for key in keys:
            print key, ':', self.paths[key]
        print 'alphabet:', self.alphabet

    def encode(self):
        dfa_data = {
            'states':self.states,
            'sStates':list(self.sStates),
            'fStates':list(self.fStates),
            'paths':self.paths,
            'alphabet':self.alphabet
        }
        return dfa_data


    def decode(self, dfa_data):
        self.states = dfa_data['states']
        self.sStates = set(dfa_data['sStates'])
        self.fStates = set(dfa_data['fStates'])
        self.paths = dfa_data['paths']
        self.alphabet = dfa_data['alphabet']

