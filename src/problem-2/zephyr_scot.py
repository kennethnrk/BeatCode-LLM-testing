def Solve(envelopes):
    if not envelopes:
        return 0
    maxEnvelopes = 1
    for I in range(1, len(envelopes)):
        for j in range(I):
            if envelopes[j][0] < envelopes[I][0] and envelopes[j][1] < envelopes[I][1]:
                maxEnvelopes = max(maxEnvelopes, Solve(envelopes[j:I+1]) + 1)
        maxEnvelopes = max(maxEnvelopes, Solve(envelopes[I:I+1]) + 1)
    return maxEnvelopes
